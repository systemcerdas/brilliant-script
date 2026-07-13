# DETAIL LAPORAN KEGIATAN GITHUB — LUTFI IHSAN
## Bulan Juni 2026 (Periode Weekly Report)

Sumber data: `input/202606/weekly_report.md`
Format acuan: `template/contoh_format.docx`

> **Catatan:** Bagian `<!-- ENRICH -->` perlu dilengkapi via Cursor AI.
> Jalankan: `python generator/generate_detail_md.py {period} --prompt`

---

## 1. Memperbaharui Webservice Modul WasRisk

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice WasRisk, sebagai berikut:

### 1.1 Memperbaharui migration portal dokumen category

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui migration portal dokumen category sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi pengecekan flag_type exists sebelum drop column pada migration portal dokumen.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaharui migration portal dokumen category. Implementasi pengecekan flag_type exists sebelum drop column pada migration portal dokumen

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Userman/Database/Migrations/2026_02_15_192703_create_portal_dokumen_category_table.php`

**Perubahan Utama:**
- PR #5277: Fix: Check if flag_type exists before dropping in migration (+5/-3 baris).

**Manfaat:**
- Mencegah kegagalan migrasi database pada saat proses deployment. Dengan pengecekan eksistensi kolom sebelum drop, proses migrasi menjadi idempoten dan aman dijalankan berulang kali tanpa risiko error di lingkungan production.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5277

---

### 1.2 Memperbaharui notifikasi email operator pusat pemantauan SDK

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui notifikasi email operator pusat pemantauan SDK sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi perbaikan agar operator pusat menerima email notifikasi pemantauan SDK.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaharui notifikasi email operator pusat pemantauan sdk. Implementasi perbaikan agar operator pusat menerima email notifikasi pemantauan SDK

**Detail Perubahan**

**File yang Diubah:**
- `Modules/PengawasanPerizinanBerusaha/Services/SDK/PemantauanService.php`

**Perubahan Utama:**
- PR #5278: fix: operator pusat belum menerima email (+2/-2 baris).
- PR #5279: fix: operator pusat belum menerima email (+2/-2 baris).

**Manfaat:**
- Memastikan operator pusat menerima notifikasi email secara tepat waktu terkait kegiatan pemantauan SDK, sehingga tidak ada laporan yang terlewat dan pengawasan dapat berjalan lebih responsif.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5278
- https://github.com/setditjen-psdkp/api-sip/pull/5279

---

### 1.3 Memperbaharui webservice inspeksi dan export master data

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice inspeksi dan export master data sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi perbaikan InspeksiService dan PemantauanService pada fitur inspeksi dan export master data.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaharui webservice inspeksi dan export master data. Implementasi perbaikan InspeksiService dan PemantauanService pada fitur inspeksi dan export master data

**Detail Perubahan**

**File yang Diubah:**
- `Modules/PengawasanPerizinanBerusaha/Services/SDK/InspeksiService.php`
- `Modules/PengawasanPerizinanBerusaha/Services/SDK/PemantauanService.php`

**Perubahan Utama:**
- PR #5280: Fitur/master data: fix inspeksi dan export (+6/-5 baris).
- PR #5281: Fitur/master data: fix export and inspeksi (+6/-5 baris).

**Manfaat:**
- Meningkatkan keandalan fitur inspeksi lapangan dan ekspor data master, sehingga petugas dapat melakukan pemeriksaan dan mengunduh data secara akurat tanpa hambatan teknis.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5280
- https://github.com/setditjen-psdkp/api-sip/pull/5281

---

### 1.4 Memperbaharui transformer PemantauanDetailResource SDK

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui transformer PemantauanDetailResource SDK sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi penanggung_jawab dan operator sebagai empty array (bukan null), update resource pemantauan detail SDK.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaharui transformer pemantauandetailresource sdk. Implementasi penanggung_jawab dan operator sebagai empty array (bukan null), update resource pemantauan detail SDK

**Detail Perubahan**

**File yang Diubah:**
- `Modules/PengawasanPerizinanBerusaha/Transformers/SDK/PemantauanDetailResource.php`
- `Modules/PengawasanPerizinanBerusaha/Services/SDK/InspeksiService.php`
- `Modules/PengawasanPerizinanBerusaha/Services/SDK/PemantauanService.php`

**Perubahan Utama:**
- PR #5282: Update PemantauanDetailResource: set penanggung_jawab and operator to… (+17/-23 baris).
- PR #5283: Fitur/master data (+25/-30 baris).
- PR #5285: fix: return empty array for penanggung_jawab instead of null to preve… (+3/-3 baris).
- PR #5286: fix: return empty array for penanggung_jawab instead of null to preve… (+3/-3 baris).

**Manfaat:**
- Mencegah error null pointer exception pada sisi frontend ketika data penanggung jawab atau operator belum tersedia, sehingga tampilan detail pemantauan SDK lebih stabil dan tidak crash.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5282
- https://github.com/setditjen-psdkp/api-sip/pull/5283
- https://github.com/setditjen-psdkp/api-sip/pull/5285
- https://github.com/setditjen-psdkp/api-sip/pull/5286

---

### 1.5 Memperbaharui pesan error upload PDF corrupt pada inspeksi lapangan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui pesan error upload PDF corrupt pada inspeksi lapangan sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi pesan error spesifik saat upload PDF corrupt pada dokumentasi inspeksi lapangan.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaharui pesan error upload pdf corrupt pada inspeksi lapangan. Implementasi pesan error spesifik saat upload PDF corrupt pada dokumentasi inspeksi lapangan

**Detail Perubahan**

**File yang Diubah:**
- `app/Http/Requests/PengawasanPerizinanBerusaha/InspeksiLapangan/UploadDokumentasiInspeksiLapanganRequest.php`

**Perubahan Utama:**
- PR #5288: fix: specific error message for corrupt PDF on upload (+12/-0 baris).

**Manfaat:**
- Memberikan umpan balik yang jelas kepada petugas lapangan saat mengunggah dokumen PDF yang rusak, sehingga masalah dapat diidentifikasi dan diselesaikan lebih cepat tanpa perlu menghubungi tim teknis.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5288

---

### 1.6 UAT Asta Data PSDKP Cilacap

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan uAT Asta Data PSDKP Cilacap sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Penyelesaian issue UAT Asta Data PSDKP Cilacap.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait uat asta data psdkp cilacap. Penyelesaian issue UAT Asta Data PSDKP Cilacap

**Detail Perubahan**

**Perubahan Utama:**
- Pengujian dan verifikasi fungsionalitas sistem Asta Data PSDKP Cilacap sesuai skenario UAT yang telah ditetapkan oleh tim pengguna lapangan.

**Manfaat:**
- Memastikan sistem PSDKP Cilacap berjalan sesuai kebutuhan operasional lapangan melalui serangkaian pengujian penerimaan pengguna, sehingga kualitas layanan kepada unit kerja terjaga.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/issues/5276

---

### 1.7 Backport hotfix production ke master (WasRisk/BAP)

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan backport hotfix production ke master (WasRisk/BAP) sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi backport hotfix TypeError urutan, lock timeout, dan perbaikan BAP dari production ke master.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait backport hotfix production ke master (wasrisk/bap). Implementasi backport hotfix TypeError urutan, lock timeout, dan perbaikan BAP dari production ke master

**Detail Perubahan**

**File yang Diubah:**
- `app/Console/Commands/ImportirPreborder/CekPengesahanDokumenPengesahan.php`
- `app/Http/Resources/PengawasanPerizinanBerusaha/InspeksiLapangan/InspeksiLapanganResource.php`
- `app/Services/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanPbUmkuService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanSelfDeclareService.php`
- `tests/Feature/Command/CekPengesahanDokumenTest.php`
- `tests/Unit/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanServiceTest.php`
- `tests/Unit/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisServiceTest.php`
- `tests/Unit/PengawasanPerizinanBerusaha/PertanyaanPbUmkuServiceTest.php`
- `tests/Unit/PengawasanPerizinanBerusaha/PertanyaanSelfDeclareServiceTest.php`
- `docs/report/2026-06-10_fix-typeerror-urutan-backport-production-to-master.md`

**Perubahan Utama:**
- PR #5289: fix: backport hotfixes from production to master (TypeError  + lock timeout fixes) (+1836/-184 baris).
- PR #5290: docs: tambah laporan riwayat fix TypeError urutan dan backport hotfix… (+140/-0 baris).

**Manfaat:**
- Menjaga konsistensi kualitas kode antara branch production dan master, sehingga perbaikan kritis seperti TypeError dan lock timeout tidak terulang pada siklus pengembangan berikutnya.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5289
- https://github.com/setditjen-psdkp/api-sip/pull/5290

---

### 1.8 Perbaikan validasi Tab 3 BAP dan predikat kepatuhan teknis

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem perbaikan validasi Tab 3 BAP dan predikat kepatuhan teknis sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi perbaikan bug validasi Tab 3 BAP, parent rollup kepatuhan teknis, dan backport hotfix kepatuhan teknis.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait perbaikan validasi tab 3 bap dan predikat kepatuhan teknis. Implementasi perbaikan bug validasi Tab 3 BAP, parent rollup kepatuhan teknis, dan backport hotfix kepatuhan teknis

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisService.php`
- `tests/Unit/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanServiceTest.php`
- `docs/report/2026-06-10_fix-bap-validation-and-kepatuhan-teknis-bugs.md`

**Perubahan Utama:**
- PR #5291: Fix: Perbaikan Bug Validasi Tab 3 BAP dan Keterangan Predikat Kepatuhan (+67/-7 baris).
- PR #5292: fix: resolve parent rollup bug and add docs (+94/-0 baris).
- PR #5293: fix: resolve leftover merge conflict markers in tests (+0/-3 baris).
- PR #5294: hotfix: backport kepatuhan teknis and BAP validation bug fixes (+142/-7 baris).

**Manfaat:**
- Memastikan proses pengisian dan penilaian Berita Acara Pemeriksaan (BAP) berjalan secara valid dan akurat, sehingga hasil predikat kepatuhan teknis yang dihasilkan dapat dipercaya sebagai dasar pengambilan keputusan pengawasan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5291
- https://github.com/setditjen-psdkp/api-sip/pull/5292
- https://github.com/setditjen-psdkp/api-sip/pull/5293
- https://github.com/setditjen-psdkp/api-sip/pull/5294

---

### 1.9 Memperbaiki indikator laporan berkala dan log inspeksi SDK

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki indikator laporan berkala dan log inspeksi SDK sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi penyesuaian indikator rentang tahun laporan berkala, penonaktifan data dummy, dan penyembunyian log inspeksi null pada modul SDK.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaiki indikator laporan berkala dan log inspeksi sdk. Implementasi penyesuaian indikator rentang tahun laporan berkala, penonaktifan data dummy, dan penyembunyian log inspeksi null pada modul SDK

**Detail Perubahan**

**File yang Diubah:**
- `Modules/PengawasanPerizinanBerusaha/Transformers/SDK/PemantauanResource.php`
- `docs/report/2026-06-11_fix-indikator-tahun-laporan-berkala.md`
- `Modules/PengawasanPerizinanBerusaha/Transformers/SDK/PemantauanDetailResource.php`
- `docs/report/2026-06-11_chore-penonaktifan-dummy-log-inspeksi.md`
- `docs/report/2026-06-11_fix-log-inspeksi-menjadi-null.md`

**Perubahan Utama:**
- PR #5296: Fix: Penyesuaian Indikator Rentang Tahun Laporan Berkala di SDK (+82/-1 baris).
- PR #5297: Chore: Penonaktifan Data Dummy Log Inspeksi SDK (+127/-55 baris).
- PR #5298: Fix: Menyembunyikan Log Inspeksi dengan Null di SDK (+72/-113 baris).

**Manfaat:**
- Meningkatkan akurasi tampilan indikator laporan berkala SDK dan membersihkan data dummy yang tidak relevan, sehingga operator memperoleh informasi yang bersih dan terpercaya untuk kegiatan monitoring.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5296
- https://github.com/setditjen-psdkp/api-sip/pull/5297
- https://github.com/setditjen-psdkp/api-sip/pull/5298

---

### 1.10 Memperbaiki sorting objek pengawasan dan alias Vuetify

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki sorting objek pengawasan dan alias Vuetify sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi perbaikan sorting kolom provinsi/kabupaten pada objek pengawasan dan alias sorting .name dari UI Vuetify.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaiki sorting objek pengawasan dan alias vuetify. Implementasi perbaikan sorting kolom provinsi/kabupaten pada objek pengawasan dan alias sorting .name dari UI Vuetify

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/ObjekPengawasanService.php`
- `docs/report/2026-06-11_fix-5021-sort-provinsi-kabupaten.md`
- `tests/Unit/PengawasanPerizinanBerusaha/ObjekPengawasanServiceTest.php`

**Perubahan Utama:**
- PR #5300: Fix: Perbaikan Sorting Kolom Provinsi dan Kabupaten/Kota di Objek Pengawasan (+59/-2 baris).
- PR #5302: Fix: Tambahan Alias Sorting .name dari UI Vuetify (#5021) (+66/-8 baris).

**Manfaat:**
- Mempermudah petugas dalam menemukan data objek pengawasan melalui pengurutan kolom provinsi dan kabupaten/kota yang kini berfungsi dengan benar, meningkatkan efisiensi operasional pengelolaan data.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5300
- https://github.com/setditjen-psdkp/api-sip/pull/5302

---

### 1.11 Release update production from stage

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan release update production from stage sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi rilis pembaruan branch production dari stage.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait release update production from stage. Implementasi rilis pembaruan branch production dari stage

**Detail Perubahan**

**File yang Diubah:**
- `.agents/instructions/rules/coding_standards.md`
- `.agents/instructions/rules/reporting.md`
- `.agents/skills/ai_assistant/SKILL.md`
- `.gitignore`
- `.phpstorm.meta.php`
- `.rnd`
- `Modules/DashboardPimpinan/Database/Seeders/DashboardPimpinanDatabaseSeeder.php`
- `Modules/DashboardPimpinan/Database/Seeders/DashboardPimpinanPermissionSeeder.php`
- `Modules/DashboardPimpinan/Exports/KeragaanExport.php`
- `Modules/DashboardPimpinan/Exports/KeragaanKapalExport.php`
- `Modules/DashboardPimpinan/Http/Controllers/DashboardPimpinanController.php`
- `Modules/DashboardPimpinan/Http/Controllers/KeragaanPSDKPController.php`
- `Modules/DashboardPimpinan/Http/Controllers/OperasiArmadaController.php`
- `Modules/DashboardPimpinan/Http/Controllers/PengawasanSdkpController.php`
- `Modules/DashboardPimpinan/Http/Controllers/ProfileOrganisasiController.php`
- `Modules/DashboardPimpinan/Http/Controllers/SanksiPnbpController.php`
- `Modules/DashboardPimpinan/Jobs/KeragaanExportJob.php`
- `Modules/DashboardPimpinan/Jobs/ProfileOrganisasiExportJob.php`
- `Modules/DashboardPimpinan/Routes/api.php`
- `Modules/DashboardPimpinan/Services/KeragaanPSDKPService.php`
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`
- `Modules/DashboardPimpinan/Tests/Feature/ExportDataTest.php`
- `Modules/DashboardPimpinan/Transformers/KeragaanPSDKP/KeragaanPSDKPResource.php`
- `Modules/DashboardPimpinan/Transformers/KeragaanPSDKP/SatkerResource.php`
- `Modules/DashboardPimpinan/Transformers/ProfilUnitKerja/UptSebaranResource.php`
- `Modules/Gateway/Console/SIMPEG/SinkronPjlpCommand.php`
- `Modules/Gateway/Console/SIMPEG/SinkronPortalPegawaiCommand.php`
- `Modules/Gateway/Console/SIPALKA/SinkronDataKapal.php`
- `Modules/Gateway/Database/Migrations/2026_02_15_183737_add_flag_type_to_portal_dokumen_table.php`
- `Modules/Gateway/Database/Migrations/2026_02_26_200545_modify_column_to_oss_perizinan_proyek_table.php`
- `Modules/Gateway/Database/Seeders/SinkronKorespondensiAllLatestSeederTableSeeder.php`
- `Modules/Gateway/Database/Seeders/SinkronKorespondensiCurrentSeederTableSeeder.php`
- `Modules/Gateway/Database/Seeders/SinkronKorespondensiSeederTableSeeder.php`
- `Modules/Gateway/Entities/OSS/PerizinanProyek.php`
- `Modules/Gateway/Entities/PortalDokumen.php`
- `Modules/Gateway/Entities/PortalPenerimaDokumen.php`
- `Modules/Gateway/Http/Controllers/ELogbookController.php`
- `Modules/Gateway/Http/Controllers/KejaksaanController.php`
- `Modules/Gateway/Http/Controllers/KorespondensiController.php`
- `Modules/Gateway/Http/Controllers/OSS/PencarianPerizinanBerusahaController.php`
- `Modules/Gateway/Http/Controllers/PortalData/PencarianPerizinanKKPRLController.php`
- `Modules/Gateway/Http/Controllers/TPKPNasional/SPKPController.php`
- `Modules/Gateway/Http/Requests/OSS/PencarianPerizinanBerusahaRequest.php`
- `Modules/Gateway/Imports/SIMPEG/PjlpImport.php`
- `Modules/Gateway/Imports/SIPALKA/KapalImport.php`
- `Modules/Gateway/Jobs/Korespondensi/SimpanDataKorespondensiAllLatestJob.php`
- `Modules/Gateway/Jobs/Korespondensi/SimpanDataKorespondensiJob.php`
- `Modules/Gateway/Jobs/Korespondensi/SimpanDataKorespondensiManualJob.php`
- `Modules/Gateway/Jobs/SIMPEG/SinkronDataPortalPegawai.php`
- `Modules/Gateway/Jobs/SIMPEG/SinkronFotoPegawaiJob.php`
- `Modules/Gateway/Jobs/SIPALKA/SinkronDataKapal.php`
- `Modules/Gateway/Routes/api.php`
- `Modules/Gateway/Services/KKPRL/LaporanTahunanService.php`
- `Modules/Gateway/Services/OSS/OSSService.php`
- `Modules/Gateway/Services/OSS/V2/PencarianPerizinanBerusahaService.php`
- `Modules/Gateway/Services/PORTAL/KorespondensiService.php`
- `Modules/Gateway/Services/PORTAL/PortalService.php`
- `Modules/Gateway/Services/PORTALDATA/KKPRLService.php`
- `Modules/Gateway/Services/PORTALDATA/PencarianPerizinanKKPRLService.php`
- `Modules/Gateway/Services/SEAMAP/LaporanTahunanService.php`
- `Modules/Gateway/Services/SIMPEG/PegawaiPortalDataService.php`
- `Modules/Gateway/Services/TOPONIM/ToponimService.php`
- `Modules/HaloPSDKP/Services/AdminService.php`
- `Modules/HaloPSDKP/Services/PertanyaanService.php`
- `Modules/LaporanKegiatanUsaha/Entities/TransaksiLaporan.php`
- `Modules/LaporanKegiatanUsaha/Http/Controllers/MasterController.php`
- `Modules/LaporanKegiatanUsaha/Services/PelaporanService.php`
- `Modules/LaporanKegiatanUsaha/Services/VerifikasiPendaftaranService.php`
- `Modules/OperasiKapalPengawas/Services/SuratTugasService.php`
- `Modules/PenangananPelanggaran/Config/.gitkeep`
- `Modules/PenangananPelanggaran/Config/config.php`
- `Modules/PenangananPelanggaran/Console/.gitkeep`
- `Modules/PenangananPelanggaran/Database/Migrations/.gitkeep`
- `Modules/PenangananPelanggaran/Database/Seeders/.gitkeep`
- `Modules/PenangananPelanggaran/Database/Seeders/PenangananPelanggaranDatabaseSeeder.php`
- `Modules/PenangananPelanggaran/Database/factories/.gitkeep`
- `Modules/PenangananPelanggaran/Entities/.gitkeep`
- `Modules/PenangananPelanggaran/Http/Controllers/.gitkeep`
- `Modules/PenangananPelanggaran/Http/Controllers/PenangananPelanggaranController.php`
- `Modules/PenangananPelanggaran/Http/Middleware/.gitkeep`
- `Modules/PenangananPelanggaran/Http/Requests/.gitkeep`
- `Modules/PenangananPelanggaran/Http/Requests/PenetapanSanksi/TandaiPenetapanSanksiRequest.php`
- `Modules/PenangananPelanggaran/Providers/.gitkeep`
- `Modules/PenangananPelanggaran/Providers/PenangananPelanggaranServiceProvider.php`
- `Modules/PenangananPelanggaran/Providers/RouteServiceProvider.php`
- `Modules/PenangananPelanggaran/Resources/assets/.gitkeep`
- `Modules/PenangananPelanggaran/Resources/assets/js/app.js`
- `Modules/PenangananPelanggaran/Resources/assets/sass/app.scss`
- `Modules/PenangananPelanggaran/Resources/lang/.gitkeep`
- `Modules/PenangananPelanggaran/Resources/views/.gitkeep`
- `Modules/PenangananPelanggaran/Resources/views/index.blade.php`
- `Modules/PenangananPelanggaran/Resources/views/layouts/master.blade.php`
- `Modules/PenangananPelanggaran/Routes/.gitkeep`
- `Modules/PenangananPelanggaran/Routes/api.php`
- `Modules/PenangananPelanggaran/Routes/web.php`
- `Modules/PenangananPelanggaran/Services/PenetapanSanksiService.php`
- `Modules/PenangananPelanggaran/Tests/Feature/.gitkeep`

**Perubahan Utama:**
- PR #5306: Release: Update Production from Stage (2026-06-14) (+141683/-5453 baris).

**Manfaat:**
- Memastikan seluruh fitur dan perbaikan yang telah diverifikasi di lingkungan stage dapat digunakan oleh pengguna production, menjaga sistem tetap terkini dan stabil untuk operasional harian PSDKP.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5306

---

### 1.12 Hotfix server error 500 simpan kepatuhan teknis

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan hotfix server error 500 simpan kepatuhan teknis sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi hotfix resolusi error 500 dan import class Auth pada modul kepatuhan teknis.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait hotfix server error 500 simpan kepatuhan teknis. Implementasi hotfix resolusi error 500 dan import class Auth pada modul kepatuhan teknis

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisService.php`

**Perubahan Utama:**
- PR #5308: Hotfix: Resolusi Server Error 500 saat Simpan Kepatuhan Teknis (+14/-14 baris).
- PR #5310: Hotfix: Import Class Auth pada Kepatuhan Teknis (+1/-0 baris).

**Manfaat:**
- Memulihkan fungsionalitas penyimpanan data kepatuhan teknis yang sempat terganggu, sehingga petugas dapat kembali menginput dan menyimpan hasil penilaian kepatuhan tanpa gangguan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5308
- https://github.com/setditjen-psdkp/api-sip/pull/5310

---

### 1.13 Menyusun dokumentasi laporan perbaikan bug kepatuhan teknis

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyusun dokumentasi laporan perbaikan bug kepatuhan teknis sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Penyusunan dokumentasi laporan perbaikan bug kepatuhan teknis.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait menyusun dokumentasi laporan perbaikan bug kepatuhan teknis. Penyusunan dokumentasi laporan perbaikan bug kepatuhan teknis

**Detail Perubahan**

**File yang Diubah:**
- `docs/report/2026-06-15_hotfix-server-error-simpan-kepatuhan-teknis.md`

**Perubahan Utama:**
- PR #5311: Docs: Laporan Perbaikan Bug Kepatuhan Teknis (+50/-0 baris).

**Manfaat:**
- Memberikan catatan teknis yang terstruktur sebagai referensi tim pengembang dan auditor, memudahkan penelusuran riwayat perbaikan dan memastikan transparansi proses pengelolaan kualitas sistem.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5311

---

### 1.14 Memperbaiki akses data lintas unit untuk pengawas perikanan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki akses data lintas unit untuk pengawas perikanan sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan memperbaiki akses data lintas unit untuk pengawas perikanan.

**Deskripsi Pekerjaan**

Telah diimplementasikan memperbaiki akses data lintas unit untuk pengawas perikanan

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/PenjadwalanService.php`
- `docs/report/2026-06-15_fix-penjadwalan-pengawas-pusat.md`
- `tests/Unit/PengawasanPerizinanBerusaha/PenjadwalanServiceTest.php`

**Perubahan Utama:**
- PR #5312: fix: Allow Pengawas Perikanan Dit. PPSDP Pusat lintas UPT (+179/-3 baris).

**Manfaat:**
- Memungkinkan Pengawas Perikanan Dit. PPSDP Pusat mengakses dan menjadwalkan kegiatan di seluruh UPT tanpa batasan unit kerja, meningkatkan fleksibilitas koordinasi pengawasan lintas wilayah.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5312

---

### 1.15 Meningkatkan keamanan sistem, memperbaiki peta situs, dan menyesuaikan halaman admin

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem meningkatkan keamanan sistem, memperbaiki peta situs, dan menyesuaikan halaman admin sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan meningkatkan keamanan sistem, memperbaiki peta situs, dan menyesuaikan halaman admin.

**Deskripsi Pekerjaan**

Telah diimplementasikan meningkatkan keamanan sistem, memperbaiki peta situs, dan menyesuaikan halaman admin

**Detail Perubahan**

**File yang Diubah:**
- `app/Http/Controllers/API/V1/Auth/AuthController.php`
- `app/Http/Library/ApiHelpers.php`

**Perubahan Utama:**
- PR #15: fix bug create account (+46/-50 baris).

**Manfaat:**
- Memperkuat keamanan proses pembuatan akun pengguna dan meningkatkan kualitas antarmuka admin, sehingga risiko celah keamanan berkurang dan pengelolaan pengguna menjadi lebih andal.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/15

---

### 1.16 Memperbarui dokumentasi pemeriksaan keamanan server

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbarui dokumentasi pemeriksaan keamanan server sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan memperbarui dokumentasi pemeriksaan keamanan server.

**Deskripsi Pekerjaan**

Telah diimplementasikan memperbarui dokumentasi pemeriksaan keamanan server

**Detail Perubahan**

**File yang Diubah:**
- `app/Http/Controllers/API/V1/Auth/AuthController.php`
- `app/Http/Library/ApiHelpers.php`
- `app/Services/ApiPegawaiService.php`
- `app/Services/AuthService.php`
- `app/Services/ProfileGeneralService.php`
- `database/seeders/UserManagement/APIUserSeeder.php`

**Perubahan Utama:**
- PR #2258: Improve api simpeg and update api user seeder (+119/-209 baris).

**Manfaat:**
- Memastikan tim pengembang memiliki dokumentasi yang akurat dan terkini untuk kegiatan audit dan pemeriksaan keamanan server secara berkala, mendukung praktik DevSecOps yang berkelanjutan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/2258

---

### 1.17 Menyiapkan alat bantu untuk pemeriksaan rutin server

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyiapkan alat bantu untuk pemeriksaan rutin server sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan menyiapkan alat bantu untuk pemeriksaan rutin server.

**Deskripsi Pekerjaan**

Telah diimplementasikan menyiapkan alat bantu untuk pemeriksaan rutin server

**Detail Perubahan**

**File yang Diubah:**
- `Modules/LaporanKegiatanUsaha/Services/AuthLkuService.php`

**Perubahan Utama:**
- PR #2261: fix: handle file is null (+1/-1 baris).

**Manfaat:**
- Mencegah crash aplikasi akibat referensi file null pada layanan autentikasi LKU, meningkatkan stabilitas sistem saat pengguna melakukan login dengan kondisi data yang tidak lengkap.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/2261

---

### 1.18 Membuat sistem menampilkan data periode terbaru secara otomatis

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem membuat sistem menampilkan data periode terbaru secara otomatis sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan membuat sistem menampilkan data periode terbaru secara otomatis.

**Deskripsi Pekerjaan**

Telah diimplementasikan membuat sistem menampilkan data periode terbaru secara otomatis

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`

**Perubahan Utama:**
- PR #5432: feat: default to latest available period if year or month is empty fo… (+98/-24 baris).

**Manfaat:**
- Mengurangi kebutuhan konfigurasi manual oleh operator dalam memilih periode data. Sistem kini secara otomatis menampilkan data terkini, mempercepat akses informasi di Dashboard Pimpinan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5432

---

### 1.19 Penyesuaian fitur unduh data (export) pada modul PSDKP Angka

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem penyesuaian fitur unduh data (export) pada modul PSDKP Angka sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan penyesuaian fitur unduh data (export) pada modul psdkp angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan penyesuaian fitur unduh data (export) pada modul psdkp angka

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Http/Requests/ExportDashboardRequest.php`
- `Modules/DashboardPimpinan/Jobs/OperasiArmadaExportJob.php`
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`

**Perubahan Utama:**
- PR #5433: Modul/psdkp angka: export (+85/-39 baris).

**Manfaat:**
- Memungkinkan pimpinan dan staf mengunduh laporan data PSDKP Angka dalam berbagai kategori secara mandiri, mendukung kebutuhan pelaporan dan analisis data pengawasan secara efisien.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5433

---

### 1.20 Memperbaiki kendala teknis pada proses unduh data (export)

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki kendala teknis pada proses unduh data (export) sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan memperbaiki kendala teknis pada proses unduh data (export).

**Deskripsi Pekerjaan**

Telah diimplementasikan memperbaiki kendala teknis pada proses unduh data (export)

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Http/Requests/ExportDashboardRequest.php`
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`

**Perubahan Utama:**
- PR #5434: fix: resolve issues reported by static analysis (Bugbot) on export da… (+30/-18 baris).

**Manfaat:**
- Memastikan proses ekspor data berjalan tanpa error setelah dilakukan analisis statis, sehingga hasil unduhan dapat diandalkan untuk keperluan pelaporan resmi.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5434

---

### 1.21 Penyesuaian fitur POA pada modul PSDKP Angka

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem penyesuaian fitur POA pada modul PSDKP Angka sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan penyesuaian fitur poa pada modul psdkp angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan penyesuaian fitur poa pada modul psdkp angka

**Detail Perubahan**

**File yang Diubah:**
- `docs/report/2026-06-18_fix-generate-penertiban-rumpon-json.md`
- `public/bucket/s3_default/dashboard/operasiPengawasan/penertiban_rumpon/data.json`
- `scripts/DashboardPimpinan/generate_penertiban_rumpon_json.py`

**Perubahan Utama:**
- PR #5435: Modul/psdkp angka: poa (+81/-5 baris).

**Manfaat:**
- Menyediakan data penertiban rumpon yang akurat dan terstruktur dalam format JSON untuk Dashboard Pimpinan, mendukung visualisasi data operasi pengawasan kelautan secara komprehensif.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5435

---

### 1.22 Membuat tabel pemeriksaan agar rentang tahunnya otomatis tanpa batasan statis

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem membuat tabel pemeriksaan agar rentang tahunnya otomatis tanpa batasan statis sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan membuat tabel pemeriksaan agar rentang tahunnya otomatis tanpa batasan statis.

**Deskripsi Pekerjaan**

Telah diimplementasikan membuat tabel pemeriksaan agar rentang tahunnya otomatis tanpa batasan statis

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`

**Perubahan Utama:**
- PR #5437: fix: buat getTabelPemeriksaan dinamis tanpa hardcode tahun 2020-2025 (+31/-13 baris).

**Manfaat:**
- Menghilangkan hardcode rentang tahun yang membatasi tampilan data hanya hingga 2025, sehingga tabel pemeriksaan armada dapat menampilkan data secara dinamis untuk tahun-tahun mendatang.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5437

---

### 1.23 Membuat tampilan rentang grafik menyesuaikan dengan tahun yang dipilih

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem membuat tampilan rentang grafik menyesuaikan dengan tahun yang dipilih sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan membuat tampilan rentang grafik menyesuaikan dengan tahun yang dipilih.

**Deskripsi Pekerjaan**

Telah diimplementasikan membuat tampilan rentang grafik menyesuaikan dengan tahun yang dipilih

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`

**Perubahan Utama:**
- PR #5439: feat: buat rentang grafik dinamis mengikuti tahun filter request (+23/-17 baris).

**Manfaat:**
- Memberikan tampilan grafik yang relevan dan kontekstual sesuai tahun yang dipilih pengguna, meningkatkan kemudahan analisis tren operasi armada oleh pimpinan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5439

---

### 1.24 Membatasi rentang data riwayat dan perbandingan untuk 5 tahun terakhir secara otomatis

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem membatasi rentang data riwayat dan perbandingan untuk 5 tahun terakhir secara otomatis sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan membatasi rentang data riwayat dan perbandingan untuk 5 tahun terakhir secara otomatis.

**Deskripsi Pekerjaan**

Telah diimplementasikan membatasi rentang data riwayat dan perbandingan untuk 5 tahun terakhir secara otomatis

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`

**Perubahan Utama:**
- PR #5440: feat: batasi data history dan comparison menjadi dinamis 5 tahun tera… (+19/-2 baris).

**Manfaat:**
- Mencegah penumpukan data historis yang tidak relevan di dashboard, sehingga perbandingan data pengawasan lebih fokus dan tampilan lebih ringan untuk diakses.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5440

---

### 1.25 Membersihkan teks label yang tidak diperlukan pada layanan pengawasan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem membersihkan teks label yang tidak diperlukan pada layanan pengawasan sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan membersihkan teks label yang tidak diperlukan pada layanan pengawasan.

**Deskripsi Pekerjaan**

Telah diimplementasikan membersihkan teks label yang tidak diperlukan pada layanan pengawasan

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`

**Perubahan Utama:**
- PR #5441: fix: bersihkan sisa label TAHUN di PengawasanSdkpService (+15/-15 baris).

**Manfaat:**
- Membersihkan sisa label teks statis yang tidak relevan dari tampilan dashboard pengawasan SDKP, sehingga informasi yang disajikan kepada pimpinan lebih ringkas, akurat, dan tidak membingungkan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5441

---

### 1.26 Menyesuaikan penamaan file unduhan agar sesuai dengan jenis datanya

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyesuaikan penamaan file unduhan agar sesuai dengan jenis datanya sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan menyesuaikan penamaan file unduhan agar sesuai dengan jenis datanya.

**Deskripsi Pekerjaan**

Telah diimplementasikan menyesuaikan penamaan file unduhan agar sesuai dengan jenis datanya

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Jobs/PengawasanSdkpExportJob.php`

**Perubahan Utama:**
- PR #5442: fix: buat penamaan file export Pengawasan SDKP mengikuti nama chartType (+4/-3 baris).

**Manfaat:**
- Memudahkan pengguna mengidentifikasi file yang diunduh tanpa harus membuka isinya terlebih dahulu, meningkatkan produktivitas dalam pengelolaan arsip laporan data pengawasan SDKP.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5442

---

### 1.27 Memperbarui data pada modul PSDKP Angka

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbarui data pada modul PSDKP Angka sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan memperbarui data pada modul psdkp angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan memperbarui data pada modul psdkp angka

**Detail Perubahan**

**File yang Diubah:**
- `.gitignore`
- `Modules/DashboardPimpinan/Http/Controllers/DashboardPimpinanController.php`
- `Modules/DashboardPimpinan/Http/Requests/SyncAngkaRequest.php`
- `Modules/DashboardPimpinan/Jobs/SyncPsdkpAngkaJob.php`
- `Modules/DashboardPimpinan/Routes/api.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`
- `public/bucket/s3_default/dashboard/operasiPengawasan/hari_operasi/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/kapal_diperiksa/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/penerbitan_skat/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/rincian_hasil_tangkapan/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/rumpon/data.json`
- `public/bucket/s3_default/dashboard/sanksiPnbp/pnbp_aggregated.json`
- `public/bucket/s3_default/dashboard/sanksiPnbp/proses_hukum.json`
- `public/bucket/s3_default/dashboard/sanksiPnbp/sanksi_perbidang.json`
- `scripts/DashboardPimpinan/analyze_excel.py`
- `scripts/DashboardPimpinan/sync_psdkp_angka.py`

**Perubahan Utama:**
- PR #5444: Modul/psdkp angka: update data (+1030/-167 baris).

**Manfaat:**
- Memastikan data yang ditampilkan di Dashboard Pimpinan mencerminkan kondisi operasional terkini, mendukung pengambilan keputusan berbasis data yang akurat oleh pimpinan PSDKP.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5444

---

### 1.28 Memperbaiki validitas data asal pada modul PSDKP Angka

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki validitas data asal pada modul PSDKP Angka sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan memperbaiki validitas data asal pada modul psdkp angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan memperbaiki validitas data asal pada modul psdkp angka

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Jobs/PengawasanSdkpExportJob.php`
- `public/bucket/s3_default/dashboard/operasiPengawasan/hari_operasi/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/hari_operasi_skat_kapal_diperiksa/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/kapal_diperiksa/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/penerbitan_skat/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/penertiban_rumpon/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/rumpon/data.json`
- `scripts/DashboardPimpinan/sync_psdkp_angka.py`

**Perubahan Utama:**
- PR #5445: Modul/psdkp angka: fix ori data (+224/-275 baris).

**Manfaat:**
- Memastikan integritas data sumber yang digunakan sebagai dasar visualisasi dashboard, sehingga grafik dan tabel operasi pengawasan menampilkan angka yang valid dan dapat dipertanggungjawabkan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5445

---

### 1.29 Penyesuaian fitur modul PSDKP Angka

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem penyesuaian fitur modul PSDKP Angka sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan penyesuaian fitur modul psdkp angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan penyesuaian fitur modul psdkp angka

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Http/Controllers/DashboardPimpinanController.php`
- `Modules/DashboardPimpinan/Jobs/SyncPsdkpAngkaJob.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`
- `docs/report/2026-06-18_fix-cursor-bugbot-issues.md`
- `docs/report/2026-06-18_fix-pengawasan-sdkp-peak-logic.md`
- `public/bucket/s3_default/dashboard/operasiPengawasan/hari_operasi_skat_kapal_diperiksa/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/rincian_hasil_tangkapan/data.json`
- `public/bucket/s3_default/dashboard/pengawasanKelautan/data.json`
- `public/bucket/s3_default/dashboard/pengawasanPerikanan/data.json`
- `scripts/DashboardPimpinan/sync_psdkp_angka.py`

**Perubahan Utama:**
- PR #5447: Modul/psdkp angka (+251/-29 baris).

**Manfaat:**
- Meningkatkan keakuratan logika penentuan puncak operasi pengawasan dan menyelesaikan isu analisis statis yang dilaporkan, menjamin kualitas data yang ditampilkan kepada pimpinan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5447

---

### 1.30 Mengintegrasikan data dashboard speedboat ke dalam format sistem

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem mengintegrasikan data dashboard speedboat ke dalam format sistem sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan mengintegrasikan data dashboard speedboat ke dalam format sistem.

**Deskripsi Pekerjaan**

Telah diimplementasikan mengintegrasikan data dashboard speedboat ke dalam format sistem

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `docs/report/2026-06-18_feat-speedboat-excel-to-json.md`
- `scripts/DashboardPimpinan/generate_speedboat_json.py`

**Perubahan Utama:**
- PR #5448: feat(DashboardPimpinan): integrasi data speedboat dari Excel ke JSON … (+119/-2 baris).

**Manfaat:**
- Memungkinkan data armada speedboat yang sebelumnya tersimpan di Excel dapat divisualisasikan secara langsung di Dashboard Pimpinan, mendukung pemantauan armada laut PSDKP secara komprehensif.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5448

---

### 1.31 Menyiapkan data awal untuk dashboard speedboat

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyiapkan data awal untuk dashboard speedboat sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan menyiapkan data awal untuk dashboard speedboat.

**Deskripsi Pekerjaan**

Telah diimplementasikan menyiapkan data awal untuk dashboard speedboat

**Detail Perubahan**

**File yang Diubah:**
- `.gitignore`
- `public/bucket/s3_default/dashboard/speedboat/3. Data Speedboat T.A 2024.xlsx`
- `public/bucket/s3_default/dashboard/speedboat/4. Data Speedboat T.A 2025.xlsx`
- `public/bucket/s3_default/dashboard/speedboat/5. Daftar Speedboat 2026 + URC UPT (1.9.2025).xlsx`
- `public/bucket/s3_default/dashboard/speedboat/data.json`

**Perubahan Utama:**
- PR #5449: chore: allow speedboat dashboard data in gitignore and add initial data (+18/-0 baris).

**Manfaat:**
- Menyediakan data dasar armada speedboat tahun 2024-2026 dalam format JSON yang siap digunakan oleh sistem dashboard, memastikan visualisasi armada dapat ditampilkan segera setelah fitur diluncurkan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5449

---

### 1.32 Mengonfigurasi fitur obrolan (chat) backend dan mengatasi kendala jaringan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem mengonfigurasi fitur obrolan (chat) backend dan mengatasi kendala jaringan sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan mengonfigurasi fitur obrolan (chat) backend dan mengatasi kendala jaringan.

**Deskripsi Pekerjaan**

Telah diimplementasikan mengonfigurasi fitur obrolan (chat) backend dan mengatasi kendala jaringan

**Detail Perubahan**

**File yang Diubah:**
- `app/Console/Commands/TraitMaker.php`
- `app/Console/Commands/stubs/trait.stub`
- `app/Http/Controllers/API/V1/Auth/AuthController.php`
- `app/Http/Controllers/API/V1/Dashboard/Profile/PenugasanController.php`
- `app/Http/Controllers/API/V1/Dashboard/Profile/ProfileController.php`
- `app/Http/Controllers/API/V1/Notification/OtpController.php`
- `app/Http/Controllers/API/V1/Permohonan/PermohonanRegistrasiController.php`
- `app/Http/Library/ApiHelpers.php`
- `app/Http/Library/LokasiKerjaHelper.php`
- `app/Http/Library/OtpGenerator.php`
- `app/Http/Library/WaNotifications.php`
- `app/Http/Requests/authRegisterRequest.php`
- `app/Http/Requests/authSendOtpRequest.php`
- `app/Http/Requests/authVerifyOtpRequest.php`
- `app/Http/Requests/kewenanganCreateRequest.php`
- `app/Http/Requests/kewenanganUpdateRequest.php`
- `app/Http/Requests/updatePhoneRequest.php`
- `app/Http/Resources/AjukanPenugasanResource.php`
- `app/Http/Resources/Auth/UserResource.php`
- `app/Http/Resources/ProfileUnitKerjaResource.php`
- `app/Models/KewenanganPegawai.php`
- `app/Models/KontakPegawai.php`
- `app/Models/Otp.php`
- `app/Models/Satwas.php`
- `app/Models/UnitKerja.php`
- `app/Models/Wilker.php`
- `config/app.php`
- `database/migrations/2023_02_16_103931_create_kewenangan_pegawais_table.php`
- `database/migrations/2023_02_17_015639_create_unit_kerjas_table.php`
- `database/migrations/2023_03_21_032013_create_otps_table.php`
- `database/migrations/2023_03_21_032236_create_kontak_pegawais_table.php`
- `database/migrations/2023_03_27_095251_create_satwass_table.php`
- `database/migrations/2023_03_27_095713_create_wilkers_table.php`
- `database/migrations/2023_03_29_140311_add_server_code_to_otps.php`
- `routes/api.php`

**Perubahan Utama:**
- PR #17: Local dev (+495/-79 baris).

**Manfaat:**
- Membersihkan sisa label teks statis yang tidak relevan dari tampilan dashboard pengawasan SDKP, sehingga informasi yang disajikan kepada pimpinan lebih ringkas, akurat, dan tidak membingungkan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/17

---

### 1.33 Mengonfigurasi fitur obrolan (chat) frontend dan mengatasi kendala jaringan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem mengonfigurasi fitur obrolan (chat) frontend dan mengatasi kendala jaringan sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan mengonfigurasi fitur obrolan (chat) frontend dan mengatasi kendala jaringan.

**Deskripsi Pekerjaan**

Telah diimplementasikan mengonfigurasi fitur obrolan (chat) frontend dan mengatasi kendala jaringan

**Detail Perubahan**

**File yang Diubah:**
- `app/Http/Controllers/API/V1/Notification/OtpController.php`
- `app/Http/Library/EmailNotifications.php`
- `config/app.php`

**Perubahan Utama:**
- PR #25: Local dev (+137/-5 baris).

**Manfaat:**
- Memudahkan pengguna mengidentifikasi file yang diunduh tanpa harus membuka isinya terlebih dahulu, meningkatkan produktivitas dalam pengelolaan arsip laporan data pengawasan SDKP.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/25

---

### 1.34 Penyesuaian grafik utama pada modul PSDKP Angka

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem penyesuaian grafik utama pada modul PSDKP Angka sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan penyesuaian grafik utama pada modul psdkp angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan penyesuaian grafik utama pada modul psdkp angka

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `docs/report/2026-06-19_fix-pie-chart-sanksi-pnbp.md`

**Perubahan Utama:**
- PR #5453: Modul/psdkp angka: main pie chart  (+33/-2 baris).

**Manfaat:**
- Memastikan data yang ditampilkan di Dashboard Pimpinan mencerminkan kondisi operasional terkini, mendukung pengambilan keputusan berbasis data yang akurat oleh pimpinan PSDKP.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5453

---

### 1.35 Penyesuaian fitur pada modul PSDKP Angka

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem penyesuaian fitur pada modul PSDKP Angka sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan penyesuaian fitur pada modul psdkp angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan penyesuaian fitur pada modul psdkp angka

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Http/Controllers/DashboardPimpinanController.php`
- `Modules/DashboardPimpinan/Routes/api.php`

**Perubahan Utama:**
- PR #5455: Modul/psdkp angka (+14/-8 baris).

**Manfaat:**
- Memastikan integritas data sumber yang digunakan sebagai dasar visualisasi dashboard, sehingga grafik dan tabel operasi pengawasan menampilkan angka yang valid dan dapat dipertanggungjawabkan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5455

---

### 1.36 Memperbaiki pengamanan akses publik pada sistem

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki pengamanan akses publik pada sistem sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Telah diimplementasikan memperbaiki pengamanan akses publik pada sistem.

**Deskripsi Pekerjaan**

Telah diimplementasikan memperbaiki pengamanan akses publik pada sistem

**Detail Perubahan**

**File yang Diubah:**
- `app/Http/Middleware/AccessMiddleware.php`

**Perubahan Utama:**
- PR #5456: fix(Middleware): amankan akses public pada AccessMiddleware untuk res… (+16/-9 baris).

**Manfaat:**
- Meningkatkan keakuratan logika penentuan puncak operasi pengawasan dan menyelesaikan isu analisis statis yang dilaporkan, menjamin kualitas data yang ditampilkan kepada pimpinan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5456

---

### 1.37 Pengembangan Wedding Invitation Layout

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem pengembangan Wedding Invitation Layout sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Finalisasi tata letak, rotasi teks "Love Story", dan perataan koordinat elemen lokasi (Location Pin) pada frontend portal.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait pengembangan wedding invitation layout. Finalisasi tata letak, rotasi teks "Love Story", dan perataan koordinat elemen lokasi (Location Pin) pada frontend portal

**Detail Perubahan**

**Perubahan Utama:**
- Pengujian dan verifikasi fungsionalitas sistem Asta Data PSDKP Cilacap sesuai skenario UAT yang telah ditetapkan oleh tim pengguna lapangan.

**Manfaat:**
- Memungkinkan data armada speedboat yang sebelumnya tersimpan di Excel dapat divisualisasikan secara langsung di Dashboard Pimpinan, mendukung pemantauan armada laut PSDKP secara komprehensif.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/issues/5276

---

### 1.38 Migrasi fitur cabang sdn-kacangan ke main

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan migrasi fitur cabang sdn-kacangan ke main sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Pengaturan environment vars, reset data dummy presensi/cuti, pembaruan akses login admin, dan manajemen sinkronisasi cabang.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait migrasi fitur cabang sdn-kacangan ke main. Pengaturan environment vars, reset data dummy presensi/cuti, pembaruan akses login admin, dan manajemen sinkronisasi cabang

**Detail Perubahan**

**Perubahan Utama:**
- Pengujian dan verifikasi fungsionalitas sistem Asta Data PSDKP Cilacap sesuai skenario UAT yang telah ditetapkan oleh tim pengguna lapangan.

**Manfaat:**
- Menyediakan data dasar armada speedboat tahun 2024-2026 dalam format JSON yang siap digunakan oleh sistem dashboard, memastikan visualisasi armada dapat ditampilkan segera setelah fitur diluncurkan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/issues/5276

---

### 1.39 Pengembangan sistem otomasi VPS Storage Backup

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem pengembangan sistem otomasi VPS Storage Backup sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi skrip Python vps-backup-gdrive.py untuk audit penyimpan, pencadangan ke Google Drive (OAuth), dan pembersihan otomatis.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait pengembangan sistem otomasi vps storage backup. Implementasi skrip Python vps-backup-gdrive.py untuk audit penyimpan, pencadangan ke Google Drive (OAuth), dan pembersihan otomatis

**Detail Perubahan**

**Perubahan Utama:**
- Pengujian dan verifikasi fungsionalitas sistem Asta Data PSDKP Cilacap sesuai skenario UAT yang telah ditetapkan oleh tim pengguna lapangan.

**Manfaat:**
- Memperbaiki tampilan pie chart sanksi PNBP agar data terdistribusi secara akurat dan visual, memberikan gambaran proporsi jenis sanksi yang jelas kepada pimpinan PSDKP.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/issues/5276

---

### 1.40 Optimasi performa eksport SKP & Spatial Mapping

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan optimasi performa eksport SKP & Spatial Mapping sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Implementasi export chunking (500 data) untuk memecahkan error 500 saat generasi excel dan validasi sinkronisasi koordinat kosong.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait optimasi performa eksport skp & spatial mapping. Implementasi export chunking (500 data) untuk memecahkan error 500 saat generasi excel dan validasi sinkronisasi koordinat kosong

**Detail Perubahan**

**Perubahan Utama:**
- Pengujian dan verifikasi fungsionalitas sistem Asta Data PSDKP Cilacap sesuai skenario UAT yang telah ditetapkan oleh tim pengguna lapangan.

**Manfaat:**
- Menyempurnakan routing dan controller Dashboard Pimpinan agar endpoint API bekerja secara konsisten, memastikan seluruh data PSDKP Angka dapat diakses dengan benar oleh frontend.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/issues/5276

---

### 1.41 Resolusi Error Git & Integrasi Layanan Backend

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan resolusi Error Git & Integrasi Layanan Backend sebagai bagian dari pembaruan modul WasRisk. Kegiatan ini berkaitan dengan: Perbaikan URL profil, sinkronisasi repositori lintas platform, resolusi TypeError payment service fallback konfigurasi.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait resolusi error git & integrasi layanan backend. Perbaikan URL profil, sinkronisasi repositori lintas platform, resolusi TypeError payment service fallback konfigurasi

**Detail Perubahan**

**Perubahan Utama:**
- Pengujian dan verifikasi fungsionalitas sistem Asta Data PSDKP Cilacap sesuai skenario UAT yang telah ditetapkan oleh tim pengguna lapangan.

**Manfaat:**
- Memungkinkan fitur komunikasi real-time berbasis chat di platform Grafisa berfungsi pada lingkungan development lokal, mempercepat proses pengembangan dan pengujian fitur kolaborasi antar pengguna.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/issues/5276

---

## 2. Memperbaharui Webservice Modul User Management

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice User Management, sebagai berikut:

### 2.1 Memperbaharui permission dan seeder master data SDK

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui permission dan seeder master data SDK sebagai bagian dari pembaruan modul User Management. Kegiatan ini berkaitan dengan: Implementasi update seeder AkunTableSeeder, perbaikan filter role dan permission by user pada modul Master Data/SDK.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaharui permission dan seeder master data sdk. Implementasi update seeder AkunTableSeeder, perbaikan filter role dan permission by user pada modul Master Data/SDK

**Detail Perubahan**

**File yang Diubah:**
- `Modules/PengawasanPerizinanBerusaha/Database/Seeders/SDK/AkunTableSeeder.php`
- `Modules/PengawasanPerizinanBerusaha/Services/SDK/PemantauanService.php`
- `app/Http/Library/AuthHelpers.php`

**Perubahan Utama:**
- PR #5270: Fitur/master data: update seeder dan filter role (+36/-5 baris).
- PR #5271: Fitur/master data: fix permission (+18/-8 baris).
- PR #5272: fix: permission by user (+8/-1 baris).
- PR #5273: fix: permission (+4/-4 baris).
- PR #5274: fix: permission (+23/-27 baris).

**Manfaat:**
- Memastikan pembagian hak akses pada modul Master Data SDK berjalan sesuai peran pengguna, mencegah akses tidak sah dan memastikan integritas data seeder untuk lingkungan pengujian dan production.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5270
- https://github.com/setditjen-psdkp/api-sip/pull/5271
- https://github.com/setditjen-psdkp/api-sip/pull/5272
- https://github.com/setditjen-psdkp/api-sip/pull/5273
- https://github.com/setditjen-psdkp/api-sip/pull/5274

---

## 3. Penyusunan dan Pembaharuan Modul PSDKP Angka (Dashboard Pimpinan)

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem menyusun dan memperbaharui webservice PSDKP Angka, sebagai berikut:

### 3.1 Implementasi unified dashboard export

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan implementasi unified dashboard export sebagai bagian dari pembaruan modul PSDKP Angka. Kegiatan ini berkaitan dengan: Implementasi fitur export terpadu untuk semua kategori dashboard pimpinan.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait implementasi unified dashboard export. Implementasi fitur export terpadu untuk semua kategori dashboard pimpinan

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Exports/GenericExport.php`
- `Modules/DashboardPimpinan/Http/Controllers/DashboardPimpinanController.php`
- `Modules/DashboardPimpinan/Http/Requests/ExportDashboardRequest.php`
- `Modules/DashboardPimpinan/Jobs/KeragaanExportJob.php`
- `Modules/DashboardPimpinan/Jobs/OperasiArmadaExportJob.php`
- `Modules/DashboardPimpinan/Jobs/PengawasanSdkpExportJob.php`
- `Modules/DashboardPimpinan/Jobs/ProfileOrganisasiExportJob.php`
- `Modules/DashboardPimpinan/Jobs/SanksiPnbpExportJob.php`
- `Modules/DashboardPimpinan/Services/DashboardExportService.php`
- `Modules/DashboardPimpinan/Tests/Feature/ExportDataTest.php`
- `docs/report/2026-06-11_feat-unified-dashboard-export.md`
- `docs/report/2026-06-11_fix-dashboard-export-validation.md`

**Perubahan Utama:**
- PR #5299: feat: implement unified dashboard export for all categories (+902/-48 baris).

**Manfaat:**
- Memungkinkan fitur komunikasi real-time berbasis chat di platform Grafisa berfungsi pada lingkungan development lokal, mempercepat proses pengembangan dan pengujian fitur kolaborasi antar pengguna.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5299

---

### 3.2 Menyesuaikan teks label pada kartu informasi di Dashboard Pimpinan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyesuaikan teks label pada kartu informasi di Dashboard Pimpinan sebagai bagian dari pembaruan modul PSDKP Angka. Kegiatan ini berkaitan dengan: Telah diimplementasikan menyesuaikan teks label pada kartu informasi di dashboard pimpinan.

**Deskripsi Pekerjaan**

Telah diimplementasikan menyesuaikan teks label pada kartu informasi di dashboard pimpinan

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`
- `public/bucket/s3_default/dashboard/operasiPengawasan/rincian_hasil_tangkapan/data.json`
- `scripts/DashboardPimpinan/generate_rincian_hasil_tangkapan_json.py`

**Perubahan Utama:**
- PR #5436: fix: hapus label tahun/bulan dari card DashboardPimpinan & perbaiki s… (+48/-70 baris).

**Manfaat:**
- Memastikan pembagian hak akses pada modul Master Data SDK berjalan sesuai peran pengguna, mencegah akses tidak sah dan memastikan integritas data seeder untuk lingkungan pengujian dan production.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5436

---

### 3.3 Membatasi tampilan grafik dan tabel operasi armada untuk rentang 5 tahun terakhir

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem membatasi tampilan grafik dan tabel operasi armada untuk rentang 5 tahun terakhir sebagai bagian dari pembaruan modul PSDKP Angka. Kegiatan ini berkaitan dengan: Telah diimplementasikan membatasi tampilan grafik dan tabel operasi armada untuk rentang 5 tahun terakhir.

**Deskripsi Pekerjaan**

Telah diimplementasikan membatasi tampilan grafik dan tabel operasi armada untuk rentang 5 tahun terakhir

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`

**Perubahan Utama:**
- PR #5438: feat: batasi grafik dan tabel OperasiArmada tampil per 5 tahun terakhir (+6/-3 baris).

**Manfaat:**
- Membuat visualisasi operasi armada lebih fokus dan relevan dengan membatasi tampilan pada 5 tahun terakhir, mengurangi kepadatan informasi dan memudahkan analisis tren oleh pimpinan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5438

---

### 3.4 Memulihkan dan menyesuaikan ulang data operasi armada tahun 2026

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memulihkan dan menyesuaikan ulang data operasi armada tahun 2026 sebagai bagian dari pembaruan modul PSDKP Angka. Kegiatan ini berkaitan dengan: Telah diimplementasikan memulihkan dan menyesuaikan ulang data operasi armada tahun 2026.

**Deskripsi Pekerjaan**

Telah diimplementasikan memulihkan dan menyesuaikan ulang data operasi armada tahun 2026

**Detail Perubahan**

**File yang Diubah:**
- `public/bucket/s3_default/dashboard/operasiPengawasan/penertiban_rumpon/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/rincian_hasil_tangkapan/data.json`
- `public/bucket/s3_default/dashboard/pengawasanKelautan/data.json`
- `public/bucket/s3_default/dashboard/pengawasanPerikanan/data.json`

**Perubahan Utama:**
- PR #5446: fix: restore data operasi armada dan sinkronisasi ulang data 2026 tan… (+704/-656 baris).

**Manfaat:**
- Membuat visualisasi operasi armada lebih fokus dan relevan dengan membatasi tampilan pada 5 tahun terakhir, mengurangi kepadatan informasi dan memudahkan analisis tren oleh pimpinan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5446

---

### 3.5 Menyelesaikan beberapa kendala tampilan dan data pada Dashboard Pimpinan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyelesaikan beberapa kendala tampilan dan data pada Dashboard Pimpinan sebagai bagian dari pembaruan modul PSDKP Angka. Kegiatan ini berkaitan dengan: Telah diimplementasikan menyelesaikan beberapa kendala tampilan dan data pada dashboard pimpinan.

**Deskripsi Pekerjaan**

Telah diimplementasikan menyelesaikan beberapa kendala tampilan dan data pada dashboard pimpinan

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`
- `scripts/DashboardPimpinan/generate_speedboat_json.py`

**Perubahan Utama:**
- PR #5450: fix(DashboardPimpinan): resolusi 4 isu Cursor Bugbot (speedboat JSON,… (+24/-6 baris).

**Manfaat:**
- Menyediakan fitur ekspor terpadu untuk semua kategori Dashboard Pimpinan dalam satu antarmuka, memudahkan pimpinan mendapatkan laporan lintas bidang tanpa harus mengakses setiap modul secara terpisah.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5450

---

## 4. Modul Master Data / OSS / KKPRL

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice Master Data, sebagai berikut:

### 4.1 Memperbaiki penanganan data dummy sinkronisasi KKPRL

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki penanganan data dummy sinkronisasi KKPRL sebagai bagian dari pembaruan modul Master Data. Kegiatan ini berkaitan dengan: Implementasi perbaikan data dummy berdasarkan subjek hukum pada proses sinkronisasi KKPRL.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaiki penanganan data dummy sinkronisasi kkprl. Implementasi perbaikan data dummy berdasarkan subjek hukum pada proses sinkronisasi KKPRL

**Detail Perubahan**

**File yang Diubah:**
- `.agents/instructions/rules/reporting.md`
- `.agents/skills/ai_assistant/SKILL.md`
- `Modules/Userman/Jobs/Sync/KKPRL/SyncKKPRLPerizinanJob.php`
- `docs/report/2026-06-11_fix-penanganan-data-dummy-kkprl-subjek-hukum.md`

**Perubahan Utama:**
- PR #5295: Fix: Penanganan Data Dummy pada Sinkronisasi KKPRL berdasarkan Subjek Hukum (+146/-1 baris).

**Manfaat:**
- Mencegah data dummy subjek hukum mengganggu proses sinkronisasi perizinan KKPRL, memastikan hanya data valid yang diproses sehingga integritas data pengawasan perairan laut terjaga.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5295

---

### 4.2 Memperbaiki timeout dan deteksi file sinkronisasi OSS

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki timeout dan deteksi file sinkronisasi OSS sebagai bagian dari pembaruan modul Master Data. Kegiatan ini berkaitan dengan: Implementasi perbaikan fail-fast timeout, deteksi file, PDF stripping, dan penanganan long whitespace pada sinkronisasi OSS/KKPRL.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait memperbaiki timeout dan deteksi file sinkronisasi oss. Implementasi perbaikan fail-fast timeout, deteksi file, PDF stripping, dan penanganan long whitespace pada sinkronisasi OSS/KKPRL

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Gateway/Services/OSS/OSSService.php`
- `docs/report/2026-06-11_fix-timeout-dan-deteksi-pdf-sinkron-oss.md`
- `tests/Unit/OSSServiceTest.php`

**Perubahan Utama:**
- PR #5301: Fix: Perbaikan Timeout dan Deteksi File Sinkronisasi OSS (#5180) (+178/-4 baris).
- PR #5303: Fix: Perbaikan Fail-Fast Timeout dan PDF Stripping pada OSS (#5180) (+16/-7 baris).
- PR #5304: Fix: Penanganan Spasi Panjang (Long Whitespace) pada Deteksi PDF OSS (#5180) (+25/-7 baris).

**Manfaat:**
- Meningkatkan ketahanan proses sinkronisasi data OSS dengan mekanisme fail-fast dan deteksi file PDF yang lebih akurat, sehingga data perizinan usaha tersinkronisasi secara andal.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5301
- https://github.com/setditjen-psdkp/api-sip/pull/5303
- https://github.com/setditjen-psdkp/api-sip/pull/5304

---

### 4.3 Penyelesaian issue filter KKPRL berdasarkan unit kerja

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem penyelesaian issue filter KKPRL berdasarkan unit kerja sebagai bagian dari pembaruan modul Master Data. Kegiatan ini berkaitan dengan: Penyelesaian issue filter list KKPRL dalam detail berdasarkan unit kerja.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait penyelesaian issue filter kkprl berdasarkan unit kerja. Penyelesaian issue filter list KKPRL dalam detail berdasarkan unit kerja

**Detail Perubahan**

**Perubahan Utama:**
- Pengujian dan verifikasi fungsionalitas sistem Asta Data PSDKP Cilacap sesuai skenario UAT yang telah ditetapkan oleh tim pengguna lapangan.

**Manfaat:**
- Memungkinkan petugas melihat daftar KKPRL yang relevan dengan unit kerja mereka secara spesifik, meningkatkan efisiensi pengawasan perizinan berbasis lokasi dan kewenangan unit kerja.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/issues/5276

---

### 4.4 UAT Kewilayahan Spasial & Audit Sinkronisasi OSS

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan uAT Kewilayahan Spasial & Audit Sinkronisasi OSS sebagai bagian dari pembaruan modul Master Data. Kegiatan ini berkaitan dengan: Verifikasi topology GeoJSON (Point, Polygon, Line), resolusi kendala payload. Perbaikan NIB Duplicate dengan perintah artisan cleanup-duplicate-nib.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi terkait uat kewilayahan spasial & audit sinkronisasi oss. Verifikasi topology GeoJSON (Point, Polygon, Line), resolusi kendala payload. Perbaikan NIB Duplicate dengan perintah artisan cleanup-duplicate-nib

**Detail Perubahan**

**Perubahan Utama:**
- Pengujian dan verifikasi fungsionalitas sistem Asta Data PSDKP Cilacap sesuai skenario UAT yang telah ditetapkan oleh tim pengguna lapangan.

**Manfaat:**
- Mencegah data dummy subjek hukum mengganggu proses sinkronisasi perizinan KKPRL, memastikan hanya data valid yang diproses sehingga integritas data pengawasan perairan laut terjaga.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/issues/5276

---

## RINGKASAN KEGIATAN

Total sub-kegiatan dari weekly report: **51**
