# script-getcontact

Bot CLI PHP untuk cek **tag/nama** yang disimpan pengguna GetContact pada nomor WhatsApp.

Berdasarkan [rusmanaid/getcontact](https://github.com/rusmanaid/getcontact) — hasil reverse. File terenkripsi asli ada di [script-decoder/bahan/getcontact](../script-decoder/bahan/getcontact/).

## Struktur

```
script-getcontact/
├── script/
│   └── bot.php       # Bot siap pakai
└── docs/
    └── ANALISIS.md   # Analisis teknis
```

## Quick start

```powershell
cd script-getcontact
php script/bot.php
```

## Persyaratan

| Komponen | Versi |
|----------|-------|
| PHP | 7.4+ |
| Ekstensi | `curl`, `readline` |
| OS | Linux / macOS (`xdg-open`) |

## Cara pakai

1. Jalankan `php script/bot.php`
2. Pilih menu **04** — Mulai bot
3. Key: `getcontact`
4. Input nomor WA format `08xx...`
5. Verifikasi via WhatsApp
6. Lihat daftar tag/nama

## Decode ulang dari file terenkripsi

Gunakan tool decoder terpisah:

```powershell
cd script-decoder
python script/decode_php.py bahan/getcontact/bot.php
# hasil: output/getcontact/clean/decoded.php
```

Salin ke `script-getcontact/script/bot.php` jika perlu update.

## Catatan

- Bukan produk resmi GetContact.
- Penggunaan scraping dapat melanggar ToS layanan.

## Kredit

- Author asli: **Rusmana-ID** / [Inject-ID](https://youtube.com/@Inject1D)
