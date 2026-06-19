# script-decoder

Tool Python untuk decode file PHP yang di-obfuscate dengan **php-encryptor** (hex escape + enkripsi + `eval()`).

Bukan khusus GetContact — bisa dipakai untuk file PHP terenkripsi dengan pola yang sama.

## Struktur

```
script-decoder/
├── script/
│   └── decode_php.py     # Script utama
├── bahan/                # File input (.php terenkripsi)
│   └── getcontact/
│       └── bot.php       # Contoh: bot GetContact
└── output/               # Hasil decode (gitignored)
    └── getcontact/
        ├── decoded.php
        ├── hex_readable.php
        ├── payload.json
        ├── REPORT.md
        └── clean/
            └── decoded.php
```

## Quick start

```powershell
cd script-decoder

# Decode semua file di bahan/
python script/decode_php.py

# Decode file tertentu
python script/decode_php.py bahan/getcontact/bot.php
```

## Persyaratan

- Python 3.8+
- Koneksi internet (API `php-encryptor.vercel.app`)

## Cara kerja

1. Baca file PHP terenkripsi dari `bahan/`
2. Decode hex escape string
3. Ekstrak payload (`scriptId`, `data`, `iv`, `mac`)
4. POST ke API dekripsi
5. Simpan hasil ke `output/<nama-projek>/`

## Menambah bahan baru

```
bahan/
└── nama-projek/
    └── file.php
```

Jalankan decoder — output otomatis masuk ke `output/nama-projek/`.

## Output

| File | Isi |
|------|-----|
| `decoded.php` | Kode mentah dari API |
| `hex_readable.php` | Input dengan hex string terbaca |
| `payload.json` | Ringkasan payload enkripsi |
| `REPORT.md` | Laporan decode |
| `clean/decoded.php` | Versi rapih |

## Contoh: GetContact

Bahan contoh ada di `bahan/getcontact/bot.php`. Hasil decode di `output/getcontact/clean/decoded.php`.

Untuk bot siap pakai, lihat [script-getcontact](../script-getcontact/).
