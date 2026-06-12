# SPMB Bogor Kab — Bot Registrasi & Login (Python)

Versi Python dari [script-spmb-bot](../script-spmb-bot/README.md).  
Menggunakan **Playwright Python** + **pycryptodome** — tidak memerlukan Node.js.

Bagian dari [BrillianScript](../README.md) · repo: [BrillianLabs/BrillianScript](https://github.com/BrillianLabs/BrillianScript)

---

## Struktur

```
script-spmb-bot-python/
├── README.md
├── spmb_bot.py         # skrip utama (registrasi + login + audit)
├── setup_python.ps1    # installer dependensi (jalankan sekali)
├── .data.example       # template konfigurasi (di-commit)
├── .data               # data asli — gitignored
└── spmb_output/        # log JSON & screenshot — gitignored
```

---

## Setup

```powershell
cd script-spmb-bot-python

# 1. Install dependensi (sekali saja)
.\setup_python.ps1

# 2. Siapkan file data
copy .data.example .data
# Edit .data — isi NIK, nama, jenis kelamin, password
```

### Format `.data`

```
nama:Nama Lengkap Siswa
nik:3201xxxxxxxxxxxx
nisn:null
jenis_kel:perempuan
pass:PasswordKuat123#
```

| Field | Wajib | Keterangan |
|-------|-------|------------|
| `nama` | Ya | Sesuai dokumen |
| `nik` | Ya | 16 digit; dipakai sebagai username login |
| `nisn` | Tidak | `null` jika belum ada (wajar dari PAUD/bimba) |
| `jenis_kel` | Ya | `perempuan` atau `laki-laki` |
| `pass` | Ya | Min. 8 karakter, huruf besar/kecil, angka, simbol |

---

## Perintah

| Perintah | Fungsi |
|----------|--------|
| `python spmb_bot.py` | Registrasi SD |
| `python spmb_bot.py --login` | Cek login NIK + password |
| `python spmb_bot.py --audit` | **Audit lengkap** (register + login + diagnosis) |
| `python spmb_bot.py --audit --visible` | Sama seperti `--audit` namun **menampilkan browser/UI** |
| `python spmb_bot.py --data path\ke\.data` | Gunakan file data kustom |

### Alur yang disarankan

> **Gunakan `--audit` terlebih dahulu** untuk diagnosis otomatis sebelum mengambil tindakan.

```powershell
python spmb_bot.py --audit
```

Audit akan:
1. Mencoba registrasi → deteksi apakah NIK sudah ada di database
2. Mencoba login → verifikasi password
3. Cetak **diagnosis + saran tindakan** otomatis

---

## Output

| Mode | Log JSON | Screenshot |
|------|----------|------------|
| Registrasi | `spmb_output/api-log.json` | `01-register.png` … `04-result.png` |
| Login | `spmb_output/login-log.json` | `login-result.png` |
| Audit | `spmb_output/audit-report.json` | semua screenshot di atas |

### Contoh output audit

```
┌─────────────────────────────────┐
│  🩺 DIAGNOSIS AUDIT             │
└─────────────────────────────────┘

  ⚠️  NIK sudah terdaftar TETAPI password salah.

  → Password yang Anda gunakan bukan password yang disetel operator sekolah.
    Hubungi Operator Sekolah Asal/Tujuan untuk mendapatkan password SPMB.
    JANGAN daftar ulang — NIK sudah ada di sistem.

  ┌─ Ringkasan Teknis ──────────────────────────────────────────────
  │  NIK sudah ada di DB  : Ya
  │  Pesan registrasi     : Data diri sudah ada sebelumnya...
  │  Login berhasil       : Tidak
  │  Pesan login          : Maaf, Username/Password Salah...
  └────────────────────────────────────────────────────────────────
```

---

## Kenapa NIK "sudah terdaftar" padahal belum pernah daftar?

Operator sekolah asal (SD/bimba) **menginput data siswa secara massal** ke SPMB
sebelum periode pendaftaran dibuka. Artinya:

- NIK sudah ada di database SPMB
- Password dipegang operator, **bukan** password yang Anda buat sendiri
- Solusi: hubungi sekolah asal/tujuan untuk mendapatkan password

---

## Troubleshooting

| Gejala | Penyebab | Tindakan |
|--------|----------|----------|
| `ModuleNotFoundError: playwright` | Belum install | `pip install playwright && playwright install chromium` |
| `ModuleNotFoundError: Crypto` | pycryptodome tidak ada | `pip install pycryptodome` |
| *Data diri sudah ada* | NIK sudah di-booking/didaftarkan | Hubungi sekolah asal/tujuan minta reset akun |
| *Username/Password Salah* | Password beda / akun nge-bug | Jika gagal login padahal merasa benar: minta sekolah reset password |
| *Data tidak sesuai Dukcapil* | Salah input NIK/Nama | NIK dan Nama di-cek real-time ke Dukcapil, pastikan ketikan benar |
| reCAPTCHA error | Bot terdeteksi | Gunakan mode `--visible` atau daftar manual |
| Timeout / gagal buka halaman | Server SPMB lambat | Coba lagi nanti |

---

---

## Pemantauan Bot di VPS (Server)

Karena bot telah di-deploy menggunakan **Systemd Service** dan **Gunicorn**, Anda dapat mengecek status bot kapan saja dengan dua cara:

### 1. Melalui Web Dashboard
Buka browser di HP/PC Anda dan masukkan alamat:
👉 `http://<IP_VPS_ANDA>:8000` *(Contoh: http://43.134.108.19:8000)*

Dashboard ini akan otomatis merefresh setiap 30 detik untuk memberikan informasi log terbaru dan bukti BINGO jika berhasil.

### 2. Melalui SSH / Terminal VPS
Jika butuh melakukan restart atau mematikan bot, masuk ke VPS Anda dan gunakan perintah berikut:
- **Cek Status Bot**: `sudo systemctl status spmb_watcher`
- **Restart Bot**: `sudo systemctl restart spmb_watcher`
- **Mematikan Bot**: `sudo systemctl stop spmb_watcher`
- **Cek Log Real-time**: `journalctl -u spmb_watcher -f`

*(Ganti `spmb_watcher` menjadi `spmb_web` jika ingin memodifikasi service dashboard Gunicorn)*

---

## Keamanan

- Jangan commit `.data` atau `.cred` (sudah di `.gitignore`).
- File `spmb_output/` berisi screenshot yang mungkin memuat data pribadi — jaga kerahasiaannya.
- Hindari menyebar *IP Address* dan Port Dashboard Anda ke publik.
