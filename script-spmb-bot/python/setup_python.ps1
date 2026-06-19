# setup_python.ps1 — Install dependensi Python untuk spmb_bot.py
# Jalankan SEKALI sebelum pertama kali pakai: .\setup_python.ps1

$ErrorActionPreference = 'Stop'

Write-Host "`n=== Setup SPMB Bot Python ===" -ForegroundColor Cyan

# Cek Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "[ERROR] Python tidak ditemukan." -ForegroundColor Red
    Write-Host "  Install dari: https://python.org (centang 'Add to PATH')" -ForegroundColor Yellow
    exit 1
}

$pyVersion = python --version
Write-Host "  Python : $pyVersion" -ForegroundColor Green

# Install dependensi pip
Write-Host "`n[1/2] Menginstall playwright + pycryptodome..." -ForegroundColor Yellow
pip install playwright pycryptodome --quiet

# Install browser Chromium
Write-Host "[2/2] Menginstall Chromium (hanya sekali, ~150 MB)..." -ForegroundColor Yellow
playwright install chromium

Write-Host "`n[OK] Setup selesai!" -ForegroundColor Green
Write-Host ""
Write-Host "Cara pakai:" -ForegroundColor Cyan
Write-Host "  python spmb_bot.py               -> Registrasi SD"
Write-Host "  python spmb_bot.py --login       -> Cek login"
Write-Host "  python spmb_bot.py --audit       -> Audit lengkap (DISARANKAN)"
Write-Host ""
Write-Host "Jangan lupa salin .data.example ke .data dan isi data asli." -ForegroundColor Yellow
