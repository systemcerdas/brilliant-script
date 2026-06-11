# Generator Laporan Bulanan — Lutfi Ihsan

Sistem generate laporan bulanan Tenaga Teknis Implementasi Logika Sistem.

## Struktur Folder

```
Laporan Bulanan/
├── README.md
├── generator/              # Script Python
│   ├── generate.py         # Laporan Word final
│   ├── generate_detail_md.py
│   ├── weekly_to_docx.py
│   ├── init_month.py
│   └── lib/
├── template/               # Template Word + screenshot
│   ├── laporan_template.docx
│   ├── contoh_format.docx
│   ├── weekly_report_template.docx
│   └── media/
├── input/YYYYMM/           # Bahan per bulan
├── output/YYYYMM/          # Hasil laporan final
└── archive/                # File asli (nama lama) — jangan dihapus
    ├── originals/          # Salinan file sebelum reorganisasi
    └── data/               # Data pendukung lama
```

**Root hanya berisi folder + README.** Semua bahan aktif ada di subfolder.
**File original** disimpan di `archive/originals/` — tidak dihapus saat merapikan.

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
cd "i:\My Drive\2026\Dokumen\Laporan Bulanan"

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
