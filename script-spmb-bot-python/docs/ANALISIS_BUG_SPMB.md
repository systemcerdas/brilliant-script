# Analisis Bug Sistem Pendaftaran SPMB Kabupaten Bogor

Dokumen ini merangkum hasil *reverse engineering* dan audit otomatis terhadap *endpoint* API Registrasi dan Login SPMB Kabupaten Bogor (`https://spmb.bogorkab.go.id/`), berdasarkan kendala di lapangan di mana orang tua siswa sering terjebak pada error **"Data diri sudah ada"** namun tidak bisa login karena **"Password Salah"**.

## Kasus / Keluhan Utama
Pendaftar (orang tua murid) mencoba melakukan **Registrasi Akun Baru** secara mandiri di website SPMB. Namun sistem menolak dengan pesan error *"Data diri sudah ada sebelumnya, silahkan hubungi Sekolah Asal atau Sekolah Tujuan untuk mendapatkan akun."*.
Sebagai respons, orang tua mencoba login menggunakan password yang mereka yakini benar. Sistem menolak dengan pesan *"Maaf, Username/Password Salah!"*.

Hal ini membuat pendaftar bingung karena mereka merasa belum pernah mendaftar, apalagi siswa berasal dari Bimba (Non-Dapodik formal), sehingga kecil kemungkinan datanya ditarik otomatis oleh sistem.

---

## Metodologi Pengujian
Pengujian dilakukan menggunakan bot Playwright (Python) yang mencegat *(intercept)* dan mendekripsi *payload* JWT AES-256 dari API SPMB untuk melihat respons asli dari server, karena UI web SPMB sering mem-blokir atau menyembunyikan pesan aslinya. 

Ada 3 skenario *dummy data* yang diuji ke dalam endpoint `/v2/ppdb-service/akun/akunRegistrasi`:

### Tes 1: NIK Kasus Asli (Valid & Sesuai KTP)
*   **Input**: NIK anak yang dikeluhkan *"nyangkut"*.
*   **Respons Registrasi**: `Data diri sudah ada sebelumnya, silahkan hubungi Sekolah Asal atau Sekolah Tujuan untuk mendapatkan akun.`
*   **Respons Login**: `Maaf, Username/Password Salah.!`

### Tes 2: NIK Palsu / Acak (Tidak Valid)
*   **Input**: NIK 16 digit yang dikarang sembarangan (contoh: `3201206605199999`) dengan nama asal.
*   **Respons Registrasi**: `Data tidak sesuai dengan Dukcapil (NIK)`
*   **Respons Login**: (Tidak relevan, karena gagal registrasi).
*   **Temuan Awal**: API SPMB secara aktif melakukan pengecekan NIK dan Nama secara *real-time* ke server API Dinas Kependudukan dan Pencatatan Sipil (Dukcapil).

### Tes 3: NIK Valid Milik Orang Lain (Fresh)
*   **Input**: NIK asli (diambil dari sampel KTP) namun milik orang dewasa dari provinsi lain yang **belum pernah** didaftarkan ke SPMB Bogor.
*   **Respons Registrasi 1**: `Success` (Pendaftaran diterima dan NIK masuk ke database).
*   **Respons Login 1**: `Maaf, Username/Password Salah.!` (Gagal login padahal baru saja sukses mendaftar dengan password tersebut).
*   **Respons Registrasi 2 (Re-try)**: `Data diri sudah ada sebelumnya, silahkan hubungi Sekolah Asal...`
*   **Temuan Akhir**: Sistem berhasil memverifikasi NIK baru lewat Dukcapil dan merekamnya di database. Namun, sistem gagal mengaktifkan akun tersebut secara utuh, sehingga tidak bisa di-login, tapi saat mencoba daftar lagi, NIK tersebut sudah *locked*.

---

## Kesimpulan Teknis (Root Cause)

Berdasarkan ketiga tes di atas, masalah yang dialami pendaftar adalah **100% bug pada sistem *backend* SPMB**, dengan skenario berikut:

1. **Sinkronisasi Dukcapil Bekerja:** Sistem SPMB sudah terintegrasi dengan baik dengan Dukcapil. Ini berarti NIK anak tersebut **benar-benar valid** dan memang sudah terkunci/tersimpan di dalam database SPMB.
2. **Kecacatan Proses Registrasi Publik:** Saat pendaftar melakukan pendaftaran pertama kalinya, data mereka (NIK & Nama) *berhasil* masuk ke dalam database (seperti pada Tes 3). 
3. **Bug Hash Password / State Akun:** Meskipun datanya masuk, *script backend* dari pihak developer (PT. BTU) memiliki kelemahan di mana:
   *  *Password* pendaftar tidak terenkripsi/tersimpan dengan benar, ATAU
   *  *Status* akun langsung menjadi `inactive` (butuh verifikasi admin),
   sehingga saat pendaftar mencoba login, mereka selalu ditolak dengan *"Password Salah"*.
4. **Deadlock (Terjebak):** Akibatnya, pendaftar tidak bisa login, dan karena datanya sudah terlanjur masuk, pendaftar juga selamanya ditolak untuk mendaftar ulang karena validasi pengecekan "*Unique NIK*" pada form registrasi.

## Solusi Lapangan
Satu-satunya jalan keluar jika NIK sudah terjebak *deadlock* ini adalah intervensi manual dari dalam sistem.
Orang tua harus menyerahkan NIK tersebut kepada **Operator Sekolah SD Tujuan / Dinas Pendidikan** dan meminta mereka:
> *"Tolong reset password / hapus akun ini dari Dashboard Admin karena pendaftaran mandiri kami mengalami deadlock akibat bug dari sistem pusat."* 

Operator (yang masuk via portal Admin) memiliki kemampuan *bypass* untuk membuatkan ulang akun tersebut dan menarik data anak tersebut langsung dari dalam tanpa melewati halaman registrasi publik.
