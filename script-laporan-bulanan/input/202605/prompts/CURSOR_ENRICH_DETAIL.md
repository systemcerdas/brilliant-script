# Prompt Enrichment Detail Laporan — 202605

Gunakan file `detail_github.md` sebagai target edit.

## Tugas
Lengkapi setiap sub-kegiatan (`###`) yang masih berisi `<!-- ENRICH -->` atau prolog/deskripsi yang terlalu singkat.

## Format wajib per sub-kegiatan

```
### X.Y Judul Kegiatan

**Prolog**
[1-2 kalimat konteks: apa, modul apa, mengapa]

**Deskripsi Pekerjaan**
[Paragraf formal: Telah diimplementasikan/dilakukan...]

**Detail Perubahan**

**File yang Diubah:**
- `path/file.php`

**Perubahan Utama:**
- poin teknis spesifik

**Manfaat:**
- manfaat bisnis/operasional

**Dokumentasi**
- link PR
```

## Sumber data
1. Baca diff PR via `gh pr view <num> --repo setditjen-psdkp/api-sip`
2. Cross-check `weekly_report.md` dan `prs.json` di folder `input/202605/`
3. Ikuti gaya penulisan file referensi `input/202605/detail_github.md`

## Aturan penulisan
- Bahasa Indonesia formal (Tenaga Teknis Implementasi Logika Sistem)
- Prolog: konteks singkat sebelum deskripsi detail
- Hindari copy-paste judul PR mentah sebagai deskripsi
- Gabungkan PR terkait dalam satu sub-kegiatan jika satu aktivitas weekly

## File saat ini

```markdown
# DETAIL LAPORAN KEGIATAN GITHUB — LUTFI IHSAN
## Bulan Mei 2026 (Periode Weekly Report W1–W3)

Sumber data: `202605_Program dan Data Weekly Report.docx.md`  
Format acuan: `Contoh Format.docx`

---

## 1. Memperbaharui Webservice Modul WasRisk

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice Modul WasRisk, sebagai berikut:

### 1.1 Menambahkan notifikasi pengesahan dokumen hasil inspeksi by sistem

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan menambahkan notifikasi pengesahan dokumen hasil inspeksi by sistem sebagai bagian dari pembaruan modul WasRisk.


**Deskripsi Pekerjaan**

Telah diimplementasikan mekanisme pengesahan otomatis dokumen hasil inspeksi yang sudah terlewat lebih dari 1×24 jam. Sistem akan mengesahkan dokumen secara otomatis dan mengirimkan notifikasi kepada pengawas berisi kode verifikasi untuk penelusuran dokumen hasil inspeksi.

**Detail Perubahan**

**File yang Diubah:**
- `app/Console/Commands/ImportirPreborder/CekPengesahanDokumenPengesahan.php`
- `app/Jobs/PengawasanPerizinanBerusaha/NotifikasiSahkanDokumenPengawasan.php`
- `tests/Feature/Console/Commands/ImportirPreborder/CekPengesahanDokumenPengesahanTest.php`

**Perubahan Utama:**
- Penambahan job notifikasi pengesahan dokumen hasil pengawasan via WhatsApp dan email.
- Penyesuaian command `CekPengesahanDokumenPengesahan` untuk memicu proses pengesahan otomatis.
- Penambahan feature test untuk memvalidasi alur pengesahan otomatis.

**Manfaat:**
- Dokumen hasil inspeksi yang melewati batas waktu tetap dapat diproses tanpa intervensi manual.
- Pengawas mendapat notifikasi berisi kode verifikasi untuk penelusuran dokumen.
- Mengurangi backlog dokumen yang belum disahkan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5119

---

### 1.2 Memperbaharui logic unggah objek pengawasan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan memperbaharui logic unggah objek pengawasan sebagai bagian dari pembaruan modul WasRisk.


**Deskripsi Pekerjaan**

Telah dilakukan perbaikan pada proses import objek pengawasan via Excel, khususnya pada validasi field NIB agar lebih toleran terhadap perbedaan format data (spasi, tipe data).

**Detail Perubahan**

**File yang Diubah:**
- `app/Imports/ObjekPengawasanImport.php`

**Perubahan Utama:**
- Penambahan trimming pada nilai NIB sebelum validasi.
- Penggunaan loose comparison (`==`) untuk pencocokan NIB, mengakomodasi perbedaan tipe data string/integer dari file Excel.

**Manfaat:**
- Mengurangi kegagalan import akibat format NIB yang tidak konsisten.
- Meningkatkan keberhasilan proses unggah objek pengawasan massal via Excel.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/commit/8eec29921f39b881ca6cd730093c43a35bf1600a

---

### 1.3 Memperbaharui logic dashboard WasRisk

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan memperbaharui logic dashboard WasRisk sebagai bagian dari pembaruan modul WasRisk.


**Deskripsi Pekerjaan**

Telah dilakukan perbaikan pada dashboard WasRisk untuk menampilkan jumlah objek pengawasan, realisasi pengawasan, dan monitoring inspeksi manual dengan akurat, termasuk perbaikan akses operator pusat dan perhitungan input manual.

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/DashboardPerizinanBerusahaService.php`
- `tests/Feature/PengawasanPerizinanBerusaha/DashboardMonitoringSistemManualTest.php`

**Perubahan Utama:**
- Perbaikan agar operator pusat dapat melihat seluruh data realisasi pengawasan (PR #5122).
- Perbaikan perhitungan dashboard input manual pada monitoring inspeksi (PR #5125).
- Penambahan feature test komprehensif untuk validasi dashboard monitoring sistem manual.

**Manfaat:**
- Dashboard menampilkan data realisasi pengawasan yang akurat untuk semua level operator.
- Monitoring inspeksi manual berjalan konsisten antara data sistem dan input manual.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5122
- https://github.com/setditjen-psdkp/api-sip/pull/5125

---

### 1.4 Memperbaharui logic notifikasi pengesahan dokumen hasil inspeksi (per objek)

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan memperbaharui logic notifikasi pengesahan dokumen hasil inspeksi (per objek) sebagai bagian dari pembaruan modul WasRisk.


**Deskripsi Pekerjaan**

Telah diperbaiki logika pengiriman notifikasi pengesahan dokumen agar dikirim per objek pengawasan (perusahaan), bukan per dokumen BAP. Sebelumnya, jika satu perusahaan memiliki banyak dokumen BAP, notifikasi terkirim berulang kali.

**Detail Perubahan**

**File yang Diubah:**
- `app/Console/Commands/ImportirPreborder/CekPengesahanDokumenPengesahan.php`

**Perubahan Utama:**
- Pengelompokan objek pengawasan unik sebelum proses generate dokumen dan notifikasi.
- Notifikasi WhatsApp dan email dikirim sekali per objek pengawasan, bukan per BAP.
- Generate dokumen hasil pengawasan dipicu per objek pengawasan.

**Manfaat:**
- Pengawas tidak menerima notifikasi berulang untuk perusahaan yang sama.
- Kode verifikasi penelusuran tetap relevan per objek pengawasan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5129

---

### 1.5 Memperbaharui logic penjadwalan pengawas

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan memperbaharui logic penjadwalan pengawas sebagai bagian dari pembaruan modul WasRisk.


**Deskripsi Pekerjaan**

Telah ditambahkan validasi backend pada proses penjadwalan agar pengawas yang dipilih tidak boleh berasal dari UPT yang berbeda dengan objek pengawasan, kecuali memiliki role Operator Pusat WasRisk.

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/PenjadwalanService.php`

**Perubahan Utama:**
- Validasi setiap pegawai (pengawas) yang dipilih saat `pilihJadwal`.
- Pengecekan kesesuaian `unit_kerja` pegawai dengan UPT objek pengawasan.
- Pengecualian untuk role `Operator Pusat WasRisk`.
- Rollback transaksi database jika validasi gagal.

**Manfaat:**
- Mencegah penugasan pengawas dari UPT yang tidak sesuai wilayah kerja.
- Menjaga integritas data penjadwalan pengawasan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5134

---

### 1.6 Memperbaharui logic simpan pertanyaan inspeksi WasRisk

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan memperbaharui logic simpan pertanyaan inspeksi WasRisk sebagai bagian dari pembaruan modul WasRisk.


**Deskripsi Pekerjaan**

Telah dilakukan hotfix pada proses penyimpanan pertanyaan inspeksi dan Berita Acara Pemeriksaan (BAP), termasuk validasi jawaban wajib, perbaikan relasi model, dan penanganan error saat generate dokumen PDF.

**Detail Perubahan**

**File yang Diubah:**
- `app/Models/PengawasanPerizinanBerusaha/InspeksiLapangan/PertanyaanKepatuhanTeknis.php`
- `app/Services/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanPbUmkuService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanSelfDeclareService.php`
- `tests/Feature/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanServiceTest.php`
- `tests/Feature/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisServiceTest.php`

**Perubahan Utama:**
- Penambahan validasi jawaban wajib sebelum menyelesaikan BAP Tab 3 (kepatuhan-teknis, self-declare, pbumku).
- Penambahan relasi `subPertanyaan()` sebagai alias `child()` pada model `PertanyaanKepatuhanTeknis`.
- Penambahan `return` setelah `DB::rollBack()` saat response API gagal, mencegah crash `Undefined property: stdClass::$data`.
- Penyesuaian tipe parameter `$urutan` menjadi nullable (`?int`) untuk pertanyaan bertipe penjelasan.
- Penambahan feature test (9 passed, 10 assertions).

**Manfaat:**
- Mencegah BAP diselesaikan tanpa j
...
```
