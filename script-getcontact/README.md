# script-getcontact

Bot CLI PHP untuk cek tag/nama yang disimpan di GetContact, plus tool Python untuk reverse kode terenkripsi.

Berdasarkan [rusmanaid/getcontact](https://github.com/rusmanaid/getcontact) — hasil reverse oleh BrillianLabs.

## Struktur

```
script-getcontact/
├── decoder/
│   ├── script/decode_bot.py    # Tool decoder
│   ├── bahan/bot.php           # File terenkripsi (input)
│   └── output/                 # Hasil decode (gitignored, regeneratable)
├── getcontact/
│   └── script/bot.php          # Bot siap pakai
└── docs/
    ├── getcontact.md
    ├── decoder.md
    └── ANALISIS.md
```

## Quick start

```powershell
# Jalankan bot
php getcontact/script/bot.php

# Decode ulang dari file terenkripsi
python decoder/script/decode_bot.py
```

## Persyaratan

| Tool | Kebutuhan |
|------|-----------|
| Bot | PHP 7.4+, ekstensi `curl` & `readline` |
| Decoder | Python 3.8+, koneksi internet |

## Dokumentasi

- [docs/getcontact.md](docs/getcontact.md) — panduan bot
- [docs/decoder.md](docs/decoder.md) — panduan decoder
- [docs/ANALISIS.md](docs/ANALISIS.md) — analisis teknis obfuscation

## Catatan

- `decoder/bahan/bot.php` = versi asli terenkripsi.
- `getcontact/script/bot.php` = versi clean hasil reverse.
- Bukan produk resmi GetContact.

## Kredit

- Author asli: **Rusmana-ID** / [Inject-ID](https://youtube.com/@Inject1D)
