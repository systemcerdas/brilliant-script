import { chromium } from 'playwright';
import { createDecipheriv } from 'crypto';
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const outDir = join(__dirname, 'spmb_output');
mkdirSync(outDir, { recursive: true });

const SPMB_AES_KEY = Buffer.from('54F4a4E/Dd16c36E!@#a57fd8Ab46E90', 'utf8');
const SPMB_AES_IV = Buffer.from('021326!@#1o41A$m', 'utf8');

const args = process.argv.slice(2);
const checkLogin = args.includes('--check-login') || args.includes('--login');
const checkRegister = !checkLogin;

function parseData(path) {
  const raw = readFileSync(path, 'utf8');
  const data = {};
  for (const line of raw.split(/\r?\n/)) {
    const m = line.match(/^([^:]+):(.*)$/);
    if (m) data[m[1].trim()] = m[2].trim();
  }
  return data;
}

function parseJwtPayload(token) {
  const parts = String(token).split('.');
  if (parts.length !== 3) return null;
  try {
    return JSON.parse(Buffer.from(parts[1], 'base64url').toString('utf8'));
  } catch {
    return null;
  }
}

function decryptSpmbCipher(cipherB64) {
  if (!cipherB64 || typeof cipherB64 !== 'string') return null;
  try {
    const decipher = createDecipheriv('aes-256-cbc', SPMB_AES_KEY, SPMB_AES_IV);
    let plain = decipher.update(cipherB64, 'base64', 'utf8');
    plain += decipher.final('utf8');
    return plain;
  } catch {
    return null;
  }
}

function interpretSpmbBody(body) {
  if (!body || typeof body !== 'object') {
    return { raw: body, message: null, statusCode: null, parsed: null };
  }

  if (body.message && typeof body.message === 'string') {
    return {
      raw: body,
      message: body.message,
      statusCode: body.status_code ?? body.statusCode ?? null,
      parsed: body,
    };
  }

  const cipher = body.response ?? body.data;
  if (typeof cipher !== 'string') {
    return { raw: body, message: null, statusCode: null, parsed: body };
  }

  const decrypted = decryptSpmbCipher(cipher);
  if (!decrypted) {
    return { raw: body, message: null, statusCode: null, decrypted: null, hint: 'Dekripsi gagal' };
  }

  let parsed = null;
  try {
    parsed = JSON.parse(decrypted);
  } catch {
    parsed = decrypted;
  }

  if (typeof parsed === 'string') {
    const jwt = parseJwtPayload(parsed);
    if (jwt) {
      return {
        raw: body,
        decrypted,
        parsed: jwt,
        message: jwt.message ?? null,
        statusCode: jwt.status_code ?? jwt.statusCode ?? null,
      };
    }
    return { raw: body, decrypted, parsed, message: parsed, statusCode: null };
  }

  return {
    raw: body,
    decrypted,
    parsed,
    message: parsed?.message ?? parsed?.error ?? null,
    statusCode: parsed?.status_code ?? parsed?.statusCode ?? null,
  };
}

function suggestAction(message, httpStatus, mode) {
  const msg = (message || '').toLowerCase();

  if (mode === 'login') {
    if (msg.includes('success')) return 'Login berhasil.';
    if (msg.includes('password') || msg.includes('sandi') || msg.includes('salah')) {
      return 'Password salah. Minta reset ke Operator Sekolah Asal/Tujuan — bukan password registrasi mandiri jika belum pernah daftar sendiri.';
    }
    if (msg.includes('tidak ditemukan') || msg.includes('belum terdaftar')) {
      return 'Akun belum ada atau username salah. Hubungi sekolah asal untuk aktivasi akun.';
    }
    if (httpStatus === 203 || httpStatus === 400) {
      return 'Login ditolak. Kemungkinan password dari sekolah berbeda, atau akun belum diaktifkan operator.';
    }
  }

  if (msg.includes('sudah ada') || msg.includes('sudah terdaftar')) {
    return 'NIK sudah ada di SPMB. Hubungi Sekolah Asal/Tujuan untuk mendapatkan akun, lalu login.';
  }
  if (msg.includes('recaptcha') || msg.includes('captcha')) {
    return 'Validasi reCAPTCHA gagal. Coba di browser biasa.';
  }
  if (httpStatus >= 500) return 'Server SPMB bermasalah. Coba lagi nanti.';
  return null;
}

function loadRegistrationData(dir) {
  const dataPath = join(dir, '.data');
  const examplePath = join(dir, '.data.example');
  if (!existsSync(dataPath)) {
    console.error('File .data tidak ditemukan.');
    console.error(`Salin ${examplePath} → ${dataPath} lalu isi data asli.`);
    process.exit(1);
  }
  return parseData(dataPath);
}

function printResult(title, entry, extra = {}) {
  console.log(`\n=== ${title} ===`);
  if (!entry) {
    console.log('Tidak ada respons API tercatat.');
    return;
  }
  console.log(`HTTP status   : ${entry.httpStatus}`);
  console.log(`Status kode   : ${entry.statusCode ?? '(tidak ada)'}`);
  console.log(`Pesan server  : ${entry.message ?? '(tidak terdekripsi)'}`);
  if (entry.suggestion) console.log(`Saran         : ${entry.suggestion}`);
  if (extra.url) console.log(`URL halaman   : ${extra.url}`);
  if (extra.loggedIn != null) console.log(`Login OK      : ${extra.loggedIn ? 'ya' : 'tidak'}`);
  if (entry.parsed && typeof entry.parsed === 'object') {
    console.log('Detail        :', JSON.stringify(entry.parsed, null, 2));
  }
}

async function captureToasts(page) {
  return page.evaluate(() =>
    [...document.querySelectorAll('.p-toast-message-text, .p-toast-detail, .p-message-text')]
      .map((el) => el.textContent?.trim())
      .filter(Boolean)
  );
}

function attachApiLogger(page, apiLog, mode) {
  page.on('response', async (res) => {
    const url = res.url();
    if (!url.includes('ppdb-service')) return;

    let body = null;
    try {
      body = await res.json();
    } catch {
      try {
        body = await res.text();
      } catch {
        body = null;
      }
    }

    const interpreted = interpretSpmbBody(body);
    apiLog.push({
      url,
      endpoint: url.split('/').slice(-1)[0],
      httpStatus: res.status(),
      ...interpreted,
      suggestion: suggestAction(interpreted.message, res.status(), mode),
    });
  });
}

async function createSession() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    userAgent:
      'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    locale: 'id-ID',
  });
  return { browser, page: await context.newPage() };
}

async function runCheckLogin(data, apiLog) {
  const { browser, page } = await createSession();
  attachApiLogger(page, apiLog, 'login');

  console.log('Membuka halaman login...');
  await page.goto('https://spmb.bogorkab.go.id/login', {
    waitUntil: 'networkidle',
    timeout: 90000,
  });
  await page.waitForTimeout(2000);

  const userInput = page.getByPlaceholder(/username|nik|masukan/i).first();
  if ((await userInput.count()) > 0) {
    await userInput.fill(data.nik);
  } else {
    await page.locator('input:visible').first().fill(data.nik);
  }

  await page.locator('input[type="password"]').first().fill(data.pass);
  console.log(`Mencoba login NIK: ${data.nik}`);

  await page.getByRole('button', { name: /login|masuk/i }).click();
  await page.waitForTimeout(8000);
  await page.screenshot({ path: join(outDir, 'login-result.png'), fullPage: true });

  const finalUrl = page.url();
  const loggedIn = /\/akun(\/|$)/.test(finalUrl) && !finalUrl.includes('/login');
  const token = await page.evaluate(() => localStorage.getItem('access_token'));
  const toasts = await captureToasts(page);
  const authEntry =
    [...apiLog].reverse().find((e) => e.endpoint === 'akunAutentikasi') ??
    apiLog.find((e) => e.endpoint === 'akunAutentikasi');

  writeFileSync(
    join(outDir, 'login-log.json'),
    JSON.stringify({ toasts, loggedIn, finalUrl, hasToken: Boolean(token), entries: apiLog }, null, 2)
  );

  printResult('HASIL LOGIN', authEntry, { url: finalUrl, loggedIn: loggedIn || Boolean(token) });

  if (toasts.length) {
    console.log('\nToast di halaman:');
    for (const t of [...new Set(toasts)]) console.log(`  - ${t}`);
  }

  console.log('\nLog lengkap: spmb_output/login-log.json');
  await browser.close();
}

async function runRegister(data, apiLog) {
  const { browser, page } = await createSession();
  attachApiLogger(page, apiLog, 'register');

  const jkValue = data.jenis_kel?.toLowerCase().includes('perempuan') ? 'P' : 'L';
  const jkLabel = jkValue === 'P' ? 'Perempuan' : 'Laki - laki';

  console.log('Membuka halaman register...');
  await page.goto('https://spmb.bogorkab.go.id/register', {
    waitUntil: 'networkidle',
    timeout: 90000,
  });
  await page.waitForTimeout(2000);
  await page.screenshot({ path: join(outDir, '01-register.png'), fullPage: true });

  await page.locator('text=SD').first().click();
  await page.waitForTimeout(500);
  await page.getByRole('button', { name: 'Lanjutkan' }).click();
  await page.waitForTimeout(2000);
  await page.screenshot({ path: join(outDir, '02-step2.png'), fullPage: true });
  console.log('Jenjang SD dipilih, masuk langkah 2');

  await page.getByPlaceholder('Masukan Nama Lengkap').fill(data.nama);
  await page.getByPlaceholder('Masukan NIK').fill(data.nik);
  if (data.nisn && data.nisn !== 'null') {
    await page.getByPlaceholder('Masukan NISN').fill(data.nisn);
  }
  await page.locator('input[type="password"]').nth(0).fill(data.pass);
  await page.locator('input[type="password"]').nth(1).fill(data.pass);
  await page.getByText(jkLabel, { exact: true }).click();
  await page.waitForTimeout(1000);
  await page.screenshot({ path: join(outDir, '03-filled.png'), fullPage: true });
  console.log(`Form diisi: ${data.nama} | NIK ${data.nik} | ${jkLabel}`);

  await page.getByRole('button', { name: 'Daftar' }).click();
  await page.waitForTimeout(8000);
  await page.screenshot({ path: join(outDir, '04-result.png'), fullPage: true });

  const toasts = await captureToasts(page);
  const regEntry = apiLog.find((e) => e.endpoint === 'akunRegistrasi');

  writeFileSync(join(outDir, 'api-log.json'), JSON.stringify({ toasts, entries: apiLog }, null, 2));

  printResult('HASIL REGISTRASI', regEntry);

  if (toasts.length) {
    console.log('\nToast di halaman (bisa generik):');
    for (const t of [...new Set(toasts)]) console.log(`  - ${t}`);
  }

  console.log('\nLog lengkap: spmb_output/api-log.json');
  await browser.close();
}

async function main() {
  const data = loadRegistrationData(__dirname);
  const apiLog = [];

  if (checkLogin) {
    await runCheckLogin(data, apiLog);
  } else if (checkRegister) {
    await runRegister(data, apiLog);
  }
}

main().catch((err) => {
  console.error('FATAL:', err.message || err);
  if (err.code === 'ERR_INVALID_PACKAGE_CONFIG') {
    console.error('\nnode_modules rusak (sering di Google Drive). Coba:');
    console.error('  Remove-Item -Recurse -Force node_modules');
    console.error('  npm install');
    console.error('  npx playwright install chromium');
  }
  process.exit(1);
});
