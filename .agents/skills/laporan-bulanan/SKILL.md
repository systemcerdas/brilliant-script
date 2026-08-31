---
name: laporan-bulanan
description: >
  Skill untuk generate, mengelola, dan debug laporan bulanan Tenaga Teknis Implementasi Logika Sistem
  menggunakan script Python di script-laporan-bulanan/. Meliputi weekly report, detail GitHub,
  enrichment AI, dan generate dokumen Word final.
---

# Skill: Laporan Bulanan

Workspace root: `script-laporan-bulanan/`  
Semua command dijalankan dari folder tersebut kecuali dinyatakan lain.

---

## Lokasi Penting

| Path | Keterangan |
|------|------------|
| `generator/generate.py` | Entry point utama generate laporan Word |
| `generator/init_month.py` | Scaffold folder bulan baru |
| `generator/weekly_to_docx.py` | Konversi weekly_report.md → .docx |
| `generator/generate_detail_md.py` | Generate/enrich detail_github.md |
| `generator/lib/docx_builder.py` | Builder Word: TOC, BAB II, Lampiran, footer |
| `generator/lib/config.py` | Path resolver & config loader |
| `generator/lib/parser.py` | Parser weekly report & detail MD |
| `generator/lib/github.py` | Fetch PR dari GitHub CLI (`gh`) |
| `generator/config_template.json` | Template config.json bulan baru |
| `input/YYYYMM/` | Data input per periode |
| `output/YYYYMM/` | Hasil generate |
| `template/laporan_template.docx` | Template Word utama |
| `template/weekly_report_template.docx` | Template Word weekly report |
| `template/media/` | Gambar lampiran (auto-extract dari template) |
| `.agents/skills/laporan-bulanan/scripts/fetch_prs_to_weekly.py` | Auto-fetch raw PR ke weekly_report.md |
| `.agents/skills/laporan-bulanan/scripts/generate_detail_from_github.py` | Auto-generate detail_github.md dari PR GitHub |
| `.agents/skills/laporan-bulanan/resources/PROMPT_POLES_WEEKLY.md` | Prompt AI (Cursor) untuk merapikan weekly report |

---

## Workflow Lengkap Bulan Baru

### Step 0 – Init

```powershell
cd script-laporan-bulanan
python generator/init_month.py 202608 --from 202607
```

Edit `input/202608/config.json`: sesuaikan `bulan`, `bulan_up`, `tahun`, `date_ranges`, `output_filename`.

### Step 1 – Weekly Report

Tarik data PR terbaru (mentah) ke dalam tabel Markdown:

```powershell
python .agents/skills/laporan-bulanan/scripts/fetch_prs_to_weekly.py 202608
```

Gunakan **Prompt AI** (`.agents/skills/laporan-bulanan/resources/PROMPT_POLES_WEEKLY.md`) di dalam IDE Anda (Cursor/Copilot) untuk memoles/merapikan isi `activity` dan `output` pada `weekly_report.md` agar lebih mudah dibaca. Setelah tabelnya rapi, timpa/simpan kembali ke filenya.

Konversi ke DOCX:

```powershell
python generator/weekly_to_docx.py 202608
```

### Step 2 – Detail GitHub

Ada 2 cara yang dapat dilakukan:

**Cara A (Enrichment AI / Klasik):**
```powershell
# Skeleton dari weekly
python generator/generate_detail_md.py 202608 --from-weekly

# Tambah prolog per sub-kegiatan
python generator/generate_detail_md.py 202608 --add-prolog

# Generate prompt AI (untuk Cursor/Copilot)
python generator/generate_detail_md.py 202608 --prompt
```
Lalu buka `input/202608/prompts/CURSOR_ENRICH_DETAIL.md` dan enrich dengan AI.

**Cara B (Enrichment Otomatis via Script - Terbaru):**
Alih-alih menggunakan AI, script ini akan secara otomatis mengisi tag `<!-- ENRICH -->` pada `detail_github.md` dengan placeholder default berdasarkan konteks yang sudah ada. Sangat menghemat waktu!
```powershell
# Skeleton dari weekly
python generator/generate_detail_md.py 202608 --from-weekly

# Tambah prolog per sub-kegiatan
python generator/generate_detail_md.py 202608 --add-prolog

# Auto-enrich menggunakan script
python ../.agents/skills/laporan-bulanan/scripts/enrich_auto.py 202608
```
Setelah jalan, silakan periksa `detail_github.md` untuk merapikan sedikit jika diperlukan.

### Step 3 – Generate Laporan

```powershell
python generator/generate.py 202608
# Paksa fetch ulang PR:
python generator/generate.py 202608 --fetch-prs
```

**Note Sistem Generator**: 
- `Lampiran 1 (Weekly Report)` kini diambil murni dari *export* manual yang diletakkan di `input/YYYYMM/YYYYMM_Program dan Data Weekly Report.docx` (berformat *Landscape*).
- `generate.py` menggunakan pustaka `docxcompose` (dipadukan dengan *Section Break Next Page* kustom) untuk menggabungkan `Dokumen Utama`, `Lampiran 1 (Manual)`, dan `Lampiran 2 (Code Diff)` ke dalam satu *file* utuh tanpa merusak format halamannya (portrait/landscape).
- Code Diff JSON panjang di- *truncate* max 150 karakter/baris untuk mencegah *freeze* pada Microsoft Word.

Output: `output/202608/Laporan Bulanan_Lutfi Ihsan - Agustus 2026.docx`

Buka di Word -> **Ctrl+A -> F9** untuk update semua field (TOC + nomor halaman).

---

## Format File Input

### `config.json` — field wajib

```json
{
  "period": "202608",
  "bulan": "Agustus",
  "bulan_up": "AGUSTUS",
  "tahun": 2026,
  "output_filename": "Laporan Bulanan_Lutfi Ihsan - Agustus 2026.docx",
  "weekly_user_filter": "Lutfi",
  "github": {
    "repo": "setditjen-psdkp/api-sip",
    "author": "lutfiihsan",
    "author_display": "lutfiihsan (Lutfi Ihsan)",
    "date_ranges": ["2026-08-01..2026-08-10", "2026-08-11..2026-08-20", "2026-08-21..2026-08-31"],
    "fetch_if_missing": true,
    "fetch_always": false
  },
  "tech": {
    "language": "PHP v8.2",
    "framework": "Laravel 11",
    "repo_url": "https://github.com/setditjen-psdkp/api-sip"
  },
  "bab1": { "pencapaian": "...", "tantangan": "..." },
  "bab3": { "kesimpulan_items": ["..."] }
}
```

### `detail_github.md` — format section

```markdown
## 1. Judul Modul
Narasi intro modul.

### 1.1 Sub-kegiatan

**Prolog**
Konteks singkat.

**Deskripsi Pekerjaan**
Deskripsi teknis.

**Detail Perubahan**

**File yang Diubah:**
- path/file.php

**Perubahan Utama:**
- Poin teknis

**Manfaat:**
- Manfaat operasional

**Dokumentasi**
- https://github.com/org/repo/pull/NNN
```

### `kegiatan_tambahan.json` — opsional

```json
[
  {
    "judul": "Rapat Koordinasi",
    "deskripsi": "Deskripsi singkat.",
    "docs": ["-"]
  }
]
```

---

## Struktur Dokumen Output

```
Cover                           <- tidak bernomor halaman
Daftar Isi                      <- TOC Word field, update manual
Kata Pengantar
BAB I  - Pendahuluan
BAB II - Pelaksanaan Kegiatan   <- dari detail_github.md + kegiatan_tambahan.json + PR GitHub
BAB III - Penutup
LAMPIRAN (cover page)           <- halaman sendiri
  Lampiran 1 - Weekly Report
  Lampiran 2 - Kode Sumber & PR List
```

**Footer**: nomor halaman centered di setiap halaman (cover dokumen kosong via `different_first_page`).

---

## Marker Template Word

| Marker teks | Fungsi |
|-------------|--------|
| `{{ TOC }}` | Inject Daftar Isi (fallback: sebelum paragraf "Kata Pengantar") |
| `{{ BAB2 }}` | Inject konten BAB II |
| `{{ LAMPIRAN }}` | Inject isi lampiran (setelah cover LAMPIRAN) |

---

## Troubleshooting Umum

| Gejala | Penyebab | Fix |
|--------|----------|-----|
| `PermissionError` saat save | File .docx masih terbuka di Word | Tutup Word dulu |
| TOC tidak update | Field belum di-refresh | Ctrl+A -> F9 di Word |
| Nomor halaman `{ PAGE }` literal | Field belum di-render | Ctrl+A -> F9 |
| `FileNotFoundError: prs.json` | GitHub CLI belum login | `gh auth login` |
| PR tidak lengkap | Date range di config kurang | Periksa `date_ranges` di config.json |
| Blank page sebelum Daftar Isi | Paragraf kosong extra saat inject TOC | Lihat `build_report` di `docx_builder.py` |
| Cover lampiran & isi 1 halaman | Page break awal `build_lampiran` hilang | Pastikan ada `OxmlElement("w:br")` type page di awal `build_lampiran` |

---

## Gambar Lampiran

Diambil otomatis dari `template/media/`:

| File | Konten |
|------|--------|
| `image3.jpeg` | Screenshot GitHub PR list |
| `image4.jpeg` | Screenshot server development |
| `image12.jpeg` | Screenshot GitHub PR tambahan |

Ganti file di `template/media/` untuk update gambar tanpa ubah kode.
