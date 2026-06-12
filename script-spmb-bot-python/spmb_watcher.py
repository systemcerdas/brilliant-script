"""
spmb_watcher.py — Bot Pengawas SPMB 24 Jam
============================================
Bot ini akan berjalan 24 jam nonstop di server untuk mengecek status akun
secara berkala sampai sekolah (tanpa sepengetahuan Anda) memperbaiki/membuka akun tersebut.
- Anti-ban: Interval acak (default 10 - 25 menit) agar terlihat natural.
- Stealth: Menggunakan playwright-stealth untuk memalsukan sidik jari browser.
- Otomatis Berhenti: Bot akan langsung berhenti dan menyimpan bukti jika LOGIN BERHASIL.

Persiapan di Server:
  pip install playwright-stealth
"""

import time
import random
import sys
import logging
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

# Menggunakan argumen native Playwright untuk anti-deteksi

# Import fungsi dari spmb_bot.py
try:
    from spmb_bot import parse_data, DATA_FILE, SPMB_URL, MOBILE_UA, interpret_spmb_body, suggest_action, capture_toasts
except ImportError:
    print("[ERROR] Pastikan spmb_bot.py berada di folder yang sama.")
    sys.exit(1)

# Setup Logger
log_file = Path("spmb_output/watcher.log")
log_file.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

def create_stealth_session(playwright):
    # Gunakan argumen browser anti-deteksi
    browser = playwright.chromium.launch(
        headless=True,
        args=[
            '--disable-blink-features=AutomationControlled',
            '--disable-infobars',
            '--window-size=390,844'
        ]
    )
    context = browser.new_context(
        viewport={"width": 390, "height": 844},
        user_agent=MOBILE_UA,
        locale="id-ID",
        timezone_id="Asia/Jakarta",
    )
    page = context.new_page()
    return browser, page

def do_stealth_login_check(data: dict, playwright) -> tuple:
    browser, page = create_stealth_session(playwright)
    api_log = []

    def on_response(res):
        url = res.url
        if "ppdb-service" not in url:
            return
        try:
            body = res.json()
        except:
            try: body = res.text()
            except: body = None

        interpreted = interpret_spmb_body(body)
        api_log.append({
            "endpoint": url.split("/")[-1],
            "http_status": res.status,
            "message": interpreted.get("message")
        })

    page.on("response", on_response)

    try:
        page.goto(f"{SPMB_URL}/login", wait_until="networkidle", timeout=90_000)
        page.wait_for_timeout(random.randint(2000, 4000))  # Jeda natural

        # Isi username pelan-pelan
        user_input = page.get_by_placeholder("username").or_(page.get_by_placeholder("NIK")).or_(page.get_by_placeholder("masukan"))
        if user_input.count() > 0:
            user_input.first.type(data["nik"], delay=random.randint(50, 150))
        else:
            page.locator("input:visible").first.type(data["nik"], delay=random.randint(50, 150))
        
        page.wait_for_timeout(random.randint(500, 1000))

        # Isi password pelan-pelan
        page.locator('input[type="password"]').first.type(data["pass"], delay=random.randint(50, 150))
        page.wait_for_timeout(random.randint(500, 1000))

        # Klik tombol login
        login_btn = page.get_by_role("button", name="Login").or_(page.get_by_role("button", name="Masuk"))
        login_btn.first.click()
        
        # Tunggu respons
        page.wait_for_timeout(8000)

        final_url = page.url
        logged_in = "/akun" in final_url and "/login" not in final_url
        token     = page.evaluate("() => localStorage.getItem('access_token')")
        
        auth_entry = next((e for e in reversed(api_log) if e["endpoint"] == "akunAutentikasi"), None)
        msg = auth_entry["message"] if auth_entry else "Tidak ada respons"

        if logged_in or token:
            # Ambil screenshot buat bukti kalau sukses
            page.screenshot(path=str(Path("spmb_output/SUCCESS_LOGIN.png")), full_page=True)

        return logged_in or bool(token), msg

    except Exception as e:
        return False, f"Error: {str(e)}"
    finally:
        browser.close()

def do_stealth_register_check(data: dict, playwright) -> tuple:
    browser, page = create_stealth_session(playwright)
    api_log = []

    def on_response(res):
        url = res.url
        if "ppdb-service" not in url:
            return
        try:
            body = res.json()
        except:
            try: body = res.text()
            except: body = None

        interpreted = interpret_spmb_body(body)
        api_log.append({
            "endpoint": url.split("/")[-1],
            "http_status": res.status,
            "message": interpreted.get("message")
        })

    page.on("response", on_response)

    jk_value = "P" if "perempuan" in (data.get("jenis_kel") or "").lower() else "L"
    jk_label  = "Perempuan" if jk_value == "P" else "Laki - laki"

    try:
        page.goto(f"{SPMB_URL}/register", wait_until="networkidle", timeout=90_000)
        page.wait_for_timeout(random.randint(2000, 4000))

        page.locator("text=SD").first.click()
        page.wait_for_timeout(random.randint(500, 1000))
        page.get_by_role("button", name="Lanjutkan").click()
        page.wait_for_timeout(random.randint(2000, 3000))

        page.get_by_placeholder("Masukan Nama Lengkap").type(data["nama"], delay=random.randint(50, 150))
        page.get_by_placeholder("Masukan NIK").type(data["nik"], delay=random.randint(50, 150))
        nisn = data.get("nisn", "null")
        if nisn and nisn.lower() != "null":
            page.get_by_placeholder("Masukan NISN").type(nisn, delay=random.randint(50, 150))
        page.locator('input[type="password"]').nth(0).type(data["pass"], delay=random.randint(50, 150))
        page.locator('input[type="password"]').nth(1).type(data["pass"], delay=random.randint(50, 150))
        
        page.get_by_text(jk_label, exact=True).click()
        page.wait_for_timeout(random.randint(500, 1500))

        page.get_by_role("button", name="Daftar").click()
        page.wait_for_timeout(8000)

        reg_entry = next((e for e in reversed(api_log) if e["endpoint"] == "akunRegistrasi"), None)
        msg = reg_entry["message"] if reg_entry else "Tidak ada respons"

        if "Success" in str(msg):
            page.screenshot(path=str(Path("spmb_output/SUCCESS_REGISTER.png")), full_page=True)
            return True, msg
        return False, msg

    except Exception as e:
        return False, f"Error: {str(e)}"
    finally:
        browser.close()

def main():
    data = parse_data(DATA_FILE)
    logging.info(f"=== SPMB Watcher Dimulai untuk NIK: {data['nik']} ===")
    logging.info("Bot akan berjalan terus-menerus. Tekan Ctrl+C untuk berhenti.")
    logging.info("Tipe: Stealth Mode, Interval: 10 - 25 Menit")

    check_count = 0

    with sync_playwright() as pw:
        while True:
            check_count += 1
            logging.info(f"[Cek ke-{check_count}] Menguji REGISTRASI terlebih dahulu...")
            
            try:
                reg_sukses, reg_pesan = do_stealth_register_check(data, pw)
                
                if reg_sukses:
                    logging.info("🎉🎉🎉 BINGO! REGISTRASI BERHASIL! 🎉🎉🎉")
                    logging.info("Sekolah sepertinya telah MENGHAPUS akun lama yang rusak!")
                    logging.info("Bot otomatis mendaftarkan ulang, dan NIK Anda sekarang berhasil terdaftar.")
                    logging.info("Silakan login sekarang juga di browser Anda.")
                    logging.info("Bukti screenshot: spmb_output/SUCCESS_REGISTER.png")
                    break
                else:
                    if "sudah ada" in str(reg_pesan).lower() or "already" in str(reg_pesan).lower():
                        logging.info("  ▸ Registrasi ditolak (Data sudah ada). Lanjut mengecek LOGIN...")
                        
                        time.sleep(random.uniform(5, 10)) # jeda sebelum login
                        log_sukses, log_pesan = do_stealth_login_check(data, pw)
                        
                        if log_sukses:
                            logging.info("🎉🎉🎉 BINGO! LOGIN BERHASIL! 🎉🎉🎉")
                            logging.info("Sekolah sepertinya sudah MERESET/MENGAKTIFKAN akun Anda!")
                            logging.info("Silakan login manual sekarang juga di browser Anda.")
                            logging.info("Bukti screenshot: spmb_output/SUCCESS_LOGIN.png")
                            break
                        else:
                            if "Password Salah" in str(log_pesan):
                                logging.info("  ❌ Login ditolak (Password Salah). Belum ada perubahan dari sekolah.")
                            else:
                                logging.info(f"  ❌ Login gagal: {log_pesan}")
                    else:
                        logging.warning(f"⚠️ Gagal registrasi dengan pesan aneh/error: {reg_pesan}")

            except Exception as e:
                logging.error(f"Terjadi kesalahan saat mengeksekusi bot: {e}")

            # Sleep natural (10 - 25 menit) untuk menghindari WAF / rate limit
            # Agar cepat untuk testing, Anda bisa kurangi ini
            sleep_minutes = random.uniform(10, 25) 
            logging.info(f"Zzz... Menunggu {sleep_minutes:.2f} menit sebelum cek berikutnya...\n")
            time.sleep(sleep_minutes * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[OK] Watcher dihentikan oleh pengguna.")
        sys.exit(0)
