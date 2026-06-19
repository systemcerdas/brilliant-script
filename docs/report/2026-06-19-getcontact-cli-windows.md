# Laporan Perbaikan CLI Windows — script-getcontact

> Tanggal: 19 Juni 2026  
> Scope: `script-getcontact/script/bot.php`

---

## 1. Masalah

Saat menjalankan CLI di **Windows**, setelah input nomor WhatsApp muncul error:

```
'xdg-open' is not recognized as an internal or external command,
operable program or batch file.
```

Diikuti **Verifikasi! Gagal!** karena link WhatsApp tidak terbuka — user tidak bisa mengirim pesan verifikasi.

### Penyebab

| Aspek | Detail |
|-------|--------|
| Perintah asli | `system("xdg-open " . $wa)` |
| Platform | `xdg-open` hanya tersedia di Linux / desktop environment Unix |
| Windows | Tidak ada `xdg-open` — perintah setara: `start "" "url"` |
| Dampak | Link verifikasi VerifyKit tidak terbuka → verifikasi gagal setelah hitung mundur |

### Konteks alur verifikasi

1. User input nomor WA
2. Script POST ke VerifyKit → dapat `result.validation.link`
3. Link harus dibuka di WhatsApp → user **kirim pesan verifikasi manual**
4. Setelah hitung mundur 10 detik, script cek status via `/v3.0/check`
5. Jika pesan belum dikirim → **Verifikasi! Gagal!**

---

## 2. Perbaikan

### Fungsi baru di `bot.php`

**`clear_screen()`** — bersihkan terminal per OS:
- Windows → `cls`
- lainnya → `clear`

**`open_url($url)`** — buka URL di browser/app default:
- Windows → `start "" <url>`
- macOS → `open <url>`
- Linux → `xdg-open <url>`

Semua URL di-escape dengan `escapeshellarg()`.

### Perubahan lain

| Perubahan | Alasan |
|-----------|--------|
| Tampilkan link WA di terminal | Fallback copy-paste manual jika browser tidak terbuka |
| `trim()` pada input nomor | Hindari spasi berlebih (`0812...` vs `0     0812...`) |
| README: dukungan Windows | Dokumentasi platform |

### Cuplikan kode (setelah perbaikan)

```php
echo $c.$wa."\n\n";
open_url($wa);
echo $p."[".$h."•".$p."] Buka link di atas, kirim pesan WA, tunggu hitung mundur.\n\n";
```

---

## 3. Cara pakai di Windows

```powershell
cd script-getcontact
php script/bot.php
```

1. Pilih menu **04 — Mulai Bot**
2. Masukkan nomor (`0812xxxxxxxx`)
3. Link WA muncul di terminal + browser/WA Desktop terbuka
4. **Kirim pesan verifikasi** di WhatsApp sebelum hitung mundur habis
5. Jika browser tidak terbuka — copy link dari terminal, buka manual

---

## 4. Catatan

- Verifikasi **tidak otomatis** — user wajib kirim pesan WA sendiri
- Hitung mundur tetap **10 detik** (sama dengan versi asli & web)
- `bot_original.php` **belum** diupdate (arsip asli reverse)
- Versi web (`script-getcontact/web/`) tidak terpengaruh — sudah pakai tombol link di browser

---

## 5. Referensi

- [2026-06-19-session-riwayat.md](2026-06-19-session-riwayat.md) — riwayat session lengkap
- [2026-06-19-getcontact-keamanan.md](2026-06-19-getcontact-keamanan.md) — review keamanan
- `script-getcontact/README.md` — panduan CLI & web
