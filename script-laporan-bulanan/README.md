# Generator Laporan Bulanan — Lutfi Ihsan

Sistem generate laporan bulanan Tenaga Teknis Implementasi Logika Sistem.

## Struktur Folder

```
script-laporan-bulanan/
├── README.md
├── generator/
├── template/
├── input/YYYYMM/
├── output/YYYYMM/
└── archive/
```

**Semua path relatif dari folder `script-laporan-bulanan/`.**

Bagian dari [BrillianScript](../README.md).

## Prasyarat

```powershell
pip install -r generator/requirements.txt
gh auth login
```

## Bulan Baru (contoh Juni 2026)

```powershell
python generator/init_month.py 202606 --from 202605
```

Isi di `input/202606/`:

| File | Keterangan |
|------|------------|
| `config.json` | Bulan, tahun, date range GitHub, ringkasan BAB I/III |
| `weekly_report.md` | Logbook Timja Program dan Data |
| `weekly_report.docx` | Versi Word (opsional, dari script) |
| `detail_github.md` | Detail kegiatan per modul |
| `detail_github.txt` | Versi plain-text detail |
| `detail_laporan.docx` | Lampiran detail Word (opsional) |
| `prs.json` | Auto-fetch dari `gh` jika kosong |
| `kegiatan_tambahan.json` | Rapat & kegiatan non-GitHub (opsional) |
| `prompts/` | Prompt Cursor untuk enrichment AI |

## Workflow Rutin

```powershell
cd script-laporan-bulanan

# 1. Weekly report → DOCX
python generator/weekly_to_docx.py 202605

# 2. Detail MD + TXT dari weekly
python generator/generate_detail_md.py 202605 --from-weekly
python generator/generate_detail_md.py 202605 --add-prolog
python generator/generate_detail_md.py 202605 --prompt   # → input/202605/prompts/

# 3. Laporan Word final
python generator/generate.py 202605
python generator/generate.py 202605 --fetch-prs   # paksa fetch ulang PR
```

Buka output di Word, lalu **Update Field** pada Daftar Isi.

## Contoh Mei 2026 (siap)

```powershell
python generator/generate.py 202605
```

Output: `output/202605/Laporan Bulanan_Lutfi Ihsan - Mei 2026.docx`

## Format detail_github.md

```markdown
## 1. Judul Modul
Pada kegiatan ini Tenaga Teknis...

### 1.1 Sub-kegiatan

**Prolog**
Konteks singkat sub-kegiatan...

**Deskripsi Pekerjaan**
...

**Detail Perubahan**

**File yang Diubah:**
- path/file.php

**Perubahan Utama:**
- poin teknis

**Manfaat:**
- manfaat operasional

**Dokumentasi**
- https://github.com/.../pull/XXXX
```
ianLabs/spmb-tools](https://github.com/BrillianLabs/spmb-tools) — branch **`spmb`**
- Branch **`master`** (jika ada) berisi proyek lain; gunakan **`spmb`** untuk tooling ini.
- Jangan commit `.data` / `.curl` — sudah di `.gitignore`.
ommit `.data` / `.curl` — sudah di `.gitignore`.
h di `.gitignore`.
