# DETAIL LAPORAN KEGIATAN GITHUB — LUTFI IHSAN
## Bulan Mei 2026 (Periode Weekly Report W1–W3)

Sumber data: `202605_Program dan Data Weekly Report.docx.md`  
Format acuan: `Contoh Format.docx`

---

## 1. Memperbaharui Webservice Modul WasRisk

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice Modul WasRisk, sebagai berikut:

### 1.1 Menambahkan notifikasi pengesahan dokumen hasil inspeksi by sistem

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menambahkan notifikasi pengesahan dokumen hasil inspeksi by sistem sebagai bagian dari pembaruan modul WasRisk.

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

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui logic unggah objek pengawasan sebagai bagian dari pembaruan modul WasRisk.

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

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui logic dashboard WasRisk sebagai bagian dari pembaruan modul WasRisk.

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

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui logic notifikasi pengesahan dokumen hasil inspeksi (per objek) sebagai bagian dari pembaruan modul WasRisk.

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

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui logic penjadwalan pengawas sebagai bagian dari pembaruan modul WasRisk.

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

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui logic simpan pertanyaan inspeksi WasRisk sebagai bagian dari pembaruan modul WasRisk.

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
- Mencegah BAP diselesaikan tanpa jawaban pertanyaan wajib.
- Mengatasi crash PHP 8.x saat menyimpan pertanyaan inspeksi.
- Kompatibilitas dengan optimasi query N+1 pada service layer.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5220

---

### 1.7 Perbaikan logic simpan Berita Acara WasRisk (Lock Wait Timeout & Race Condition)

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem perbaikan logic simpan Berita Acara WasRisk (Lock Wait Timeout & Race Condition) sebagai bagian dari pembaruan modul WasRisk.

**Deskripsi Pekerjaan**

Telah dilakukan serangkaian hotfix kritis untuk mengatasi error `SQLSTATE[1205] Lock wait timeout exceeded` dan race condition pada notifikasi dokumen hasil inspeksi saat pengawas menyimpan BAP Tab 3 dan proses generate dokumen PDF.

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanPbUmkuService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanSelfDeclareService.php`
- `app/Http/Resources/PengawasanPerizinanBerusaha/InspeksiLapangan/InspeksiLapanganResource.php`
- `tests/Unit/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanServiceTest.php`
- `tests/Unit/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisServiceTest.php`
- `tests/Unit/PengawasanPerizinanBerusaha/PertanyaanPbUmkuServiceTest.php`
- `tests/Unit/PengawasanPerizinanBerusaha/PertanyaanSelfDeclareServiceTest.php`

**Perubahan Utama:**

*PR #5229 — Lock Wait Timeout BAP Tab 3:*
- Memindahkan HTTP call ke OSS API keluar dari `DB::beginTransaction()`.
- Memindahkan `generateDokumenHasilPengawasan()` ke luar transaksi DB (setelah `DB::commit()`).
- Memindahkan validasi `jenisPertanyaan` sebelum `beginTransaction()`.
- Mengganti `InspeksiLapanganService->show()` (HTTP) dengan `InspeksiLapanganResource` (DB lokal).
- Unit test: 21 test PASS.

*PR #5231 — Lock Wait Timeout Generate Dokumen:*
- Memindahkan HTTP call OSS dan render PDF (SnappyPDF) keluar dari transaksi DB pada service Self Declare, PB UMKU, dan Kepatuhan Teknis.
- Transaksi DB hanya untuk `updateOrCreate` path dokumen (< 50ms).

*PR #5232 — PDOException Rollback:*
- Pembungkus `DB::rollBack()` dengan `if (DB::transactionLevel() > 0)`.
- Try-catch terpisah pada `generateDokumenHasilPengawasan` agar kegagalan PDF tidak mengubah response sukses BAP.

*PR #5233 — Pre-fetch jenis_pertanyaan:*
- Pre-fetch `InspeksiLapanganResource->toArray()` sebelum transaksi DB pada Tab Penanggung Jawab (status "Tidak Ada").

*PR #5235 — Race Condition Notifikasi:*
- Refactor `generateDokumenHasilPengawasan` menggunakan `Bus::chain()` untuk eksekusi sekuensial.
- Notifikasi verifikasi dokumen dikirim sebagai job terakhir dalam chain, setelah semua PDF selesai.

**Manfaat:**
- Lock database berdurasi < 50ms (sebelumnya 4–10 detik).
- Pengawas tidak lagi mengalami timeout saat menyimpan BAP Tab 3.
- Notifikasi dokumen hasil inspeksi hanya terkirim setelah PDF 100% selesai dibuat.
- User experience lebih baik — data tersimpan meskipun generate PDF gagal.

**Catatan teknis singkat:**
- Root cause: HTTP call OSS (~2–5 detik) dan render PDF di dalam transaksi DB.
- Solusi: Pisahkan I/O eksternal dari transaksi DB, gunakan `Bus::chain()` untuk urutan job.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5229
- https://github.com/setditjen-psdkp/api-sip/pull/5231
- https://github.com/setditjen-psdkp/api-sip/pull/5232
- https://github.com/setditjen-psdkp/api-sip/pull/5233
- https://github.com/setditjen-psdkp/api-sip/pull/5235

---

## 2. Memperbaharui Webservice Modul User Management

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice Modul User Management, sebagai berikut:

### 2.1 Memperbaharui logic update user (anti deadlock)

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui logic update user (anti deadlock) sebagai bagian dari pembaruan modul User Management.

**Deskripsi Pekerjaan**

Telah diperbaiki masalah deadlock (`SQLSTATE[40001]: Serialization failure: 1213 Deadlock`) yang terjadi saat update user secara concurrent, khususnya pada operasi `syncRoles` di tabel `model_has_roles`.

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/UserService.php`
- `tests/Feature/UserServiceTest.php`
- `.agents/instructions/rules/testing.md`

**Perubahan Utama:**
- Penambahan `->lockForUpdate()` pada query `find($id)` di method `updateUser`, `assignRole`, `activationUser`, dan `deleteUser`.
- Implementasi pessimistic locking untuk memaksa eksekusi berurutan pada data user yang sama.
- Penambahan feature test `UserServiceTest` dengan `DatabaseTransactions` (bukan `RefreshDatabase`).
- Update aturan testing: dilarang menggunakan trait `RefreshDatabase`.

**Manfaat:**
- Menghilangkan deadlock saat user mengklik tombol simpan berulang kali.
- Request concurrent dipaksa antre secara serial per user ID.
- Database lokal aman saat pengujian (auto-rollback).

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5130

---

## 3. Memperbaharui Webservice Modul Korespondensi

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice Modul Korespondensi, sebagai berikut:

### 3.1 Memperbaharui API korespondensi — input surat manual

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui API korespondensi — input surat manual sebagai bagian dari pembaruan modul Korespondensi.

**Deskripsi Pekerjaan**

Telah diimplementasikan dukungan input surat manual pada modul korespondensi melalui penyesuaian resource transformer dokumen surat.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Userman/Transformers/Master/PORTAL/DokumenSuratResource.php`

**Perubahan Utama:**
- Penyesuaian `DokumenSuratResource` untuk mendukung alur input surat manual.

**Manfaat:**
- Pengguna dapat memasukkan surat korespondensi secara manual tanpa melalui sinkronisasi otomatis.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5139

---

### 3.2 Perbaikan sinkron korespondensi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem perbaikan sinkron korespondensi sebagai bagian dari pembaruan modul Korespondensi.

**Deskripsi Pekerjaan**

Telah diperbaiki proses sinkronisasi penerima surat dari korespondensi dan filter data pokmaswas pada modul Dashboard Pimpinan.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `Modules/Gateway/Entities/PortalPenerimaDokumen.php`
- `Modules/Gateway/Jobs/Korespondensi/SimpanDataKorespondensiJob.php`

**Perubahan Utama:**
- Perbaikan filter pokmaswas pada service profil organisasi.
- Penyesuaian job sinkronisasi data korespondensi untuk penerima surat.

**Manfaat:**
- Data penerima surat korespondensi tersinkronisasi dengan benar.
- Filter pokmaswas menampilkan data yang akurat.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5149

---

### 3.3 Memperbaharui webservice daftar KM korespondensi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice daftar KM korespondensi sebagai bagian dari pembaruan modul Korespondensi.

**Deskripsi Pekerjaan**

Telah diperbarui webservice daftar kilometer (KM) pada modul korespondensi CRS.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Userman/Services/Master/KorespondensiCSRS/KorespondensiCRSService.php`

**Perubahan Utama:**
- Pembaruan logic `getListKm` pada service korespondensi CRS.

**Manfaat:**
- Daftar KM korespondensi ditampilkan sesuai kebutuhan modul terbaru.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5201

---

### 3.4 Memperbaharui webservice tambah dokumen korespondensi manual

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice tambah dokumen korespondensi manual sebagai bagian dari pembaruan modul Korespondensi.

**Deskripsi Pekerjaan**

Telah diimplementasikan fitur input freetext untuk field Sender pada penyimpanan dokumen korespondensi manual, beserta master table `portal_senders` dan resolusi isu migration modul Userman.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Userman/Services/Master/KorespondensiCSRS/KorespondensiCRSService.php`
- `Modules/Userman/Entities/Master/PortalKorespondensiCRS/PortalSender.php`
- `Modules/Userman/Database/Migrations/2026_05_21_051514_create_portal_senders_table.php`
- `Modules/Userman/Config/sync_master.php`
- `Modules/Userman/Tests/Unit/KorespondensiCRSTest.php`
- `modules_statuses.json`

**Perubahan Utama:**
- Penambahan tabel master `portal_senders` dan model `PortalSender`.
- Input freetext sender pada `storeManualDokumen` via `firstOrCreate`.
- `getSender` menampilkan gabungan unik sender dari `portal_dokumen` dan `portal_senders`.
- Enable kembali modul Userman dengan placeholder `sync_master.php`.
- Unit test validasi freetext sender dan merge list sender.

**Manfaat:**
- Pengguna dapat memasukkan nama pengirim surat secara bebas (freetext).
- Data sender terkonsolidasi antara data lama dan master baru.
- Migration modul Userman berjalan normal tanpa argumen `--path`.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5248

---

## 4. Penyusunan dan Pembaharuan Modul PSDKP Angka (Dashboard Pimpinan)

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem menyusun dan memperbaharui webservice Modul PSDKP Angka, sebagai berikut:

### 4.1 Menyusun API profil organisasi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyusun API profil organisasi sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan API profil organisasi pada modul Dashboard Pimpinan, mencakup controller, service, routes, dan transformer data sebaran UPT.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Http/Controllers/ProfileOrganisasiController.php`
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `Modules/DashboardPimpinan/Routes/api.php`
- `Modules/DashboardPimpinan/Transformers/ProfilUnitKerja/UptSebaranResource.php`

**Perubahan Utama:**
- Penambahan controller dan service profil organisasi (+612 baris service logic).
- Penambahan endpoint API pada routes modul Dashboard Pimpinan.
- Transformer `UptSebaranResource` untuk data sebaran unit kerja.

**Endpoint Baru:**
- Endpoint API profil organisasi pada modul Dashboard Pimpinan (lihat `Routes/api.php`).

**Manfaat:**
- Dashboard Pimpinan dapat menampilkan profil organisasi PSDKP secara terstruktur.
- Data sebaran UPT tersedia untuk visualisasi dashboard.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5141

---

### 4.2 Memperbaharui sinkron pegawai, asset, dan kapal pengawas

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui sinkron pegawai, asset, dan kapal pengawas sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah dilakukan peningkatan proses sinkronisasi data pegawai (portal SIMPEG), asset (SiSarwas), dan kapal pengawas, serta penambahan controller dan service pendukung modul PSDKP Angka.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Gateway/Jobs/SIMPEG/SinkronDataPortalPegawai.php`
- `Modules/Sisarwas/Imports/DataAssetImport.php`
- `Modules/Sisarwas/Jobs/SinkronDataAssetJob.php`
- `Modules/DashboardPimpinan/Http/Controllers/OperasiArmadaController.php`
- `Modules/DashboardPimpinan/Http/Controllers/PengawasanSdkpController.php`
- `Modules/DashboardPimpinan/Http/Controllers/SanksiPnbpController.php`
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`
- `database/migrations/2026_05_07_083716_add_data_surat_to_kapals_table.php`
- `database/seeders/Master/Kapal/KapalPengawasSeeder.php`
- `app/Http/Library/StringHelper.php`

**Perubahan Utama:**
- Optimasi job sinkronisasi portal pegawai SIMPEG.
- Perbaikan import dan job sinkronisasi asset SiSarwas.
- Penambahan kolom `data_surat` pada tabel kapal via migration.
- Seeder data kapal pengawas (+502 baris).
- Penambahan helper `StringHelper` untuk normalisasi string.
- Penambahan controller dan service operasi armada, pengawasan SDKP, dan sanksi PNBP.

**Manfaat:**
- Data pegawai, asset, dan kapal pengawas tersinkronisasi lebih efisien.
- Fondasi data master kapal pengawas lengkap untuk dashboard.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5146

---

### 4.3 Menyusun webservice export profil organisasi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyusun webservice export profil organisasi sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan fitur export data profil organisasi dan keragaan PSDKP melalui background job dengan pengiriman hasil via email.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Exports/KeragaanExport.php`
- `Modules/DashboardPimpinan/Exports/KeragaanKapalExport.php`
- `Modules/DashboardPimpinan/Jobs/KeragaanExportJob.php`
- `Modules/DashboardPimpinan/Jobs/ProfileOrganisasiExportJob.php`
- `Modules/DashboardPimpinan/Http/Controllers/DashboardPimpinanController.php`
- `Modules/DashboardPimpinan/Routes/api.php`
- `Modules/DashboardPimpinan/Tests/Feature/ExportDataTest.php`
- `app/Services/Gateway/MailService.php`

**Perubahan Utama:**
- Penambahan export class untuk data keragaan dan keragaan kapal.
- Background job `ProfileOrganisasiExportJob` dan `KeragaanExportJob`.
- Endpoint export pada controller dan routes.
- Feature test `ExportDataTest` (109 baris).
- Penyesuaian `MailService` untuk pengiriman file export.

**Manfaat:**
- Pengguna dapat mengekspor data profil organisasi dan keragaan dalam format file.
- Proses export berjalan di background tanpa memblokir request.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5176

---

### 4.4 Menyusun webservice jumlah PNBP dan denda administrasi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyusun webservice jumlah PNBP dan denda administrasi sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan webservice data jumlah PNBP dan denda administrasi pada dashboard PSDKP Angka, dengan integrasi data dari file Excel ke format JSON.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/SanksiPnbpService.php`
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `public/bucket/s3_default/dashboard/pnbpDenda/data.json`
- `scripts/generate_pnbp_json.py`

**Perubahan Utama:**
- Penambahan service logic PNBP dan denda administrasi.
- Script Python `generate_pnbp_json.py` untuk konversi Excel ke JSON.
- Data JSON PNBP dan denda tersedia di bucket S3 default.

**Manfaat:**
- Dashboard menampilkan data PNBP dan denda administrasi secara real-time dari sumber terstruktur.
- Pipeline data Excel → JSON memudahkan pembaruan data berkala.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5184

---

### 4.5 Menyusun webservice jumlah pokmaswas

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyusun webservice jumlah pokmaswas sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan integrasi data jumlah pokmaswas (kelompok masyarakat pengawas) pada dashboard PSDKP Angka dari sumber Excel ke JSON.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `public/bucket/s3_default/dashboard/pokmaswas/data.json`
- `scripts/generate_pokmaswas_json.py`

**Perubahan Utama:**
- Penambahan logic pengambilan data pokmaswas pada service profil organisasi.
- Script Python `generate_pokmaswas_json.py` untuk konversi data Excel.
- File JSON data pokmaswas di bucket S3.

**Manfaat:**
- Dashboard menampilkan jumlah dan sebaran pokmaswas secara akurat.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5186

---

### 4.6 Memperbaharui webservice keragaan PSDKP

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice keragaan PSDKP sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah dilakukan restrukturisasi webservice keragaan PSDKP dengan pemindahan logic dari controller ke service layer, penambahan transformer, dan perbaikan struktur response API.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Http/Controllers/KeragaanPSDKPController.php`
- `Modules/DashboardPimpinan/Services/KeragaanPSDKPService.php`
- `Modules/DashboardPimpinan/Transformers/KeragaanPSDKP/KeragaanPSDKPResource.php`
- `Modules/DashboardPimpinan/Transformers/KeragaanPSDKP/SatkerResource.php`

**Perubahan Utama:**
- Ekstraksi business logic dari controller ke `KeragaanPSDKPService` (+147 baris).
- Penyederhanaan controller (dari 140 baris menjadi 6 baris).
- Penambahan transformer `KeragaanPSDKPResource` dan `SatkerResource`.
- Issue tracking: https://github.com/setditjen-psdkp/api-sip/issues/5208

**Manfaat:**
- Arsitektur lebih bersih (separation of concerns).
- Response API keragaan PSDKP terstruktur dan konsisten.
- Memudahkan pengujian dan pemeliharaan.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5191
- https://github.com/setditjen-psdkp/api-sip/issues/5208

---

### 4.7 Memperbaharui webservice chart pegawai berdasarkan jenis kelamin

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice chart pegawai berdasarkan jenis kelamin sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah diperbaiki data jenis kelamin pegawai yang hilang pada chart dashboard profil organisasi, dengan peningkatan proses sinkronisasi portal pegawai SIMPEG.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Gateway/Jobs/SIMPEG/SinkronDataPortalPegawai.php`
- `Modules/Gateway/Console/SIMPEG/SinkronPortalPegawaiCommand.php`

**Perubahan Utama:**
- Perbaikan mapping field jenis kelamin pada job sinkronisasi portal pegawai (+178 baris).
- Penyesuaian command sinkronisasi portal pegawai.

**Manfaat:**
- Chart pegawai berdasarkan jenis kelamin menampilkan data lengkap.
- Data ASN yang tidak memiliki informasi gender dapat diidentifikasi dan ditangani.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5193

---

### 4.8 Menyusun webservice pengawasan SDKP

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyusun webservice pengawasan SDKP sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan webservice data pengawasan SDKP (kelautan dan perikanan) pada dashboard PSDKP Angka, dengan integrasi data dari file Excel melalui script Python.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `scripts/generate_pengawasan_kelautan_json.py`
- `scripts/generate_pengawasan_perikanan_json.py`

**Perubahan Utama:**
- Refactor `PengawasanSdkpService` (+191 baris, -112 baris).
- Script Python untuk generate JSON data pengawasan kelautan dan perikanan.
- Integrasi data Excel ke format JSON untuk dashboard.

**Manfaat:**
- Dashboard menampilkan data pengawasan SDKP per sektor (kelautan & perikanan).
- Pipeline data terotomasi dari sumber Excel.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5194

---

### 4.9 Memperbaharui database kapal pengawas

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui database kapal pengawas sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah dilakukan pembaruan detail master data kapal pengawas, termasuk spesifikasi lengkap, foto kapal, dokumen surat tanda daftar, dan file data JSON terstruktur.

**Detail Perubahan**

**File yang Diubah:**
- `database/migrations/2026_05_12_122643_add_spesifikasi_lengkap_to_kapals_table.php`
- `database/seeders/Master/Kapal/KapalPengawasSeeder.php`
- `app/Http/Resources/KapalResource.php`
- `public/bucket/s3_default/KapalPengawas/` (foto & dokumen STD)
- `public/bucket/s3_default/KapalPengawas/data.json`

**Perubahan Utama:**
- Migration penambahan kolom `spesifikasi_lengkap` pada tabel kapal.
- Update seeder kapal pengawas (+135 baris).
- Penambahan aset foto kapal pengawas (HIU, ORCA, PAUS, TODAK, dll.).
- Penambahan dokumen Surat Tanda Daftar (STD) kapal.
- File JSON master data kapal pengawas (+4322 baris).

**Manfaat:**
- Profil kapal pengawas lengkap dengan spesifikasi, foto, dan dokumen resmi.
- Dashboard operasi armada memiliki data master yang komprehensif.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5203

---

### 4.10 Memperbaharui webservice dashboard operasi kapal pengawas

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice dashboard operasi kapal pengawas sebagai bagian dari pembaruan modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah diimplementasikan webservice dashboard operasi pengawasan kapal (POA), mencakup data penertiban rumpon dan rincian hasil tangkapan dari sumber Excel multi-tahun.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `public/bucket/s3_default/dashboard/operasiPengawasan/penertiban_rumpon/data.json`
- `public/bucket/s3_default/dashboard/operasiPengawasan/rincian_hasil_tangkapan/data.json`
- `scripts/DashboardPimpinan/generate_penertiban_rumpon_json.py`
- `scripts/DashboardPimpinan/generate_rincian_hasil_tangkapan_json.py`

**Perubahan Utama:**
- Refactor `OperasiArmadaService` (+100 baris).
- Integrasi data penertiban rumpon (2023–2025) dan rincian hasil tangkapan (2007–2026).
- Script Python untuk konversi Excel ke JSON.
- Reorganisasi script generator ke folder `scripts/DashboardPimpinan/`.

**Manfaat:**
- Dashboard operasi kapal menampilkan historis operasi pengawasan multi-tahun.
- Data penertiban rumpon dan hasil tangkapan tersedia untuk analisis tren.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5207

---

## 5. Memperbaharui Modul Penanganan Pelanggaran

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui modul Penanganan Pelanggaran, sebagai berikut:

### 5.1 Memperbaharui webservice filter penetapan sanksi administrasi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice filter penetapan sanksi administrasi sebagai bagian dari pembaruan modul Penanganan Pelanggaran.

**Deskripsi Pekerjaan**

Telah diperbaiki filter kategori dokumen pada menu Penetapan Sanksi Administrasi (SA) agar kategori `SPSUP` dan `SPSUK` dapat muncul pada daftar dan perhitungan overview.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/PenangananPelanggaran/Services/PenetapanSanksiService.php`
- `Modules/PenangananPelanggaran/Tests/Unit/PenetapanSanksiFilterTest.php`

**Perubahan Utama:**
- Perluasan filter kategori dari `SP1%/SP2%` menjadi `SP%` (mencakup SPSUP, SPSUK).
- Penambahan dukungan prefix `SCP%` pada query overview.
- Perluasan validasi `category_type` pada `giveViolation` (SP3, SPS, SCP).
- Unit test `PenetapanSanksiFilterTest` (76 baris).

**Manfaat:**
- Dokumen kategori SPSUP dan SPSUK kini tampil pada menu Penetapan SA.
- Perhitungan overview sanksi lebih akurat dan inklusif.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5249

---

## 6. KEGIATAN TAMBAHAN — Modul Master Data / OSS / KKPRL
*(belum tercatat di Weekly Report, ditemukan dari audit GitHub Mei 2026)*

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaharui webservice Modul Master Data, sebagai berikut:

### 6.1 Penyusunan fitur OSS dan KKPRL/Pemantauan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem penyusunan fitur OSS dan KKPRL/Pemantauan sebagai bagian dari pembaruan modul Master Data.

**Deskripsi Pekerjaan**

Telah diimplementasikan fitur integrasi OSS dan KKPRL/Pemantauan pada modul Master Data, mencakup controller, service, job sinkronisasi, dan transformer data.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Userman/Http/Controllers/Master/KKPRL/KKPRLController.php`
- `Modules/Userman/Services/Master/KKPRL/PerizinanService.php`
- `Modules/Userman/Services/Master/OSSPelakuUsahaService.php`
- `Modules/Userman/Jobs/Sync/SyncOssNibRelationJob.php`
- `Modules/Userman/Transformers/NKUResource.php`, `PelakuUsahaResource.php`

**Perubahan Utama:**
- Penambahan endpoint dan service KKPRL/Pemantauan.
- Integrasi sinkronisasi relasi NIB OSS.
- Penyesuaian transformer data pelaku usaha dan NKU.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5097

---

### 6.2 Filter dan export data Master Data OSS

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan filter dan export data Master Data OSS sebagai bagian dari pembaruan modul Master Data.

**Deskripsi Pekerjaan**

Telah ditambahkan fitur filter dan export data OSS (NKU, Pelaku Usaha, Perizinan, Sinkron NIB) pada modul Master Data.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Userman/Services/Master/OSSPelakuUsahaService.php`
- `Modules/Userman/Exports/Master/OSSNKUExport.php`, `OSSPelakuUsahaExport.php`, `OSSPerizinanExport.php`, `OSSSinkronNIBExport.php`
- `Modules/Userman/Http/Controllers/OSSController.php`

**Perubahan Utama:**
- Refactor service OSS Pelaku Usaha (+327 baris).
- Penambahan export class untuk NKU, Pelaku Usaha, Perizinan, dan Sinkron NIB.
- Endpoint filter dan export pada routes master.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5102

---

### 6.3 Sinkron NIB Master Data dan validasi objek pengawasan

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan sinkron NIB Master Data dan validasi objek pengawasan sebagai bagian dari pembaruan modul Master Data.

**Deskripsi Pekerjaan**

Telah diperbaiki proses sinkronisasi NIB pada Master Data dan validasi NIB pada import objek pengawasan WasRisk.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Userman/Jobs/Sync/SyncOssNibRelationJob.php`
- `Modules/Userman/Services/Sync/SyncMasterService.php`
- `app/Imports/ObjekPengawasanImport.php`
- `app/Services/PengawasanPerizinanBerusaha/DashboardPerizinanBerusahaService.php`

**Perubahan Utama:**
- Perbaikan job sinkron relasi NIB OSS (PR #5110).
- Perbaikan validasi NIB dan jumlah objek dashboard (PR #5124).
- Penambahan parameter `search` pada list/export Sinkron NIB (PR #5250, #5253, #5255).
- Feature test `OSSSinkronNIBExportTest` untuk validasi threshold async export >1000 baris.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5110
- https://github.com/setditjen-psdkp/api-sip/pull/5124
- https://github.com/setditjen-psdkp/api-sip/pull/5250
- https://github.com/setditjen-psdkp/api-sip/pull/5253
- https://github.com/setditjen-psdkp/api-sip/pull/5255

---

### 6.4 Sinkron laporan tahunan KKPRL dan download file laporan (bypass CORS)

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan sinkron laporan tahunan KKPRL dan download file laporan (bypass CORS) sebagai bagian dari pembaruan modul Master Data.

**Deskripsi Pekerjaan**

Telah diimplementasikan sinkronisasi file laporan fisik KKPRL (PDF/dokumen) ke storage lokal untuk mengatasi masalah CORS saat frontend mengakses file dari domain SEAMAP (`doc-sea.kkp.go.id`).

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Userman/Database/Migrations/2026_05_26_000001_create_kkprl_laporan_files_table.php`
- `Modules/Userman/Entities/KKPRL/LaporanFile.php`, `LaporanTahunan.php`
- `Modules/Userman/Jobs/Sync/KKPRL/SyncKKPRLReportJob.php`, `SyncKKPRLReportFilesJob.php`
- `Modules/Gateway/Services/SEAMAP/LaporanTahunanService.php`
- `Modules/Userman/Transformers/LaporanKKPRLResource.php`
- `Modules/PengawasanPerizinanBerusaha/Transformers/SDK/PemantauanDetailResource.php`
- `tests/Unit/SyncKKPRLReportFilesJobTest.php`

**Perubahan Utama:**
- Tabel pivot `kkprl_laporan_files` untuk tracking status download per field file.
- Background job `SyncKKPRLReportFilesJob` untuk bulk download file pending.
- `Bus::chain`: `SyncKKPRLReportJob` → `SyncKKPRLReportFilesJob`.
- `LaporanTahunan::getFileUrl()` — otomatis serve URL lokal jika file sudah terunduh, fallback ke SEAMAP.
- IP fallback untuk URL lama `10.10.10.6` → `backend-sea.kkp.go.id` → `doc-sea.kkp.go.id`.
- Unit test: 11 test PASS (100% coverage logika sinkronisasi).
- Perbaikan lanjutan: sanitasi filename, absolute domain URL, validasi download pemantauan (PR #5258–#5267).

**Manfaat:**
- Frontend tidak lagi terkena error CORS saat memuat file laporan KKPRL.
- File laporan tersedia di storage lokal PSDKP dengan tracking status.
- Mekanisme idempotent — file yang sudah terunduh tidak di-download ulang.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5117
- https://github.com/setditjen-psdkp/api-sip/pull/5257
- https://github.com/setditjen-psdkp/api-sip/pull/5261

---

## 7. KEGIATAN TAMBAHAN — Refactor RBAC

### 7.1 Refactor Role-Based Access Control (RBAC)

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan refactor Role-Based Access Control (RBAC) sebagai bagian dari pembaruan modul RBAC.

**Deskripsi Pekerjaan**

Telah dilakukan refactor menyeluruh pada sistem RBAC, termasuk seeder akun, permission model, dan service akses modul.

**Detail Perubahan**

**File yang Diubah:**
- `app/Models/Permission.php`
- `app/Traits/HasRbacSeeder.php`
- `app/Services/IzinAksesUserModulService.php`, `KewenanganModulAccessService.php`, `PeranModulAccessService.php`
- `database/seeders/UserManagement/RBAC/SetupGoldenAccessSeeder.php`, `UpdateRolePermissionSeeder.php`
- `docs/RBAC_ARCHITECTURE_GUIDE.md`
- `tests/Unit/RBACPermissionTest.php`

**Perubahan Utama:**
- Penyederhanaan seeder akun di seluruh modul (Agenda Pimpinan, Operasi Kapal, Penanganan Pelanggaran, Userman).
- Penambahan trait `HasRbacSeeder` untuk standardisasi seeding RBAC.
- Dokumentasi arsitektur RBAC (`RBAC_ARCHITECTURE_GUIDE.md`).
- Unit test RBAC permission (119 baris).

**Manfaat:**
- Manajemen permission lebih terstruktur dan mudah dipelihara.
- Seeder RBAC konsisten di seluruh modul.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5126

---

## 8. KEGIATAN TAMBAHAN — WasRisk (lanjutan)

### 8.1 Perbaikan dashboard penjadwalan dan refactor pertanyaan inspeksi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem perbaikan dashboard penjadwalan dan refactor pertanyaan inspeksi sebagai bagian dari pembaruan modul RBAC.

**Deskripsi Pekerjaan**

Telah diperbaiki perhitungan dashboard penjadwalan inspeksi dan direfaktor service pertanyaan inspeksi pengawasan beserta penambahan source type pada korespondensi.

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/DashboardPerizinanBerusahaService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanPbUmkuService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanSelfDeclareService.php`
- `Modules/Userman/Transformers/Master/PORTAL/DokumenSuratResource.php`

**Perubahan Utama:**
- Status `BelumUploadST` dipindahkan ke kategori "Sedang Inspeksi Lapangan" pada dashboard (PR #5127).
- Refactor type-hinting pada service pertanyaan inspeksi dan penambahan source type korespondensi (PR #5136).

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5127
- https://github.com/setditjen-psdkp/api-sip/pull/5136

---

### 8.2 Optimasi performa N+1 query dan race condition pertanyaan inspeksi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan optimasi performa N+1 query dan race condition pertanyaan inspeksi sebagai bagian dari pembaruan modul RBAC.

**Deskripsi Pekerjaan**

Telah dilakukan optimasi performa inspeksi lapangan dengan mengatasi N+1 query (~200+ query → <25 query per request) dan race condition pada kalkulasi skor kepatuhan teknis.

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanPbUmkuService.php`
- `app/Services/PengawasanPerizinanBerusaha/PertanyaanSelfDeclareService.php`
- `app/Models/PengawasanPerizinanBerusaha/InspeksiLapangan/PertanyaanKepatuhanTeknis.php`
- `tests/Feature/PengawasanPerizinanBerusaha/PertanyaanKepatuhanTeknisServiceTest.php`

**Perubahan Utama:**
- Batch retrieval dengan eager loading manual (PR #5219).
- In-memory tree processing menggunakan Laravel Collections.
- Bottom-up score calculation yang atomic.
- Sanitasi UTF-8 pada response pertanyaan (PR #5222).
- Relasi `subPertanyaan()` sebagai alias `child()`.

**Manfaat:**
- Loading halaman inspeksi jauh lebih cepat.
- Background job generate dokumen lebih ringan dan stabil.
- Menghilangkan corrupted scoring pada laporan kepatuhan teknis.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5219
- https://github.com/setditjen-psdkp/api-sip/pull/5222

---

### 8.3 Fix generate dokumen BAP saat perusahaan "Tidak Ada"

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan fix generate dokumen BAP saat perusahaan "Tidak Ada" sebagai bagian dari pembaruan modul RBAC.

**Deskripsi Pekerjaan**

Telah diperbaiki regresi di mana `generateDokumenHasilPengawasan()` tidak dipanggil saat pengawas menyimpan identitas penanggung jawab dengan `status_perusahaan = "Tidak Ada"`, sehingga dokumen PDF BAP tidak terbuat dan notifikasi tidak terkirim.

**Detail Perubahan**

**File yang Diubah:**
- `app/Services/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanService.php`
- `tests/Unit/PengawasanPerizinanBerusaha/BeritaAcaraPemeriksaanServiceTest.php`

**Perubahan Utama:**
- Perluasan kondisi trigger generate dokumen: `tab === '3'` ATAU `(tab === 'penanggung-jawab' && status_perusahaan === 'Tidak Ada')`.
- Unit test regresi: 2 skenario (Tidak Ada → generate dipanggil; Ada → tidak dipanggil dari tab PJ).

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5251

---

## 9. KEGIATAN TAMBAHAN — PSDKP Angka (lanjutan)

### 9.1 Sinkron data pegawai, PJLP, dan perbaikan profil organisasi

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan sinkron data pegawai, PJLP, dan perbaikan profil organisasi sebagai bagian dari pembaruan modul RBAC.

**Deskripsi Pekerjaan**

Telah dilakukan serangkaian perbaikan sinkronisasi data pegawai (foto, PJLP, unit kerja kosong) dan penyesuaian API profil organisasi pada dashboard PSDKP Angka.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/Gateway/Jobs/SIMPEG/SinkronFotoPegawaiJob.php`, `SinkronDataPortalPegawai.php`
- `Modules/Gateway/Console/SIMPEG/SinkronPjlpCommand.php`, `SinkronPortalPegawaiCommand.php`
- `Modules/Gateway/Imports/SIMPEG/PjlpImport.php`
- `Modules/DashboardPimpinan/Services/ProfileOrganisasiService.php`
- `Modules/TanyaData/Exports/PegawaiExport.php`
- `app/Services/PegawaiService.php`

**Perubahan Utama:**
- Job sinkron foto pegawai dari portal SIMPEG (PR #5150).
- Sinkron data PJLP dan penyesuaian API main card (PR #5155).
- Perbaikan sinkron pegawai unit kerja kosong dan export pegawai (PR #5162).
- Perbaikan data piramida usia kosong (PR #5175).
- Perbaikan issue sebaran satker (PR #5214).

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5150
- https://github.com/setditjen-psdkp/api-sip/pull/5155
- https://github.com/setditjen-psdkp/api-sip/pull/5162
- https://github.com/setditjen-psdkp/api-sip/pull/5175
- https://github.com/setditjen-psdkp/api-sip/pull/5214

---

### 9.2 Perbaikan dashboard operasi armada dan keragaan PSDKP

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem perbaikan dashboard operasi armada dan keragaan PSDKP sebagai bagian dari pembaruan modul RBAC.

**Deskripsi Pekerjaan**

Telah diperbaiki rentang tahun menu operasi armada, data SKAT/rumpon/hari operasi/kapal diperiksa, serta peningkatan sebaran satker, kapal, pegawai, dan heatmap keragaan.

**Detail Perubahan**

**File yang Diubah:**
- `Modules/DashboardPimpinan/Services/OperasiArmadaService.php`
- `Modules/DashboardPimpinan/Services/KeragaanPSDKPService.php`
- `Modules/DashboardPimpinan/Services/PengawasanSdkpService.php`
- `Modules/DashboardPimpinan/Transformers/KeragaanPSDKP/SatkerResource.php`
- `public/bucket/s3_default/dashboard/operasiPengawasan/hari_operasi_skat_kapal_diperiksa/data.json`
- `scripts/DashboardPimpinan/generate_hari_operasi_skat_kapal_diperiksa_json.py`
- `database/seeders/Master/Kapal/KapalPengawasSeeder.php`

**Perubahan Utama:**
- Reset dummy dan perbaikan rentang tahun operasi armada (PR #5215).
- Data SKAT, hari operasi, kapal diperiksa dari Excel → JSON (PR #5227).
- Peningkatan sebaran satker, kapal, pegawai, dan heatmap (PR #5218).
- Update status dan dimensi kapal pengawas dari Excel 2026 (PR #5252).
- Perbaikan trend count dashboard armada (PR #5254).

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5215
- https://github.com/setditjen-psdkp/api-sip/pull/5216
- https://github.com/setditjen-psdkp/api-sip/pull/5218
- https://github.com/setditjen-psdkp/api-sip/pull/5227
- https://github.com/setditjen-psdkp/api-sip/pull/5252
- https://github.com/setditjen-psdkp/api-sip/pull/5254

---

## 10. KEGIATAN TAMBAHAN — Sentry Hotfixes (PR Open, dibuat Mei 2026)

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem menyiapkan perbaikan isu yang dilaporkan Sentry, sebagai berikut:

### 10.1 Optimasi performa query dan perbaikan error handling

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan optimasi performa query dan perbaikan error handling sebagai bagian dari pembaruan modul Monitoring Sentry.

**Deskripsi Pekerjaan**

Telah disiapkan serangkaian hotfix untuk isu performa (N+1 query, slow DB query) dan error handling (TypeError, ConnectionException) yang dilaporkan Sentry.

**Detail Perubahan**

| PR | Judul | Status | Modul |
|----|-------|--------|-------|
| #5238 | Resolve N+1 queries in SimpanDataSIUP job | Open | Gateway/SILAT |
| #5239 | Optimize TandaiJenisSuratOpdlJob query performance | Open | Gateway/Korespondensi |
| #5240 | Resolve TypeError in SIMPEG sync jobs | Open | Gateway/Userman |
| #5241 | Resolve TypeError in input-pengawas console command | Open | WasRisk |
| #5242 | Add composite index to cc_operational_vessels_per_wpp | Open | Database |
| #5243 | Optimize user search query using nested where clauses | Open | User Management |
| #5244 | Eliminate N+1 queries in UserResourceIndex | Open | User Management |
| #5245 | Fix N+1 query on pelaku usaha projects retrieval | Open | Gateway/OSS |
| #5246 | Handle connection/timeout errors in sendEmailNotification | Open | Mail |
| #5247 | Handle connection timeouts in KejaksaanService | Open | Gateway/Kejaksaan |

**Perubahan Utama (contoh):**
- **#5238**: Static cache wilayah (provinsi→kota→kecamatan→kelurahan) pada `SimpanDataSIUP`.
- **#5239**: Double-update strategy OPDL/NON-OPDL untuk menghindari full-table scan regex.
- **#5240**: Perbaikan parameter `createAkunPegawai` — kirim model instance, bukan array/string NIP.
- **#5244**: Static per-request cache lookup `Kewenangan` pada UserResource.
- **#5245**: Eager loading relasi proyek OSS pada `PencarianPerizinanBerusahaService`.
- **#5246**: Timeout 10 detik + `catch (\Throwable)` pada `sendEmailNotification`.
- **#5247**: Log timeout Kejaksaan sebagai `warning` (bukan `error`) untuk mengurangi noise Sentry.

**Dokumentasi**
- https://github.com/setditjen-psdkp/api-sip/pull/5238
- https://github.com/setditjen-psdkp/api-sip/pull/5239
- https://github.com/setditjen-psdkp/api-sip/pull/5240
- https://github.com/setditjen-psdkp/api-sip/pull/5241
- https://github.com/setditjen-psdkp/api-sip/pull/5242
- https://github.com/setditjen-psdkp/api-sip/pull/5243
- https://github.com/setditjen-psdkp/api-sip/pull/5244
- https://github.com/setditjen-psdkp/api-sip/pull/5245
- https://github.com/setditjen-psdkp/api-sip/pull/5246
- https://github.com/setditjen-psdkp/api-sip/pull/5247

---

## RINGKASAN KEGIATAN

| Sumber | Jumlah | Keterangan |
|--------|--------|------------|
| Weekly Report (W1–W3) | 26 PR + 1 commit + 1 issue | Tercatat di logbook |
| Audit GitHub tambahan | +48 PR merged/closed | Belum di weekly report |
| Sentry hotfixes (open) | +10 PR | Dibuat Mei, belum merged |
| **Total GitHub Mei 2026** | **~129 PR** | Author: lutfiihsan |

| Periode | Jumlah PR/Issue | Modul Utama |
|---------|-----------------|-------------|
| W1 (4–9 Mei) | 16 PR + 1 commit | WasRisk, Userman, Dashboard Pimpinan |
| W2 (11–15 Mei) | 3 PR + 1 issue | Korespondensi, Dashboard Pimpinan |
| W3 (18–22 Mei) | 7 PR | WasRisk (hotfix), Korespondensi, Penanganan Pelanggaran |
| W4+ & tambahan | ~48 PR merged + 10 PR open | Master Data, KKPRL, RBAC, Sentry |

**Modul yang disentuh:**
1. WasRisk (Pengawasan Perizinan Berusaha) — 16+ PR
2. Dashboard Pimpinan / PSDKP Angka — 18+ PR + 1 issue
3. Korespondensi (Userman) — 5+ PR
4. Master Data / OSS / KKPRL — 12+ PR
5. User Management / RBAC — 3+ PR
6. Gateway (SILAT, SIMPEG, Kejaksaan) — 8+ PR
7. Penanganan Pelanggaran — 1 PR
8. Sentry Hotfixes — 10 PR (open)