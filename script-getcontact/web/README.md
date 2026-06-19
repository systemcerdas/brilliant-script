# GetContact Web

Versi web interaktif untuk cek **tag/nama** yang menyimpan nomor WhatsApp di GetContact.

Bagian dari [script-getcontact](../README.md) · [BrillianScript](../../README.md)

## Struktur

```
web/
├── app.py              # Flask server + API routes
├── getcontact.py       # Client API GetContact / VerifyKit
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

## Persyaratan

| Komponen | Versi |
|----------|-------|
| Python | 3.8+ |
| Paket | `flask`, `requests` |
| Koneksi | Internet aktif |

## Instalasi & menjalankan

```powershell
cd script-getcontact/web
python -m pip install -r requirements.txt
python app.py
```

Buka browser: **http://localhost:5050**

Port default `5050`. Ubah lewat environment variable:

```powershell
$env:PORT = "8080"
python app.py
```

## Cara pakai

1. **Nomor WhatsApp** — format Indonesia, harus ada angka `0` (contoh: `081234567890`)
2. Klik **Mulai Verifikasi**
3. Klik **Buka WhatsApp** → kirim pesan verifikasi sesuai instruksi
4. Tunggu hitung mundur 10 detik
5. Hasil tag/nama muncul otomatis di halaman

Jika verifikasi belum selesai, halaman akan cek ulang setiap 3 detik.

## API

| Endpoint | Method | Body | Response |
|----------|--------|------|----------|
| `/api/start` | POST | `{ "phone" }` | `{ "ok", "wa_link", "phone", "countdown" }` |
| `/api/check` | POST | `{}` | `{ "ok", "count", "tags" }` |

Session Flask menyimpan token antara langkah start dan check.

## Environment variables

| Variable | Default | Keterangan |
|----------|---------|------------|
| `PORT` | `5050` | Port server |
| `FLASK_SECRET` | random | Secret key session Flask |

## Troubleshooting

| Masalah | Solusi |
|---------|--------|
| `ModuleNotFoundError: flask` | Jalankan `python -m pip install -r requirements.txt` |
| Nomor tidak valid | Format `08xx...`, harus mengandung `0` |
| Verifikasi gagal | Pastikan pesan WA sudah dikirim sebelum hitung mundur habis |
| Sesi habis | Refresh halaman dan mulai ulang |
| Gagal token GetContact | Coba lagi — API GetContact mungkin sibuk |

## Perbedaan dengan CLI

| | Web | CLI (`../script/bot.php`) |
|---|-----|---------------------------|
| UI | Browser | Terminal |
| Runtime | Python + Flask | PHP |
| Verifikasi WA | Link diklik manual | `xdg-open` otomatis |
| OS | Windows / Linux / macOS | Linux / macOS |

## Catatan

- Bukan produk resmi GetContact.
- Nomor yang dicek harus bisa menerima verifikasi WhatsApp.
- Penggunaan otomatisasi dapat melanggar Terms of Service GetContact.

## Lihat juga

- [../README.md](../README.md) — overview script-getcontact
- [../docs/ANALISIS.md](../docs/ANALISIS.md) — analisis teknis bot asli
