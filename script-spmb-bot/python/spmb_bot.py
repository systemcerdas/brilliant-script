"""
spmb_bot.py — SPMB Kabupaten Bogor · Versi Python
===================================================
Fitur:
  - Registrasi akun SD (default)
  - Cek login / verifikasi akun
  - Mode AUDIT: diagnosis lengkap status akun (registrasi + login + analisis)

Dependensi:
  pip install playwright pycryptodome
  playwright install chromium

Penggunaan:
  python spmb_bot.py                  → registrasi SD
  python spmb_bot.py --login          → cek login saja
  python spmb_bot.py --audit          → audit lengkap (register check + login check)
  python spmb_bot.py --help           → bantuan

File konfigurasi: .data (format key:value, sama dengan versi JS)
"""

import argparse
import base64
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# ─── Pastikan playwright tersedia ───────────────────────────────────────────
try:
    from playwright.sync_api import sync_playwright, Response
except ImportError:
    print("[ERROR] Playwright belum ter-install.")
    print("  Jalankan: pip install playwright && playwright install chromium")
    sys.exit(1)

# ─── Deteksi library kriptografi yang tersedia ───────────────────────────────
USE_PYCRYPTODOME = False
USE_CRYPTOGRAPHY = False

try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    USE_PYCRYPTODOME = True
except ImportError:
    try:
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.backends import default_backend
        USE_CRYPTOGRAPHY = True
    except ImportError:
        pass

# ─── Konstanta ──────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).parent.resolve()
OUT_DIR      = SCRIPT_DIR / "spmb_output"
DATA_FILE    = SCRIPT_DIR / ".data"
DATA_EXAMPLE = SCRIPT_DIR / ".data.example"

SPMB_URL  = "https://spmb.bogorkab.go.id"
AES_KEY   = b"54F4a4E/Dd16c36E!@#a57fd8Ab46E90"
AES_IV    = b"021326!@#1o41A$m"
MOBILE_UA = (
    "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
)

OUT_DIR.mkdir(parents=True, exist_ok=True)

# ─── Warna terminal (Windows-compatible) ────────────────────────────────────
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    BLUE   = "\033[94m"
    DIM    = "\033[2m"

def _enable_ansi():
    if sys.platform == "win32":
        import ctypes
        kernel = ctypes.windll.kernel32
        kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)

_enable_ansi()

def cprint(color: str, msg: str):
    print(f"{color}{msg}{C.RESET}")

def banner(title: str):
    line = "-" * (len(title) + 4)
    print(f"\n{C.CYAN}{C.BOLD}+{line}+")
    print(f"|  {title}  |")
    print(f"+{line}+{C.RESET}")

# ─── Parsing .data ──────────────────────────────────────────────────────────
def parse_data(path: Path) -> dict:
    if not path.exists():
        cprint(C.RED, f"[ERROR] File {path} tidak ditemukan.")
        cprint(C.YELLOW, f"  Salin {DATA_EXAMPLE} → {DATA_FILE} lalu isi data asli.")
        sys.exit(1)
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split(":", 1)
        if len(parts) == 2:
            result[parts[0].strip()] = parts[1].strip()
    return result

# ─── Dekripsi AES-256-CBC ────────────────────────────────────────────────────
def decrypt_spmb(cipher_b64: str):
    if not cipher_b64 or not isinstance(cipher_b64, str):
        return None
    try:
        raw = base64.b64decode(cipher_b64)
        if USE_PYCRYPTODOME:
            cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
            decrypted = unpad(cipher.decrypt(raw), AES.block_size)
            return decrypted.decode("utf-8")
        elif USE_CRYPTOGRAPHY:
            cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(AES_IV), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted = decryptor.update(raw) + decryptor.finalize()
            pad_len = decrypted[-1]
            return decrypted[:-pad_len].decode("utf-8")
        else:
            return None
    except Exception:
        return None

# ─── Parsing JWT payload ─────────────────────────────────────────────────────
def parse_jwt_payload(token: str):
    try:
        parts = str(token).split(".")
        if len(parts) != 3:
            return None
        payload_b64 = parts[1] + "=" * (4 - len(parts[1]) % 4)
        return json.loads(base64.urlsafe_b64decode(payload_b64).decode("utf-8"))
    except Exception:
        return None

# ─── Interpretasi body respons SPMB ─────────────────────────────────────────
def interpret_spmb_body(body) -> dict:
    if not body or not isinstance(body, dict):
        return {"raw": body, "message": None, "status_code": None, "parsed": None}

    # Body non-enkripsi (error langsung dari server)
    if "message" in body and isinstance(body["message"], str):
        return {
            "raw": body,
            "message": body["message"],
            "status_code": body.get("status_code") or body.get("statusCode"),
            "parsed": body,
        }

    cipher = body.get("response") or body.get("data")
    if not isinstance(cipher, str):
        return {"raw": body, "message": None, "status_code": None, "parsed": body}

    decrypted = decrypt_spmb(cipher)
    if not decrypted:
        return {
            "raw": body,
            "message": None,
            "status_code": None,
            "hint": "Dekripsi gagal — install pycryptodome: pip install pycryptodome",
        }

    try:
        parsed = json.loads(decrypted)
    except Exception:
        parsed = decrypted

    if isinstance(parsed, str):
        jwt = parse_jwt_payload(parsed)
        if jwt:
            return {
                "raw": body,
                "decrypted": decrypted,
                "parsed": jwt,
                "message": jwt.get("message"),
                "status_code": jwt.get("status_code") or jwt.get("statusCode"),
            }
        return {"raw": body, "decrypted": decrypted, "parsed": parsed, "message": parsed, "status_code": None}

    return {
        "raw": body,
        "decrypted": decrypted,
        "parsed": parsed,
        "message": (parsed.get("message") or parsed.get("error")) if isinstance(parsed, dict) else None,
        "status_code": (parsed.get("status_code") or parsed.get("statusCode")) if isinstance(parsed, dict) else None,
    }

# ─── Saran tindakan ──────────────────────────────────────────────────────────
def suggest_action(message, http_status: int, mode: str):
    msg = (message or "").lower()

    if mode == "login":
        if "success" in msg:
            return "✅ Login berhasil."
        if any(x in msg for x in ["password", "sandi", "salah"]):
            return (
                "Password salah. Minta reset ke Operator Sekolah Asal/Tujuan — "
                "bukan password registrasi mandiri jika belum pernah daftar sendiri."
            )
        if any(x in msg for x in ["tidak ditemukan", "belum terdaftar"]):
            return "Akun belum ada atau username salah. Hubungi sekolah asal untuk aktivasi akun."
        if http_status in (203, 400):
            return "Login ditolak. Kemungkinan password dari sekolah berbeda, atau akun belum diaktifkan operator."

    if any(x in msg for x in ["sudah ada", "sudah terdaftar", "already"]):
        return "NIK sudah ada di SPMB. Hubungi Sekolah Asal/Tujuan untuk mendapatkan akun, lalu login."
    if any(x in msg for x in ["recaptcha", "captcha"]):
        return "Validasi reCAPTCHA gagal. Coba di browser biasa."
    if http_status >= 500:
        return "Server SPMB bermasalah. Coba lagi nanti."
    return None

# ─── Utilities browser ───────────────────────────────────────────────────────
def capture_toasts(page) -> list:
    try:
        return page.evaluate("""
            () => [...document.querySelectorAll(
                '.p-toast-message-text, .p-toast-detail, .p-message-text'
            )].map(el => el.textContent?.trim()).filter(Boolean)
        """)
    except Exception:
        return []

def attach_api_logger(page, api_log: list, mode: str):
    def on_response(res):
        url = res.url
        if "ppdb-service" not in url:
            return
        try:
            body = res.json()
        except Exception:
            try:
                body = res.text()
            except Exception:
                body = None

        interpreted = interpret_spmb_body(body)
        api_log.append({
            "url": url,
            "endpoint": url.split("/")[-1],
            "http_status": res.status,
            **interpreted,
            "suggestion": suggest_action(interpreted.get("message"), res.status, mode),
        })

    page.on("response", on_response)

def create_session(playwright, headless=True):
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context(
        viewport={"width": 390, "height": 844},
        user_agent=MOBILE_UA,
        locale="id-ID",
    )
    return browser, context.new_page()

# ─── Print hasil ─────────────────────────────────────────────────────────────
def print_result(title: str, entry, extra: dict = {}):
    banner(title)
    if not entry:
        cprint(C.DIM, "  Tidak ada respons API tercatat.")
        return

    http_st = entry.get("http_status", "-")
    msg     = entry.get("message")
    sug     = entry.get("suggestion")
    sc      = entry.get("status_code")

    color = C.GREEN if isinstance(http_st, int) and http_st < 300 else (
        C.YELLOW if isinstance(http_st, int) and http_st < 500 else C.RED
    )
    cprint(color,  f"  HTTP status   : {http_st}")
    print(         f"  Status kode   : {sc or '(tidak ada)'}")
    cprint(C.BOLD, f"  Pesan server  : {msg or '(tidak terdekripsi)'}")

    if sug:
        cprint(C.YELLOW, f"  Saran         : {sug}")
    if "url" in extra:
        print(f"  URL halaman   : {extra['url']}")
    if "logged_in" in extra:
        cprint(C.GREEN if extra["logged_in"] else C.RED,
               f"  Login OK      : {'✅ ya' if extra['logged_in'] else '❌ tidak'}")

    parsed = entry.get("parsed")
    if parsed and isinstance(parsed, dict):
        print(f"  Detail        :\n{json.dumps(parsed, indent=4, ensure_ascii=False)}")

# ─── Mode: CHECK LOGIN ────────────────────────────────────────────────────────
def run_check_login(data: dict, api_log: list, playwright, headless=True) -> tuple:
    cprint(C.CYAN, "\n🔍 Memulai cek login...")
    browser, page = create_session(playwright, headless=headless)
    attach_api_logger(page, api_log, "login")

    try:
        cprint(C.DIM, "  Membuka halaman login...")
        page.goto(f"{SPMB_URL}/login", wait_until="networkidle", timeout=90_000)
        page.wait_for_timeout(2000)

        # Isi username
        user_input = page.get_by_placeholder("username") \
                         .or_(page.get_by_placeholder("NIK")) \
                         .or_(page.get_by_placeholder("masukan"))
        if user_input.count() > 0:
            user_input.first.fill(data["nik"])
        else:
            page.locator("input:visible").first.fill(data["nik"])

        page.locator('input[type="password"]').first.fill(data["pass"])
        cprint(C.DIM, f"  Mencoba login NIK: {data['nik']}")

        login_btn = page.get_by_role("button", name="Login").or_(
            page.get_by_role("button", name="Masuk")
        )
        login_btn.first.click()
        page.wait_for_timeout(8000)
        page.screenshot(path=str(OUT_DIR / "login-result.png"), full_page=True)

        final_url = page.url
        logged_in = "/akun" in final_url and "/login" not in final_url
        token     = page.evaluate("() => localStorage.getItem('access_token')")
        toasts    = capture_toasts(page)

        auth_entry = next(
            (e for e in reversed(api_log) if e["endpoint"] == "akunAutentikasi"), None
        )

        (OUT_DIR / "login-log.json").write_text(
            json.dumps({
                "timestamp": datetime.now().isoformat(),
                "nik": data["nik"],
                "toasts": toasts,
                "logged_in": logged_in,
                "final_url": final_url,
                "has_token": bool(token),
                "entries": api_log,
            }, indent=2, ensure_ascii=False, default=str),
            encoding="utf-8"
        )

        print_result("HASIL LOGIN", auth_entry, {
            "url": final_url,
            "logged_in": logged_in or bool(token),
        })

        if toasts:
            cprint(C.BLUE, "\n  Toast di halaman:")
            for t in set(toasts):
                cprint(C.BLUE, f"    ▸ {t}")

        cprint(C.DIM, "\n  Log     : spmb_output/login-log.json")
        cprint(C.DIM, "  Screenshot : spmb_output/login-result.png")

        return logged_in or bool(token), auth_entry

    finally:
        browser.close()

# ─── Mode: REGISTRASI ─────────────────────────────────────────────────────────
def run_register(data: dict, api_log: list, playwright, headless=True) -> dict:
    cprint(C.CYAN, "\n📝 Memulai registrasi...")
    browser, page = create_session(playwright, headless=headless)
    attach_api_logger(page, api_log, "register")

    jk_value = "P" if "perempuan" in (data.get("jenis_kel") or "").lower() else "L"
    jk_label  = "Perempuan" if jk_value == "P" else "Laki - laki"

    try:
        cprint(C.DIM, "  Membuka halaman register...")
        page.goto(f"{SPMB_URL}/register", wait_until="networkidle", timeout=90_000)
        page.wait_for_timeout(2000)
        page.screenshot(path=str(OUT_DIR / "01-register.png"), full_page=True)

        # Pilih jenjang SD
        page.locator("text=SD").first.click()
        page.wait_for_timeout(500)
        page.get_by_role("button", name="Lanjutkan").click()
        page.wait_for_timeout(2000)
        page.screenshot(path=str(OUT_DIR / "02-step2.png"), full_page=True)
        cprint(C.DIM, "  Jenjang SD dipilih, masuk langkah 2")

        # Isi form
        page.get_by_placeholder("Masukan Nama Lengkap").fill(data["nama"])
        page.get_by_placeholder("Masukan NIK").fill(data["nik"])
        nisn = data.get("nisn", "null")
        if nisn and nisn.lower() != "null":
            page.get_by_placeholder("Masukan NISN").fill(nisn)
        page.locator('input[type="password"]').nth(0).fill(data["pass"])
        page.locator('input[type="password"]').nth(1).fill(data["pass"])
        page.get_by_text(jk_label, exact=True).click()
        page.wait_for_timeout(1000)
        page.screenshot(path=str(OUT_DIR / "03-filled.png"), full_page=True)
        cprint(C.DIM, f"  Form diisi: {data['nama']} | NIK {data['nik']} | {jk_label}")

        page.get_by_role("button", name="Daftar").click()
        page.wait_for_timeout(8000)
        page.screenshot(path=str(OUT_DIR / "04-result.png"), full_page=True)

        toasts    = capture_toasts(page)
        reg_entry = next((e for e in api_log if e["endpoint"] == "akunRegistrasi"), None)

        (OUT_DIR / "api-log.json").write_text(
            json.dumps({
                "timestamp": datetime.now().isoformat(),
                "nik": data["nik"],
                "nama": data["nama"],
                "toasts": toasts,
                "entries": api_log,
            }, indent=2, ensure_ascii=False, default=str),
            encoding="utf-8"
        )

        print_result("HASIL REGISTRASI", reg_entry)

        if toasts:
            cprint(C.BLUE, "\n  Toast di halaman:")
            for t in set(toasts):
                cprint(C.BLUE, f"    ▸ {t}")

        cprint(C.DIM, "\n  Log        : spmb_output/api-log.json")
        cprint(C.DIM, "  Screenshots: spmb_output/01-register.png … 04-result.png")

        return reg_entry

    finally:
        browser.close()

# ─── Mode: AUDIT LENGKAP ─────────────────────────────────────────────────────
def run_audit(data: dict, playwright, headless=True):
    """
    Jalankan register-check + login-check lalu buat diagnosis status akun.

    Kenapa "NIK sudah terdaftar" bisa muncul padahal merasa belum daftar?
    ──────────────────────────────────────────────────────────────────────
    Operator sekolah asal (SD/bimba) biasanya menginput data siswa secara
    massal ke SPMB sebelum periode daftar dibuka. Artinya NIK sudah ada di
    database, tetapi password-nya dipegang operator — bukan password yang
    dibuat sendiri. Audit ini membantu membedakan kondisi tersebut.
    """
    banner("AUDIT AKUN SPMB — " + data["nik"])
    cprint(C.BOLD, f"  Nama  : {data['nama']}")
    cprint(C.BOLD, f"  NIK   : {data['nik']}")
    cprint(C.BOLD, f"  JK    : {data.get('jenis_kel', '-')}")

    # ── Langkah 1: Cek via form register ──────────────────────────────────
    cprint(C.CYAN, "\n=== [1/2] Cek status registrasi via form register ===")
    reg_log: list = []
    reg_entry = run_register(data, reg_log, playwright, headless=headless)

    reg_msg = ((reg_entry or {}).get("message") or "")
    nik_sudah_ada = any(
        x in reg_msg.lower() for x in ["sudah ada", "sudah terdaftar", "already"]
    )

    # ── Langkah 2: Cek login ──────────────────────────────────────────────
    cprint(C.CYAN, "\n=== [2/2] Cek login dengan NIK + password ===")
    login_log: list = []
    logged_in, login_entry = run_check_login(data, login_log, playwright, headless=headless)

    login_msg = ((login_entry or {}).get("message") or "")

    # ── Diagnosis ─────────────────────────────────────────────────────────
    banner("🩺 DIAGNOSIS AUDIT")

    # Tentukan skenario
    pw_wrong = any(x in login_msg.lower() for x in ["salah", "password", "sandi"])

    if nik_sudah_ada and logged_in:
        skenario = (C.GREEN,
            "✅ Akun AKTIF — NIK sudah terdaftar & login berhasil.",
            "Langsung buka https://spmb.bogorkab.go.id/login dan pilih jalur pendaftaran.")

    elif nik_sudah_ada and pw_wrong:
        skenario = (C.YELLOW,
            "⚠️  NIK sudah terdaftar TETAPI password salah.",
            ("→ Password yang Anda gunakan bukan password yang disetel operator sekolah.\n"
             "  Hubungi Operator Sekolah Asal/Tujuan untuk mendapatkan password SPMB.\n"
             "  JANGAN daftar ulang — NIK sudah ada di sistem."))

    elif nik_sudah_ada and not logged_in:
        skenario = (C.YELLOW,
            "⚠️  NIK sudah terdaftar TETAPI login ditolak.",
            ("→ Kemungkinan: akun dibuat operator sekolah dengan password berbeda,\n"
             "  atau akun belum diaktifkan. Hubungi Sekolah Asal/Tujuan.\n"
             "  Catatan: ini kasus umum — operator input massal sebelum periode daftar."))

    elif not nik_sudah_ada and logged_in:
        skenario = (C.GREEN,
            "✅ Login berhasil (NIK baru saja terdaftar atau respons register tidak terbaca).",
            "Silakan masuk ke portal SPMB dan lanjutkan pendaftaran.")

    else:
        # Belum terdaftar & login gagal
        if "recaptcha" in reg_msg.lower() or "captcha" in reg_msg.lower():
            detail = ("→ Registrasi gagal karena reCAPTCHA.\n"
                      "  Daftar manual di browser: https://spmb.bogorkab.go.id/register")
        elif reg_entry and (reg_entry.get("http_status") or 0) >= 500:
            detail = "→ Server SPMB sedang bermasalah. Coba lagi nanti."
        else:
            detail = ("→ Jika tadi tidak ada pesan error: akun mungkin baru dibuat,\n"
                      "  coba login manual di browser.\n"
                      "  Jika ada error: ulangi atau daftar manual.")
        skenario = (C.RED,
            "❌ NIK belum terdaftar di SPMB & login gagal.",
            detail)

    color, headline, detail_text = skenario
    cprint(color, f"  {headline}")
    print()
    for line in detail_text.split("\n"):
        print(f"  {line}")

    # ── Ringkasan teknis ───────────────────────────────────────────────────
    print()
    cprint(C.DIM, "  +- Ringkasan Teknis ----------------------------------------------")
    cprint(C.DIM, f"  |  NIK sudah ada di DB  : {'Ya' if nik_sudah_ada else 'Tidak / tidak terdeteksi'}")
    cprint(C.DIM, f"  |  Pesan registrasi     : {reg_msg or '(tidak ada)'}")
    cprint(C.DIM, f"  |  Login berhasil       : {'Ya' if logged_in else 'Tidak'}")
    cprint(C.DIM, f"  |  Pesan login          : {login_msg or '(tidak ada)'}")
    cprint(C.DIM, "  +----------------------------------------------------------------")

    # ── Simpan laporan audit ───────────────────────────────────────────────
    audit_report = {
        "timestamp": datetime.now().isoformat(),
        "nik": data["nik"],
        "nama": data["nama"],
        "nik_sudah_ada": nik_sudah_ada,
        "login_berhasil": logged_in,
        "pesan_registrasi": reg_msg,
        "pesan_login": login_msg,
        "register_log": reg_log,
        "login_log": login_log,
    }
    (OUT_DIR / "audit-report.json").write_text(
        json.dumps(audit_report, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8"
    )
    print()
    cprint(C.DIM, "  Laporan audit: spmb_output/audit-report.json")

# ─── Entry point ─────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        prog="spmb_bot.py",
        description="SPMB Kabupaten Bogor — Bot Registrasi & Login (Python)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh:
  python spmb_bot.py              → registrasi SD
  python spmb_bot.py --login      → cek login saja
  python spmb_bot.py --audit      → audit lengkap (DISARANKAN untuk diagnosis)
  python spmb_bot.py --audit --visible → jalankan dengan browser terbuka

Format .data (satu field per baris):
  nama:Nama Lengkap Siswa
  nik:3201xxxxxxxxxxxx
  nisn:null
  jenis_kel:perempuan
  pass:PasswordKuat123#
        """
    )
    parser.add_argument("--login", action="store_true", help="Cek login saja")
    parser.add_argument("--audit", action="store_true", help="Audit lengkap: register + login + diagnosis")
    parser.add_argument("--visible", action="store_true", help="Tampilkan browser (headless=False)")
    parser.add_argument("--data",  type=str, default=str(DATA_FILE), help=f"Path ke file .data (default: {DATA_FILE})")
    args = parser.parse_args()

    data_path = Path(args.data)
    data = parse_data(data_path)

    for field in ("nik", "pass"):
        if not data.get(field):
            cprint(C.RED, f"[ERROR] Field '{field}' wajib ada di {data_path}")
            sys.exit(1)

    if not USE_PYCRYPTODOME and not USE_CRYPTOGRAPHY:
        cprint(C.YELLOW, "[WARN] Library kriptografi tidak ditemukan — dekripsi respons dinonaktifkan.")
        cprint(C.YELLOW, "  Install: pip install pycryptodome")
        print()

    cprint(C.BOLD, f"\n  SPMB Bot Python — {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    cprint(C.DIM,  f"  Data   : {data_path}")
    cprint(C.DIM,  f"  Output : {OUT_DIR}")

    with sync_playwright() as pw:
        headless_mode = not args.visible
        if args.audit:
            run_audit(data, pw, headless=headless_mode)
        elif args.login:
            run_check_login(data, [], pw, headless=headless_mode)
        else:
            run_register(data, [], pw, headless=headless_mode)

if __name__ == "__main__":
    main()
