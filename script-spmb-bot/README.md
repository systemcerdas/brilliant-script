# SPMB Bogor Kab — Bot Registrasi & Login

Skrip Playwright untuk [SPMB Kabupaten Bogor](https://spmb.bogorkab.go.id): registrasi akun SD dan cek login. Respons API didekripsi sehingga pesan server asli tampil jelas (bukan hanya *"Terjadi kesalahan pada sistem"*).

Bagian dari [BrillianScript](../README.md) · repo: [BrillianLabs/BrillianScript](https://github.com/BrillianLabs/BrillianScript)

## Struktur

```
script-spmb-bot/
├── README.md
├── spmb_register.mjs   # skrip utama
├── run.ps1             # wrapper (disarankan di Google Drive)
├── package.json
├── .data.example       # template (commit)
├── .curl.example       # contoh DevTools (commit)
├── .data               # data asli — gitignored
├── .curl               # capture curl — gitignored
└── spmb_output/        # log & screenshot — gitignored
```

## Setup

```powershell
cd script-spmb-bot
copy .data.example .data
# Edit .data — isi NIK, nama, jenis kelamin, password
```

**Instalasi Playwright** (pilih salah satu):

```powershell
# A — Disarankan jika project di Google Drive
.\run.ps1 --check-login          # otomatis npm install di %TEMP%

# B — Folder lokal (bukan Google Drive sync)
npm install
npx playwright install chromium
```

### Format `.data`

```
nama:Nama Lengkap Siswa
nik:3201xxxxxxxxxxxx
nisn:null
jenis_kel:perempuan
pass:PasswordKuat123#
```

| Field | Wajib registrasi | Keterangan |
|-------|------------------|------------|
| `nama` | Ya | Sesuai dokumen |
| `nik` | Ya | 16 digit; dipakai juga sebagai username login |
| `nisn` | Tidak | `null` jika belum ada (wajar dari PAUD/bimba) |
| `jenis_kel` | Ya | `perempuan` atau `laki-laki` |
| `pass` | Ya | Min. 8 karakter, huruf besar/kecil, angka, simbol |

## Perintah

| Perintah | Fungsi |
|----------|--------|
| `.\run.ps1` | Registrasi SD (via folder `%TEMP%`) |
| `.\run.ps1 --check-login` | Cek login NIK + password |
| `npm run spmb:run` | Sama seperti `run.ps1` |
| `npm run spmb` | Registrasi langsung (`node spmb_register.mjs`) |
| `npm run spmb:login` | Cek login langsung |

> **Google Drive:** `node_modules` sering corrupt (`ERR_INVALID_PACKAGE_CONFIG`). **Selalu pakai `run.ps1`** atau `npm run spmb:run`.

### Alur disarankan

1. **Cek login dulu** — apakah sekolah sudah buatkan akun:
   ```powershell
   .\run.ps1 --check-login
   ```
2. Jika login gagal *"Username/Password Salah"* → minta password ke **operator bimba/sekolah tujuan**.
3. Jika registrasi gagal *"Data diri sudah ada"* → **jangan daftar ulang**; hubungi sekolah untuk akun.
4. Registrasi mandiri hanya jika NIK **belum** ada di sistem:
   ```powershell
   .\run.ps1
   ```

## Output

| Mode | Log JSON | Screenshot |
|------|----------|------------|
| Registrasi | `spmb_output/api-log.json` | `01-register.png` … `04-result.png` |
| Login | `spmb_output/login-log.json` | `login-result.png` |

Contoh output login:

```
Pesan server  : Maaf, Username/Password Salah.! silahkan registrasi atau hubungi sekolah Asal atau Sekolah Tujuan.
Login OK      : tidak
```

Contoh output registrasi (NIK sudah terdaftar):

```
Pesan server  : Data diri sudah ada sebelumnya, silahkan hubungi Sekolah Asal atau Sekolah Tujuan untuk mendapatkan akun.
```

## Troubleshooting

| Gejala | Penyebab | Tindakan |
|--------|----------|----------|
| `ERR_INVALID_PACKAGE_CONFIG` | `node_modules` rusak di Google Drive | Pakai `.\run.ps1` |
| *Data diri sudah ada* | NIK sudah diinput operator sekolah | Hubungi sekolah asal/tujuan |
| *Username/Password Salah* | Password bukan dari SPMB / belum diaktifkan | Minta reset ke operator sekolah |
| NISN kosong | Normal untuk PAUD/bimba | Bukan penyebab gagal registrasi |

## Keamanan

- Jangan commit `.data` / `.curl` (sudah di `.gitignore`).
- `.curl.example` hanya referensi format DevTools; payload terenkripsi tidak bisa dipakai ulang.
