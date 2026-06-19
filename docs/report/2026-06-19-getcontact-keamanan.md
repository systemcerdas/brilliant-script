# Laporan Keamanan — script-getcontact

> Tanggal review: 19 Juni 2026  
> Scope: `script-getcontact/` (web, CLI, arsip asli) + `script-decoder/bahan/getcontact/bot.php`

Dokumen ini menjawab apakah script GetContact di repo BrillianScript mengandung malware, serta risiko keamanan lain yang perlu diketahui sebelum dipakai.

---

## 1. Kesimpulan eksekutif

| Komponen | Malware? | Rekomendasi |
|----------|----------|-------------|
| `script-getcontact/web/` | **Tidak** | Versi paling aman & transparan — disarankan |
| `script-getcontact/script/bot.php` | **Tidak** | Aman dipakai lokal |
| `script-getcontact/script/bot_original.php` | **Tidak** | Arsip referensi; fungsional sama + key marketing |
| `script-decoder/bahan/getcontact/bot.php` | **Jangan jalankan** | File terenkripsi asli — risiko `eval()` + server eksternal |

**Tidak ditemukan** tanda malware klasik (keylogger, ransomware, botnet, eksfiltrasi data ke server mencurigakan) pada versi clean/web yang ada di repo.

**Yang berisiko** hanya file PHP **terenkripsi asli** — bukan karena malware tersembunyi, melainkan karena mekanisme `eval()` pada kode dari server pihak ketiga.

---

## 2. File yang direview

```
script-getcontact/
├── web/
│   ├── app.py
│   ├── getcontact.py
│   ├── static/app.js
│   └── templates/index.html
├── script/
│   ├── bot.php              # CLI bersih
│   └── bot_original.php     # Salinan asli reverse
└── docs/ANALISIS.md

script-decoder/
└── bahan/getcontact/bot.php # Input terenkripsi (jangan dijalankan)
```

Metode review: pembacaan manual source code, pencarian pola berbahaya (`eval`, `exec`, `system` selain UI, `base64_decode`, URL mencurigakan), dan perbandingan dengan hasil decode sebelumnya.

---

## 3. Versi web (`script-getcontact/web/`)

### Temuan

- **Network:** Hanya memanggil domain resmi alur GetContact:
  - `getcontact.com`
  - `widget.verifykit.com`
  - `gtc-manage-widget.verifykit.com` (header origin/referer)
- **Tidak ada:** `eval`, `exec`, `subprocess`, `os.system`, pickle, socket arbitrer, atau upload/download file
- **Frontend (`app.js`):** Hanya `fetch` ke `/api/start` dan `/api/check` di server lokal
- **Backend (`app.py`):** Menyimpan token sesi di Flask session cookie; tidak mengirim data ke server selain GetContact/VerifyKit

### Data yang dikirim keluar

| Data | Tujuan |
|------|--------|
| Nomor WhatsApp | VerifyKit (verifikasi) |
| Token sesi GetContact | getcontact.com |
| Hasil tag/nama | Hanya ditampilkan ke user (tidak di-forward ke server lain) |

### Catatan operasional

- `app.run(debug=True)` aktif saat development — **jangan expose ke internet publik** tanpa matikan debug dan gunakan reverse proxy + HTTPS
- Set `FLASK_SECRET` di production agar session cookie aman

**Verdict: aman dari malware.**

---

## 4. Versi CLI bersih (`script/bot.php`)

### Temuan

- Hasil decode yang sudah diaudit; tidak ada `eval()` atau remote code execution
- `curl` hanya ke `getcontact.com` dan `widget.verifykit.com`
- `system("clear")` — bersihkan terminal
- `system("xdg-open ...")` — buka browser ke link **promosi author** (bukan malware):

| URL | Fungsi |
|-----|--------|
| `t.me/config_geratis` | Grup Telegram author |
| `youtube.com/@Inject1D` | Channel YouTube |
| `tutorialinjectid.my.id` | Website author |
| `wa.me/6283879017166` | Chat admin |
| Link WhatsApp verifikasi | Dari response VerifyKit (dinamis) |

### Risiko non-malware

- `CURLOPT_SSL_VERIFYPEER = 0` — verifikasi sertifikat SSL dimatikan; rentan MITM pada jaringan tidak tepercaya
- Menu promosi author bisa mengganggu, tapi bukan eksploitasi

**Verdict: aman dari malware.**

---

## 5. Arsip asli (`script/bot_original.php`)

Isi fungsional sama dengan `bot.php` ditambah **access key marketing** (`getcontact` / `bit.ly/getcontact-key`).

Tidak ditemukan backdoor, kode tersembunyi, atau endpoint mencurigakan di luar yang sudah terdokumentasi di `docs/ANALISIS.md`.

**Verdict: aman dari malware; disimpan sebagai referensi historis.**

---

## 6. File terenkripsi asli — JANGAN dijalankan

**Lokasi:** `script-decoder/bahan/getcontact/bot.php`  
**Sumber:** [rusmanaid/getcontact](https://github.com/rusmanaid/getcontact)

### Mekanisme berbahaya

```
File terenkripsi
  → POST ke php-encryptor.vercel.app/api/run
  → eval(kode_php_dari_response)
```

| Risiko | Keterangan |
|--------|------------|
| Remote code execution | Server eksternal bisa mengubah kode yang di-`eval` kapan saja |
| Tidak bisa diaudit | Perilaku runtime bergantung response server |
| Bukan malware terkonfirmasi | Tapi **tidak bisa dijamin aman** tanpa decode & review manual |

**Gunakan hanya sebagai bahan input decoder.** Hasil decode sudah tersimpan di `script/bot.php`.

---

## 7. Perbandingan endpoint network

### Versi clean/web — hanya ini:

| URL | Metode | Fungsi |
|-----|--------|--------|
| `getcontact.com/id/manage` | GET | Ambil token sesi |
| `widget.verifykit.com/v3.0/start` | POST | Mulai verifikasi WA |
| `widget.verifykit.com/v3.0/check` | POST | Cek status verifikasi |
| `getcontact.com/validation-verifykit-check` | POST | Validasi session |
| `getcontact.com/id/manage/profile` | GET | Ambil daftar tag |

### Hanya di file terenkripsi (decoder):

| URL | Fungsi |
|-----|--------|
| `php-encryptor.vercel.app/api/run` | Dekripsi kode — **tidak dipanggil** oleh web/CLI clean |

**Tidak ada** komunikasi ke IP/domain mencurigakan di luar daftar di atas.

---

## 8. Risiko lain (bukan malware)

| Risiko | Detail |
|--------|--------|
| Privasi | Nomor WA dikirim ke GetContact & VerifyKit |
| ToS | Scraping/otomatisasi dapat melanggar Terms of Service GetContact |
| Ketidakstabilan | Bukan API resmi — bisa rusak jika GetContact mengubah halaman/API |
| Data pihak ketiga | Menampilkan tag yang diberikan pengguna lain pada nomor |
| SSL disabled (CLI) | `CURLOPT_SSL_VERIFYPEER = 0` pada bot PHP |

---

## 9. Rekomendasi penggunaan

1. **Pakai versi web** (`script-getcontact/web/`) — kode paling mudah diaudit
2. **Jangan jalankan** `script-decoder/bahan/getcontact/bot.php` langsung dengan PHP
3. **Jangan expose** Flask dev server ke internet publik
4. **Gunakan hanya di jaringan tepercaya** jika memakai CLI PHP (SSL verify off)
5. **Pahami implikasi privasi** — Anda mengirim nomor WA ke layanan pihak ketiga

---

## 10. Referensi

- Analisis teknis bot: `script-getcontact/docs/ANALISIS.md`
- Riwayat session & reverse engineering: [2026-06-19-session-riwayat.md](2026-06-19-session-riwayat.md)
- Panduan web: `script-getcontact/web/README.md`
- Repo sumber asli: https://github.com/rusmanaid/getcontact

---

*Review berdasarkan source code di repo BrillianScript per 19 Juni 2026. Tidak menggantikan audit keamanan profesional penuh.*
