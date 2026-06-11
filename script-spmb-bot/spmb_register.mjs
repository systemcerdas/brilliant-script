import { chromium } from 'playwright';
import { createDecipheriv } from 'crypto';
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const outDir = join(__dirname, 'spmb_output');
mkdirSync(outDir, { recursive: true });

/** Kunci enkripsi HTTP interceptor SPMB (AES-256-CBC) */
const SPMB_AES_KEY = Buffer.from('54F4a4E/Dd16c36E!@#a57fd8Ab46E90', 'utf8');
const SPMB_AES_IV = Buffer.from('021326!@#1o41A$m', 'utf8');

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
    const json = Buffer.from(parts[1], 'base64url').toString('utf8');
    return JSON.parse(json);
  } catch {
    return null;
  }
}

/** Dekripsi field `response` dari body API SPMB */
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

/** Ubah body mentah menjadi pesan yang bisa dibaca */
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
    return {
      raw: body,
      message: null,
      statusCode: null,
      decrypted: null,
      hint: 'Body terenkripsi, dekripsi gagal',
    };
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

function suggestAction(message, httpStatus) {
  const msg = (message || '').toLowerCase();
  if (msg.includes('sudah ada') || msg.includes('sudah terdaftar')) {
    return 'NIK sudah ada di SPMB. Hubungi Sekolah Asal (PAUD/bimba) atau Sekolah Tujuan untuk mendapatkan akun, lalu login — jangan registrasi ulang.';
  }
  if (msg.includes('recaptcha') || msg.includes('captcha')) {
    return 'Validasi reCAPTCHA gagal. Coba lagi di browser biasa (bukan otomatis) atau ganti jaringan/perangkat.';
  }
  if (httpStatus >= 500) {
    return 'Server SPMB bermasalah. Coba lagi nanti atau hubungi help desk Disdik Kab. Bogor.';
  }
  if (!message && httpStatus === 400) {
    return 'Server menolak (400) tanpa pesan terbaca. Buka DevTools → Network → akunRegistrasi → Response.';
  }
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

const data = loadRegistrationData(__dirname);
const apiLog = [];

async function captureToasts(page) {
  return page.evaluate(() =>
    [...document.querySelectorAll('.p-toast-message-text, .p-toast-detail, .p-message-text')]
      .map((el) => el.textContent?.trim())
      .filter(Boolean)
  );
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    userAgent:
      'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    locale: 'id-ID',
  });
  const page = await context.newPage();

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
      suggestion: suggestAction(interpreted.message, res.status()),
    });
  });

  const jkValue = data.jenis_kel?.toLowerCase().includes('perempuan') ? 'P' : 'L';
  const jkLabel = jkValue === 'P' ? 'Perempuan' : 'Laki - laki';

  console.log('Membuka halaman register...');
  await page.goto('https://spmb.bogorkab.go.id/register', {
    waitUntil: 'networkidle',
    timeout: 90000,
  });
  await page.waitForTimeout(2000);
  await page.screenshot({ path: join(outDir, '01-register.png'), fullPage: true });

  // Langkah 1: pilih SD
  await page.locator('text=SD').first().click();
  await page.waitForTimeout(500);
  await page.getByRole('button', { name: 'Lanjutkan' }).click();
  await page.waitForTimeout(2000);
  await page.screenshot({ path: join(outDir, '02-step2.png'), fullPage: true });
  console.log('Jenjang SD dipilih, masuk langkah 2');

  // Langkah 2: isi form
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

  // Submit
  await page.getByRole('button', { name: 'Daftar' }).click();
  await page.waitForTimeout(8000);
  await page.screenshot({ path: join(outDir, '04-result.png'), fullPage: true });

  const toasts = await captureToasts(page);
  const regEntry = apiLog.find((e) => e.endpoint === 'akunRegistrasi');

  writeFileSync(join(outDir, 'api-log.json'), JSON.stringify({ toasts, entries: apiLog }, null, 2));

  console.log('\n=== HASIL REGISTRASI ===');
  if (regEntry) {
    console.log(`HTTP status   : ${regEntry.httpStatus}`);
    console.log(`Status kode   : ${regEntry.statusCode ?? '(tidak ada)'}`);
    console.log(`Pesan server  : ${regEntry.message ?? '(tidak terdekripsi)'}`);
    if (regEntry.suggestion) console.log(`Saran         : ${regEntry.suggestion}`);
    if (regEntry.parsed && typeof regEntry.parsed === 'object') {
      console.log('Detail        :', JSON.stringify(regEntry.parsed, null, 2));
    }
  } else {
    console.log('Tidak ada request akunRegistrasi tercatat.');
  }

  if (toasts.length) {
    console.log('\nToast di halaman (bisa generik):');
    for (const t of [...new Set(toasts)]) console.log(`  - ${t}`);
  }

  console.log('\nLog lengkap: spmb_output/api-log.json');

  await browser.close();
}

main().catch((err) => {
  console.error('FATAL:', err);
  process.exit(1);
});
