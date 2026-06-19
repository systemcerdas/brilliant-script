# Laporan

Dokumentasi laporan dari project BrillianScript.

| File | Isi |
|------|-----|
| [2026-06-19-session-riwayat.md](2026-06-19-session-riwayat.md) | Kronologi session: clone, decode, migrasi, web UI, SPMB reorg |
| [2026-06-19-getcontact-keamanan.md](2026-06-19-getcontact-keamanan.md) | Review keamanan script-getcontact — apakah ada malware |

## Ringkasan

### Session riwayat (19 Juni 2026)

1. Clone & reverse engineer [rusmanaid/getcontact](https://github.com/rusmanaid/getcontact)
2. Tool decoder Python (`script-decoder`) + bot clean (`script-getcontact`)
3. Migrasi ke repo [BrillianScript](https://github.com/BrillianLabs/BrillianScript)
4. Versi web interaktif Flask (`script-getcontact/web/`)
5. Reorganisasi `script-spmb-bot` → subfolder `javascript/` & `python/`
6. Hapus access key marketing (web + CLI); asli di `bot_original.php`
7. Fix bug token: `accessToken` dari `Set-Cookie`, bukan HTML body

### Keamanan GetContact

- Versi **web** dan **CLI bersih** — tidak mengandung malware
- File **terenkripsi asli** di `script-decoder/bahan/` — jangan dijalankan (`eval` + server eksternal)
- Detail lengkap → [2026-06-19-getcontact-keamanan.md](2026-06-19-getcontact-keamanan.md)
