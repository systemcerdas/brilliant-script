# Generator Laporan Bulanan — Lutfi Ihsan

Sistem otomatisasi generate **Laporan Bulanan Tenaga Teknis Implementasi Logika Sistem** dalam format Word (`.docx`) dari data Markdown, GitHub PR, dan weekly report.

Bagian dari [BrillianScript](../README.md).

---

## Struktur Folder

```
script-laporan-bulanan/
├── README.md
├── generator/                    # Script Python
│   ├── generate.py               # Entry point utama
│   ├── init_month.py             # Inisialisasi folder bulan baru
│   ├── weekly_to_docx.py         # Konversi weekly_report.md → .docx
│   ├── generate_detail_md.py     # Generate/enrich detail_github.md
│   ├── lib/
│   │   ├── config.py             # Path resolver & config loader
│   │   ├── docx_builder.py       # Builder Word document
│   │   ├── parser.py             # Parser MD & weekly report
│   │   ├── github.py             # Fetch PR dari GitHub CLI
│   │   └── ...
│   ├── config_template.json      # Template config.json baru
│   ├── modules.json              # Definisi modul BAB II
│   └── requirements.txt
├── template/
│   ├── laporan_template.docx     # Template Word utama
│   ├── weekly_report_template.docx
│   └── media/                    # Gambar dari template (auto-extract)
├── input/
│   └── YYYYMM/                   # Data per periode
├── output/
│   └── YYYYMM/                   # Hasil generate
└── archive/
```

---

## Prasyarat

```powershell
pip install -r generator/requirements.txt
gh auth login   # GitHub CLI untuk fetch PR
```

---

## Workflow Rutin

### 0. Bulan Baru

```powershell
# Buat folder & scaffold config untuk periode baru
python generator/init_month.py 202607 --from 202606
```

Hasilnya di `input/202607/`:

| File | Keterangan |
|------|------------|
| `config.json` | Bulan, tahun, date range GitHub, ringkasan BAB I/III |
| `weekly_report.md` | Logbook kegiatan (tabel Markdown 7 kolom) |
| `detail_github.md` | Detail kegiatan per modul (diisi manual / AI) |
| `kegiatan_tambahan.json` | Rapat & kegiatan non-GitHub (opsional) |
| `prs.json` | Auto-fetch dari `gh` saat generate |
| `prompts/` | Prompt AI untuk enrichment |

Edit `config.json`, sesuaikan bulan, tahun, date range, dan nama output.

---

### 1. Weekly Report → DOCX

```powershell
python generator/weekly_to_docx.py 202607
```

Membaca `input/202607/weekly_report.md` (tabel 7 kolom) dan menghasilkan `input/202607/weekly_report.docx`.

---

### 2. Detail GitHub MD

```powershell
# Generate skeleton dari weekly report
python generator/generate_detail_md.py 202607 --from-weekly

# Tambahkan prolog otomatis per sub-kegiatan
python generator/generate_detail_md.py 202607 --add-prolog

# Generate prompt untuk enrichment AI (Cursor/Copilot)
python generator/generate_detail_md.py 202607 --prompt
```

> Setelah `--prompt`, buka `input/202607/prompts/CURSOR_ENRICH_DETAIL.md` dan jalankan di AI editor untuk mengisi deskripsi teknis.

---

### 3. Generate Laporan Final

```powershell
python generator/generate.py 202607
# atau paksa fetch ulang PR dari GitHub:
python generator/generate.py 202607 --fetch-prs
```

**Note Sistem Generator**: 
- `Lampiran 1 (Weekly Report)` kini diambil murni dari *export* manual yang diletakkan di `input/YYYYMM/YYYYMM_Program dan Data Weekly Report.docx` (berformat *Landscape*).
- `generate.py` menggunakan pustaka `docxcompose` untuk merangkai `Dokumen Utama`, `Lampiran 1 (Manual)`, dan `Lampiran 2 (Code Diff)` menjadi satu *file* secara rapi tanpa merusak layout portrait/landscape.
- Code Diff JSON panjang di- *truncate* max 150 karakter/baris untuk mencegah *lag/freeze* pada Word.

Output: `output/202607/Laporan Bulanan_Lutfi Ihsan - Juli 2026.docx`

Buka di Word → klik kanan **Daftar Isi** → **Update Field** untuk sinkronkan nomor halaman.

---

## Format File Input

### `config.json`

```json
{
  "period": "202607",
  "bulan": "Juli",
  "bulan_up": "JULI",
  "tahun": 2026,
  "output_filename": "Laporan Bulanan_Lutfi Ihsan - Juli 2026.docx",
  "weekly_user_filter": "Lutfi",
  "github": {
    "repo": "setditjen-psdkp/api-sip",
    "author": "lutfiihsan",
    "author_display": "lutfiihsan (Lutfi Ihsan)",
    "date_ranges": ["2026-07-01..2026-07-10", "..."],
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

### `weekly_report.md`

Tabel 7 kolom Markdown:

```markdown
| Weekly Cat | Date Range | Date | Activity | Output | User | Related Doc |
|---|---|---|---|---|---|---|
| W1 | 1-5 Juli | 2 Juli | Implementasi ... | Modul X selesai | Lutfi | PR #123 |
```

### `detail_github.md`

```markdown
## 1. Judul Modul
Pada kegiatan ini Tenaga Teknis ...

### 1.1 Sub-kegiatan

**Prolog**
Konteks singkat sub-kegiatan.

**Deskripsi Pekerjaan**
Deskripsi teknis pekerjaan.

**Detail Perubahan**

**File yang Diubah:**
- app/Services/ContohService.php

**Perubahan Utama:**
- Menambahkan validasi input

**Manfaat:**
- Meningkatkan keakuratan data

**Dokumentasi**
- https://github.com/org/repo/pull/123
```

### `kegiatan_tambahan.json`

```json
[
  {
    "judul": "Rapat Koordinasi Tim",
    "deskripsi": "Rapat mingguan membahas progress sprint.",
    "docs": ["Notulensi tersedia di folder input"]
  }
]
```

---

## Struktur Laporan yang Dihasilkan

```
Cover
Daftar Isi          ← TOC auto Word field (update saat dibuka)
Kata Pengantar
BAB I  – Pendahuluan
BAB II – Pelaksanaan Kegiatan  ← dari detail_github.md + PR GitHub
BAB III – Penutup
LAMPIRAN (cover)
  Lampiran 1 – Weekly Report
  Lampiran 2 – Kode Sumber & PR List
```

**Footer**: Nomor halaman di setiap halaman (cover dokumen tidak bernomor).

---

## Marker Template

Template Word (`laporan_template.docx`) menggunakan marker teks:

| Marker | Fungsi |
|--------|--------|
| `{{ TOC }}` | Lokasi inject Daftar Isi (opsional, fallback ke sebelum Kata Pengantar) |
| `{{ BAB2 }}` | Lokasi inject konten BAB II |
| `{{ LAMPIRAN }}` | Lokasi inject isi lampiran (setelah halaman cover LAMPIRAN) |

---

## Tips

- Tekan **Ctrl+A → F9** di Word untuk update semua field sekaligus (TOC + nomor halaman)
- Gunakan `--fetch-prs` jika PR bulan ini belum di-cache di `prs.json`
- Gambar lampiran diambil otomatis dari `template/media/` (`image3.jpeg`, `image4.jpeg`, `image12.jpeg`)
