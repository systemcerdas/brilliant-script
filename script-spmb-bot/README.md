# SPMB Bogor Kab — Registrasi Otomatis

Skrip Playwright untuk registrasi akun SD di [SPMB Kabupaten Bogor](https://spmb.bogorkab.go.id/register), dengan dekripsi respons API agar pesan error server tampil jelas (bukan hanya *"Terjadi kesalahan pada sistem"*).

Bagian dari [BrillianScript](../README.md).

## Struktur

```
script-spmb-bot/
├── README.md
├── spmb_register.mjs
├── package.json
├── .data.example
├── .curl.example
├── .data              # lokal, gitignored
├── .curl              # lokal, gitignored
└── spmb_output/       # gitignored
```

## Setup

```powershell
cd script-spmb-bot
copy .data.example .data
# Edit .data — isi nama, NIK, jenis kelamin, password

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

| Field | Wajib | Keterangan |
|-------|-------|------------|
| `nama` | Ya | Sesuai dokumen |
| `nik` | Ya | 16 digit |
| `nisn` | Tidak | Kosongkan `null` jika belum ada (umum dari PAUD/bimba) |
| `jenis_kel` | Ya | `perempuan` atau `laki-laki` |
| `pass` | Ya | Min. 8 karakter, huruf besar/kecil, angka, simbol |

## Menjalankan

```powershell
npm run spmb
```

Log: `spmb_output/api-log.json` · Screenshot: `spmb_output/01-register.png` … `04-result.png`

## Catatan

- Jangan commit `.data` / `.curl`.
- `.curl.example` hanya referensi format DevTools; gunakan skrip Playwright, bukan replay curl.
