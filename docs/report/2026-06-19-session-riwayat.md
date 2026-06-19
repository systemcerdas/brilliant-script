# Riwayat Session — 19 Juni 2026

Laporan lengkap pekerjaan dari session Cursor: reverse engineering GetContact bot, migrasi ke BrillianScript, pembuatan web UI, dan reorganisasi SPMB bot.

---

## 1. Clone repositori GetContact

**Permintaan:** Clone https://github.com/rusmanaid/getcontact

**Tindakan:**
- Clone ke `C:\Users\DATA-PSDKP\Documents\Brilliant-Data\getcontact`
- Isi awal: `bot.php` (terenkripsi, ~77 KB), `README.md`

**Sumber:** [rusmanaid/getcontact](https://github.com/rusmanaid/getcontact)

---

## 2. Decode / reverse `bot.php`

**Permintaan:** Reverse atau decode kode, hasil ke folder result, pakai Python.

**Temuan obfuscation (3 lapisan):**

| Lapisan | Teknik |
|---------|--------|
| 1 | Hex escape string (`\x4f\x70...`) |
| 2 | Noise code — fungsi acak (`_vcgehlul` = concat, `_dnmxhumc` = API call) |
| 3 | Enkripsi + POST ke `php-encryptor.vercel.app/api/run` + `eval()` |

**Tool:** `decode_bot.py` (Python 3, stdlib + urllib)

**Alur decode:**
1. Decode hex string
2. Ekstrak payload: `scriptId`, `data`, `iv`, `mac`
3. POST ke API dekripsi
4. Simpan kode PHP hasil decode

**Payload yang diekstrak:**

| Field | Nilai |
|-------|-------|
| scriptId | `3a83c2af4875e6da00d2cd7bbaac0b47` |
| iv | `b0626b462ac26c0d4d23adb68cbc3546` |
| mac | `0688539cd67b07a612377d9933c5fd312bf82e3d07a42567ce8aaa426c1bbe45` |
| data | ~18.200 karakter (base64 terenkripsi) |

**Fungsi bot setelah decode:**
- CLI PHP cek tag/nama GetContact untuk nomor WhatsApp
- Verifikasi via VerifyKit + WhatsApp
- Scrape `getcontact.com/id/manage/profile` → parse `<div class="pt-text">`
- Author asli: Rusmana-ID / Inject-ID

---

## 3. Struktur folder hasil decode (getcontact repo lokal)

```
getcontact/
├── decoder/
│   ├── script/decode_bot.py
│   ├── bahan/bot.php
│   └── output/          # regeneratable
├── getcontact/
│   └── script/bot.php   # clean, siap pakai
├── docs/
│   ├── getcontact.md
│   ├── decoder.md
│   └── ANALISIS.md
└── README.md
```

**Folder `output/clean/`** — versi rapih tanpa kata "deobfuscated" di nama file.

---

## 4. README & dokumentasi awal

Dibuat:
- `README.md` (root getcontact)
- `docs/getcontact.md` — panduan bot
- `docs/decoder.md` — panduan decoder
- `docs/ANALISIS.md` — analisis teknis lengkap

---

## 5. Migrasi ke BrillianScript

**Permintaan:** Pindah ke `brilliant-script`, rapihkan, push.

**Target repo:** [BrillianLabs/BrillianScript](https://github.com/BrillianLabs/BrillianScript)

**Struktur awal migrasi:**
```
script-getcontact/   # berisi decoder + bot (belum dipisah)
```

**Commit:** `feat(getcontact): add bot CLI and PHP decoder tool`

**Masalah saat push:** `desktop.ini` di `.git/refs/` — dibersihkan, lalu pull rebase + push berhasil.

---

## 6. Pisah decoder & getcontact

**Permintaan:** Decoder sendiri, getcontact sendiri — decoder tidak khusus getcontact saja.

**Struktur final:**

```
script-decoder/
├── script/decode_php.py    # generic, terima bahan/**/*.php
├── bahan/getcontact/bot.php
└── output/getcontact/      # gitignored

script-getcontact/
├── script/bot.php          # CLI clean
└── docs/ANALISIS.md
```

**Commit:** `refactor: split script-decoder and script-getcontact`

**Decoder generic:**
```powershell
python script/decode_php.py                    # semua di bahan/
python script/decode_php.py bahan/getcontact/bot.php
```

---

## 7. Reorganisasi SPMB bot

**Permintaan:** `script-spmb-bot` dibuat subfolder versi Python & JavaScript; perbaiki gitignore.

**Struktur:**

```
script-spmb-bot/
├── README.md
├── .gitignore
├── javascript/     # ex script-spmb-bot (Node + Playwright)
└── python/         # ex script-spmb-bot-python
```

**Perbaikan gitignore:**
- `.cred` dan `.curl` dihapus dari tracking git (sebelumnya ter-commit di python)
- Path diupdate: `script-spmb-bot/javascript/...`, `script-spmb-bot/python/...`
- Folder `script-spmb-bot-python/` dihapus (digabung)

**Commit:** `refactor(spmb-bot): split into javascript and python subfolders`

**deploy_vps.py** diupdate ke path `script-spmb-bot/python/`.

---

## 8. Versi web interaktif GetContact

**Permintaan:** Buat versi web interaktif di `script-getcontact`.

**Stack:** Flask + requests + HTML/CSS/JS

```
script-getcontact/web/
├── app.py
├── getcontact.py       # port logic dari bot.php
├── requirements.txt
├── templates/index.html
├── static/style.css
├── static/app.js
└── README.md
```

**Alur web:**
1. Input nomor WA
2. `POST /api/start` → link verifikasi WhatsApp
3. Hitung mundur 10 detik + polling
4. `POST /api/check` → tampilkan daftar tag

**Menjalankan:**
```powershell
cd script-getcontact/web
python -m pip install -r requirements.txt
python app.py
# http://localhost:5050
```

---

## 9. Access key dihapus (web & CLI)

**Konteks:** Key `getcontact` di bot asli hanya gimmick marketing (hardcoded, bukan API GetContact). Link promosi: `bit.ly/getcontact-key`.

**Tindakan — Web:**
- Hapus field Access Key dari UI web
- Hapus pengecekan `GETCONTACT_KEY` di `app.py`
- Update README web & utama

**Tindakan — CLI:**
- `script/bot.php` — versi bersih, langsung ke input nomor WA setelah menu 04
- `script/bot_original.php` — salinan asli hasil reverse (key gate tetap ada)

**Autentikasi nyata:** verifikasi WhatsApp via VerifyKit.

---

## 10. Perbaikan bug token GetContact (web)

**Gejala:** Error `Gagal mengambil token dari GetContact.` saat submit nomor di web UI.

**Penyebab:** `accessToken` dikirim GetContact lewat header `Set-Cookie`, bukan di HTML body. PHP CLI tetap jalan karena memakai `CURLOPT_HEADER=1` (header ikut dibaca). Python `requests` hanya mem-parse `res.text`.

**Perbaikan di `web/getcontact.py`:**
- Ambil `accessToken` dari `res.cookies` terlebih dahulu
- Fallback parse dari response headers jika cookie kosong
- Tambah `allow_redirects=True` agar mengikuti redirect seperti PHP

**Verifikasi:** `fetch_session_tokens()` berhasil mengambil `accessToken`, `token`, dan `hash` dari live API.

---

## 11. Endpoint yang dipakai bot

| URL | Fungsi |
|-----|--------|
| `https://php-encryptor.vercel.app/api/run` | Dekripsi kode terenkripsi (decoder saja) |
| `https://getcontact.com/id/manage` | Ambil accessToken, token, hash |
| `https://widget.verifykit.com/v3.0/start` | Mulai verifikasi WA |
| `https://widget.verifykit.com/v3.0/check` | Cek status verifikasi |
| `https://getcontact.com/validation-verifykit-check` | Validasi session |
| `https://getcontact.com/id/manage/profile` | Scrape daftar tag |

---

## 12. Commits ke BrillianScript (session ini)

| Commit | Pesan |
|--------|-------|
| `f2416f9` | `feat(getcontact): add bot CLI and PHP decoder tool` |
| `0559f64` | `refactor: split script-decoder and script-getcontact` |
| `14511c0` | `refactor(spmb-bot): split into javascript and python subfolders` |
| `9ca353c` | `feat(getcontact): add web UI, clean CLI, and session report` |

---

## 13. Peta repo saat ini (BrillianScript)

```
brilliant-script/
├── docs/report/              ← laporan ini
├── script-decoder/
├── script-getcontact/
│   ├── script/
│   │   ├── bot.php           # CLI bersih
│   │   └── bot_original.php  # asli dengan key gate
│   ├── web/
│   └── docs/ANALISIS.md
├── script-spmb-bot/
│   ├── javascript/
│   └── python/
├── script-laporan-bulanan/
└── README.md
```

---

## 14. Catatan keamanan & legal

- Bot **bukan** produk resmi GetContact
- File asli memakai `eval()` + server eksternal — gunakan `script/bot.php` clean atau versi web
- Scraping/otomatisasi dapat melanggar ToS GetContact
- Jangan commit: `.cred`, `.curl`, `.data` (sudah di-gitignore)

---

## 15. Referensi

- Repo sumber: https://github.com/rusmanaid/getcontact
- Repo tujuan: https://github.com/BrillianLabs/BrillianScript
- Analisis teknis bot: `script-getcontact/docs/ANALISIS.md`
- Panduan web: `script-getcontact/web/README.md`
