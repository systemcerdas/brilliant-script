from spmb_watcher import send_bingo_email
import logging

logging.basicConfig(level=logging.INFO)

print("Menguji pengiriman email...")
try:
    send_bingo_email(
        subject="TEST BINGO: Email Alert SPMB",
        text_body="Ini adalah email test untuk memastikan SMTP berjalan lancar.",
        img_path="spmb_output/01-register.png"  # Menggunakan screenshot yang sudah ada
    )
    print("Test selesai.")
except Exception as e:
    print(f"Error test email: {e}")
