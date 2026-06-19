# GetContact Bot

Bot CLI berbasis PHP untuk mengecek **tag atau nama** yang disimpan pengguna GetContact pada nomor WhatsApp tertentu.

## Lokasi file

```
getcontact/script/bot.php
```

## Persyaratan

| Komponen | Versi |
|----------|-------|
| PHP | 7.4+ |
| Ekstensi | `curl`, `readline` |
| OS | Linux / macOS (`xdg-open`) |

## Cara menjalankan

```powershell
cd script-getcontact
php getcontact/script/bot.php
```

### Menu

| No | Fungsi |
|----|--------|
| 04 | Mulai bot — cek nomor |
| 00 | Keluar |

### Alur cek nomor

1. Key: `getcontact`
2. Nomor WA format `08xx...`
3. Verifikasi via WhatsApp (VerifyKit)
4. Tampil daftar tag/nama

## Sumber file

| File | Keterangan |
|------|------------|
| `getcontact/script/bot.php` | Versi clean, siap pakai |
| `decoder/bahan/bot.php` | Versi asli terenkripsi |

## Lihat juga

- [decoder.md](decoder.md)
- [ANALISIS.md](ANALISIS.md)
