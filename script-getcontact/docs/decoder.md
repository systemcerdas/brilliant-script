# PHP Decoder

Tool Python untuk mendekripsi kode tersembunyi di `decoder/bahan/bot.php`.

## Lokasi

```
decoder/script/decode_bot.py    ← jalankan
decoder/bahan/bot.php         ← input
decoder/output/               ← output (regeneratable)
```

## Cara menjalankan

```powershell
cd script-getcontact
python decoder/script/decode_bot.py
```

Hasil:
- `decoder/output/` — file mentah & clean
- `getcontact/script/bot.php` — bot diperbarui otomatis
- `docs/ANALISIS.md` — laporan analisis

## Persyaratan

Python 3.8+, koneksi internet (API `php-encryptor.vercel.app`).

## Update bahan

Ganti `decoder/bahan/bot.php`, lalu jalankan ulang decoder.

## Lihat juga

- [getcontact.md](getcontact.md)
- [ANALISIS.md](ANALISIS.md)
