# script-getcontact

Bot untuk cek **tag/nama** yang disimpan pengguna GetContact pada nomor WhatsApp.

Tersedia dua versi:
- **CLI** — `script/bot.php` (PHP)
- **Web** — `web/` (Flask) → [web/README.md](web/README.md)

Berdasarkan [rusmanaid/getcontact](https://github.com/rusmanaid/getcontact) — hasil reverse.

## Struktur

```
script-getcontact/
├── script/
│   ├── bot.php          # CLI bersih (tanpa access key)
│   └── bot_original.php # Salinan asli reverse (dengan key gate)
├── web/
│   ├── app.py           # Server Flask
│   ├── getcontact.py    # Logic API
│   ├── requirements.txt
│   ├── templates/
│   └── static/
└── docs/
    └── ANALISIS.md
```

## Quick start — Web (disarankan)

Dokumentasi lengkap: [web/README.md](web/README.md)

```powershell
cd script-getcontact/web
python -m pip install -r requirements.txt
python app.py
```

Buka http://localhost:5050

1. Masukkan nomor WA (`08xx...`)
2. Klik **Buka WhatsApp** → kirim pesan verifikasi
3. Tunggu hitung mundur → hasil tag muncul otomatis

## Quick start — CLI

```powershell
cd script-getcontact
php script/bot.php
```

Pilih menu **04 — Mulai Bot**, lalu masukkan nomor WA.

Butuh PHP 7.4+ dengan `curl` dan `readline`. Mendukung **Windows**, Linux, dan macOS.

Versi asli dengan access key marketing (`getcontact` / `bit.ly/getcontact-key`) ada di `script/bot_original.php`.

## Decode ulang

```powershell
cd script-decoder
python script/decode_php.py bahan/getcontact/bot.php
```

## Catatan

- Bukan produk resmi GetContact.
- Verifikasi WhatsApp wajib — nomor yang dicek harus bisa menerima pesan WA.
- Penggunaan otomatisasi dapat melanggar ToS GetContact.

## Kredit

- Author asli: **Rusmana-ID** / [Inject-ID](https://youtube.com/@Inject1D)
