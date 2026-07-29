# DETAIL LAPORAN KEGIATAN GITHUB — LUTFI IHSAN
## Bulan Juli 2026 (Periode Weekly Report)

Sumber data: `input/202607/weekly_report.md`
Repo: https://github.com/systemcerdas/sipservice

---

## 1. Modul PSDKP Angka — API & Legenda Satker

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem mengembangkan dan memperbaiki Modul PSDKP Angka pada repositori sipservice, mencakup legenda satker, API POKMASWAS, area pengawasan, WPPNRI, dan detail armada.

### 1.1 Pembaruan Legenda Satker dan API POKMASWAS

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbarui tampilan legenda satker dan endpoint API POKMASWAS sebagai bagian dari penguatan Modul PSDKP Angka pada sistem sipservice.

**Deskripsi Pekerjaan**

Telah dilakukan pembaruan klasifikasi dan tampilan legenda satker pada Modul PSDKP Angka serta penyesuaian endpoint API POKMASWAS. Pada pembaruan ini turut dilakukan penghapusan metadata statis dari file GeoJSON sehingga data yang disajikan bersifat dinamis dan selalu sinkron dengan sumber data terkini.

**Detail Perubahan**

**Perubahan Utama:**
- Pembaruan klasifikasi legenda satker pada tampilan peta pengawasan.
- Pembaruan endpoint API POKMASWAS dengan penghapusan meta statis dari GeoJSON.

**Manfaat:**
- Data satker dan POKMASWAS yang ditampilkan lebih akurat dan real-time, mengurangi potensi ketidaksesuaian antara data peta dan data backend.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/1
- https://github.com/systemcerdas/sipservice/pull/2

---

### 1.2 Implementasi Area Pengawasan dan WPPNRI

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem mengimplementasikan endpoint area pengawasan dan Wilayah Pengelolaan Perikanan Negara Republik Indonesia (WPPNRI) sebagai bagian dari Modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi endpoint area pengawasan dan WPPNRI guna menyediakan data spasial pengawasan yang terstruktur. Dalam proses ini juga dilakukan penyederhanaan layer armada dengan menghapus layer kapal pengawas pusat dan UPT agar tampilan data lebih ringkas dan tidak redundan.

**Detail Perubahan**

**Perubahan Utama:**
- Implementasi endpoint area pengawasan dan data spasial WPPNRI.
- Penghapusan layer kapal-pengawas-pusat dan kapal-pengawas-upt dari layerArmada.

**Manfaat:**
- Data area pengawasan dan WPPNRI tersedia secara terstruktur untuk keperluan pelaporan dan visualisasi peta pengawasan laut, dengan tampilan armada yang lebih bersih.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/3
- https://github.com/systemcerdas/sipservice/pull/4

---

### 1.3 Implementasi Detail Armada, Realisasi Anggaran, dan PNBP

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem mengimplementasikan API detail armada pengawasan serta melakukan serangkaian peningkatan terhadap data realisasi anggaran dan Penerimaan Negara Bukan Pajak (PNBP) pada Modul PSDKP Angka.

**Deskripsi Pekerjaan**

Telah dilakukan implementasi endpoint detail armada kapal pengawasan pada Modul PSDKP Angka. Selain itu, dilakukan pula penyempurnaan logika pengolahan data realisasi anggaran dan PNBP agar nilai yang ditampilkan lebih akurat, lengkap, dan sesuai dengan data operasional di lapangan.

**Detail Perubahan**

**Perubahan Utama:**
- Implementasi endpoint detailArmada untuk data kapal pengawasan.
- Peningkatan akurasi kalkulasi data realisasi anggaran.
- Penyempurnaan pengolahan data PNBP pada modul pelaporan.

**Manfaat:**
- Data armada pengawasan, realisasi anggaran, dan PNBP tersedia secara detail dan akurat untuk mendukung pelaporan kinerja PSDKP kepada pimpinan.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/5
- https://github.com/systemcerdas/sipservice/pull/6
- https://github.com/systemcerdas/sipservice/pull/7

---

## 2. Modul GeoJSON dan Dashboard Pimpinan

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem melakukan pembaruan pada data GeoJSON dan Dashboard Pimpinan, mencakup simplifikasi atribut, label WPPNRI, sinkronisasi data kewenangan, serta penyesuaian struktur response API.

### 2.1 Simplifikasi GeoJSON POKMASWAS dan Label WPPNRI

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menyederhanakan atribut GeoJSON POKMASWAS dan menambahkan dukungan parameter label pada endpoint WPPNRI guna meningkatkan performa rendering peta.

**Deskripsi Pekerjaan**

Telah dilakukan simplifikasi atribut pada file GeoJSON POKMASWAS untuk mengurangi ukuran payload yang dikirimkan ke klien. Selain itu, diimplementasikan pula dukungan parameter label pada endpoint WPPNRI menggunakan simplified GeoJSON, sehingga tampilan informasi pada peta menjadi lebih informatif dan terarah.

**Detail Perubahan**

**Perubahan Utama:**
- Penyederhanaan atribut pada file GeoJSON POKMASWAS.
- Implementasi dukungan parameter label WPPNRI dengan simplified GeoJSON.

**Manfaat:**
- Ukuran file GeoJSON lebih kecil sehingga performa rendering peta meningkat. Parameter label WPPNRI memungkinkan tampilan informasi yang lebih informatif bagi pengguna.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/8
- https://github.com/systemcerdas/sipservice/pull/9

---

### 2.2 Pembaruan Dashboard Pimpinan — PNBP, Kewenangan, dan Realisasi Anggaran

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan serangkaian perbaikan dan pembaruan pada Dashboard Pimpinan, meliputi parameter perbandingan PNBP, data realisasi anggaran, sinkronisasi data kewenangan dari lingkungan produksi, serta penghapusan filter tanggal yang tidak relevan.

**Deskripsi Pekerjaan**

Telah dilakukan perbaikan parameter perbandingan PNBP menjadi mode tren, peningkatan akurasi data realisasi anggaran, dan sinkronisasi data kewenangan dari lingkungan produksi ke lingkungan pengembangan. Selain itu, dihapus pula filter tanggal yang tidak logis pada data kewenangan aktif agar data yang ditampilkan pada Dashboard Pimpinan lebih representatif.

**Detail Perubahan**

**Perubahan Utama:**
- Perubahan parameter perbandingan PNBP ke mode tren pada dashboard.
- Peningkatan akurasi data realisasi anggaran.
- Sinkronisasi data kewenangan dari lingkungan produksi.
- Penghapusan filter tanggal yang tidak logis untuk data kewenangan aktif.

**Manfaat:**
- Dashboard Pimpinan menampilkan data kewenangan, PNBP, dan realisasi anggaran yang lebih akurat dan konsisten, sehingga informasi yang diterima pimpinan dapat dijadikan dasar pengambilan keputusan yang lebih tepat.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/10
- https://github.com/systemcerdas/sipservice/pull/11
- https://github.com/systemcerdas/sipservice/pull/12
- https://github.com/systemcerdas/sipservice/pull/13
- https://github.com/systemcerdas/sipservice/pull/14

---

### 2.3 Penambahan Field Persentase pada Response API Dashboard

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem menambahkan field persentase pada berbagai response API Dashboard Pimpinan dan melakukan penyesuaian struktur response agar selaras dengan kebutuhan tampilan di sisi frontend.

**Deskripsi Pekerjaan**

Telah dilakukan penambahan field persentase dan persentaseDisplay pada response API tren, PNBP, dan pagu Dashboard Pimpinan. Selain itu, dilakukan pula penyesuaian struktur response RealisasiAnggaran, perbaikan logika perbandingan tahun historis, dan penanganan override data polsus/ppns pada lingkungan non-produksi agar pengujian dapat berjalan dengan data yang representatif.

**Detail Perubahan**

**Perubahan Utama:**
- Penambahan field persentase dan persentaseDisplay pada response API tren PSDKP Angka.
- Penyesuaian struktur response API RealisasiAnggaran.
- Penambahan field persentase pada data PNBP dan pagu pimpinan.
- Perbaikan logika perbandingan tahun historis pada legacy comparison.
- Override data polsus dan ppns dengan demo JSON di lingkungan non-produksi.

**Manfaat:**
- Frontend dapat menampilkan indikator persentase pencapaian PNBP dan realisasi anggaran secara langsung tanpa perlu melakukan kalkulasi di sisi klien, sehingga konsistensi tampilan lebih terjaga.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/15
- https://github.com/systemcerdas/sipservice/pull/16
- https://github.com/systemcerdas/sipservice/pull/17
- https://github.com/systemcerdas/sipservice/pull/18
- https://github.com/systemcerdas/sipservice/pull/19
- https://github.com/systemcerdas/sipservice/pull/20
- https://github.com/systemcerdas/sipservice/pull/21

---

### 2.4 Perbaikan Flag Kapal Pusat dan Pembaruan Konfigurasi Repository

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki logika flag is_pusat dan flag kapal pengawas pusat pada Modul PSDKP Angka, serta memperbarui konfigurasi .gitignore untuk mencegah file data sensitif masuk ke dalam repository.

**Deskripsi Pekerjaan**

Telah dilakukan perbaikan logika flag is_pusat pada filter data Modul PSDKP Angka, sehingga pemisahan data kapal pengawas pusat dan UPT dapat berjalan dengan benar. Pembaruan file .gitignore juga dilakukan untuk memastikan file-file yang bersifat lokal dan sensitif tidak ikut ter-commit ke dalam repository.

**Detail Perubahan**

**Perubahan Utama:**
- Perbaikan logika filter flag is_pusat pada endpoint Modul PSDKP Angka.
- Perbaikan flag kapal pengawas pusat pada layer data armada.
- Pembaruan file .gitignore untuk mengecualikan file data lokal.

**Manfaat:**
- Filter data berdasarkan flag pusat berjalan dengan benar sehingga data kapal pusat dan UPT terpisah secara tepat. Pembaruan .gitignore menjaga keamanan file sensitif agar tidak tersimpan di repository publik.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/22
- https://github.com/systemcerdas/sipservice/pull/23

---

## 3. Modul Realisasi Anggaran dan Statistik Pengawasan Laut

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem mengimplementasikan service pengelolaan realisasi anggaran dan menambahkan dataset awal untuk dashboard statistik pengawasan laut.

### 3.1 Implementasi RealisasiAnggaranService dan Dataset Pengawasan Laut

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem membuat RealisasiAnggaranService sebagai komponen terpusat untuk memproses dan mengagregasi data pagu anggaran, serta menambahkan dataset awal statistik dashboard pengawasan laut.

**Deskripsi Pekerjaan**

Telah dilakukan perbaikan logika data pagu anggaran dan diimplementasikan RealisasiAnggaranService sebagai service baru yang bertanggung jawab atas agregasi dan pengolahan data realisasi anggaran secara terpusat. Selain itu, ditambahkan pula dataset awal statistik pengawasan laut sebagai fondasi data pada dashboard statistik PSDKP.

**Detail Perubahan**

**Perubahan Utama:**
- Perbaikan logika dan kalkulasi data pagu anggaran.
- Implementasi RealisasiAnggaranService untuk agregasi realisasi anggaran.
- Penambahan dataset awal statistik dashboard pengawasan laut.

**Manfaat:**
- Agregasi data realisasi anggaran menjadi terpusat dalam satu service, memudahkan pemeliharaan dan meningkatkan akurasi kalkulasi. Dashboard pengawasan laut memiliki data awal yang siap ditampilkan kepada pimpinan.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/24
- https://github.com/systemcerdas/sipservice/pull/25
- https://github.com/systemcerdas/sipservice/pull/26

---

## 4. Dokumentasi API dan Infrastruktur Sistem

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbarui dokumentasi API sipservice, mengimplementasikan konfigurasi CORS, dan mendokumentasikan arsitektur Decoupled SSE.

### 4.1 Pembaruan Dokumentasi API dan Konfigurasi CORS

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem melakukan pembaruan dokumentasi API sipservice secara menyeluruh dan mengimplementasikan konfigurasi CORS dengan daftar allowed origins beserta mekanisme pattern matching untuk mendukung akses multi-origin secara aman.

**Deskripsi Pekerjaan**

Telah dilakukan pembaruan dokumentasi API sipservice mencakup perubahan endpoint dan parameter terbaru. Ditambahkan pula dokumentasi untuk arsitektur Decoupled SSE (Server-Sent Events) guna memudahkan pemahaman alur data real-time pada sistem. Implementasi konfigurasi CORS dengan daftar origin yang diizinkan dan pattern matching turut diselesaikan untuk memungkinkan akses aman dari berbagai domain yang telah disetujui.

**Detail Perubahan**

**Perubahan Utama:**
- Pembaruan umum dokumentasi API sipservice.
- Penambahan dokumentasi arsitektur Decoupled SSE.
- Implementasi konfigurasi CORS dengan allowed origins dan pattern matching.

**Manfaat:**
- Dokumentasi API yang lengkap dan mutakhir memudahkan integrasi oleh tim frontend maupun stakeholder teknis lainnya. Konfigurasi CORS yang tepat memungkinkan akses lintas domain yang aman sesuai kebijakan keamanan sistem.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/27
- https://github.com/systemcerdas/sipservice/pull/28
- https://github.com/systemcerdas/sipservice/pull/30

---

## 5. Modul Kepatuhan Teknis — Perbaikan Logika Skor CBIB dan CPIB

Pada kegiatan ini Tenaga Teknis Implementasi Logika Sistem memperbaiki logika perhitungan skor CBIB dan CPIB pada Modul Kepatuhan Teknis dan menambahkan script helper untuk koreksi data historis.

### 5.1 Perbaikan Logika Skor CBIB dan CPIB pada Kepatuhan Teknis

**Prolog**

Pada sub-kegiatan ini, Tenaga Teknis Implementasi Logika Sistem memperbaiki logika perhitungan skor Cara Budidaya Ikan yang Baik (CBIB) dan Cara Pembenihan Ikan yang Baik (CPIB) pada proses penyimpanan data Kepatuhan Teknis, serta menyediakan script utilitas untuk koreksi data historis yang terdampak.

**Deskripsi Pekerjaan**

Telah dilakukan identifikasi dan perbaikan bug pada logika kalkulasi skor CBIB dan CPIB yang terjadi saat proses penyimpanan data Kepatuhan Teknis. Selain perbaikan logika utama, ditambahkan pula script helper sebagai alat bantu untuk melakukan koreksi terhadap data historis yang nilainya tidak valid akibat bug sebelumnya, sehingga integritas data kepatuhan teknis dapat dipulihkan.

**Detail Perubahan**

**Perubahan Utama:**
- Perbaikan logika kalkulasi skor CBIB dan CPIB pada proses simpan Kepatuhan Teknis.
- Penambahan script helper chore untuk koreksi data historis yang terdampak bug skor.

**Manfaat:**
- Skor CBIB dan CPIB dihitung dengan benar sehingga validitas data kepatuhan teknis terjaga. Script helper memungkinkan koreksi data historis secara sistematis tanpa intervensi manual yang berisiko.

**Dokumentasi**
- https://github.com/systemcerdas/sipservice/pull/29
- https://github.com/systemcerdas/sipservice/pull/31
