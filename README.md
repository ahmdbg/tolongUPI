# Tolong UPI

Tolong UPI adalah aplikasi berbasis terminal yang mempertemukan mahasiswa atau
pengguna yang membutuhkan bantuan dengan pengguna lain yang bersedia
mengerjakannya. Semua data disimpan secara lokal di komputer menggunakan file
JSON, sehingga aplikasi tidak memerlukan server database atau layanan tambahan.

> **Status proyek:** aplikasi ini merupakan proyek pembelajaran/portabel.
> Pilihan **View Requests** pada dashboard saat ini hanya menampilkan pesan dan
> belum memiliki layar daftar request tersendiri. Daftar request terbuka dapat
> dilihat melalui menu **Get Request**.

---

## Daftar Isi

- [Ringkasan](#ringkasan)
- [Fitur](#fitur)
- [Cara Kerja](#cara-kerja)
- [Struktur Proyek](#struktur-proyek)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi dan Menjalankan](#instalasi-dan-menjalankan)
- [Panduan Penggunaan](#panduan-penggunaan)
- [Format Penyimpanan Data](#format-penyimpanan-data)
- [Alur dan Validasi](#alur-dan-validasi)
- [Contoh Skenario](#contoh-skenario)
- [Batasan dan Keamanan](#batasan-dan-keamanan)
- [Pemecahan Masalah](#pemecahan-masalah)
- [Pengembangan Selanjutnya](#pengembangan-selanjutnya)

---

## Ringkasan

Aplikasi menyediakan alur sederhana sebagai berikut:

1. Pengguna membuat akun.
2. Pengguna masuk dengan username dan password.
3. Pengguna dapat membuat permintaan bantuan beserta kategori dan imbalan.
4. Pengguna lain dapat mengambil permintaan yang masih berstatus `open`.
5. Permintaan yang sudah diambil berubah menjadi `taken` dan menyimpan username
   penerimanya.

Konsep “UPI” pada nama proyek merujuk pada identitas kampus/lokal proyek,
sedangkan implementasi saat ini tidak terhubung ke sistem atau API resmi UPI.

---

## Fitur

### Manajemen akun

- Pendaftaran akun baru.
- Username unik dan tidak boleh sama dengan akun yang sudah terdaftar.
- Password dikonfirmasi dua kali saat registrasi.
- Password minimal 6 karakter.
- Pengecekan username dan password saat login.
- Password tidak disimpan sebagai teks biasa, melainkan sebagai hash SHA-256.

### Pembuatan request

- Empat kategori tersedia:
  - `Desain`
  - `Akademik`
  - `Programming`
  - `Editing`
- Deskripsi request wajib diisi.
- Imbalan harus berupa bilangan bulat dan bernilai lebih dari nol.
- ID request dibuat otomatis secara berurutan berdasarkan ID terbesar yang ada.

### Pengambilan request

- Menampilkan request berstatus `open`.
- Tidak menampilkan request milik pengguna yang sedang login.
- Pengguna dapat memilih request melalui ID.
- Setelah diambil, status request berubah menjadi `taken`.
- Username penerima disimpan pada field `penerima`.
- Pengguna tidak dapat mengambil request miliknya sendiri.

---

## Cara Kerja

### Struktur menu

Saat aplikasi pertama kali dijalankan:

```text
1. Register
2. Login
3. Exit
```

Setelah berhasil login, pengguna masuk ke dashboard:

```text
1. Create Request
2. View Requests
3. Get Request
4. Logout
```

### Siklus data

```text
Register -> users.json -> login berhasil
                            |
                            v
                    dashboard pengguna
                            |
              +-------------+-------------+
              |                           |
      Create Request               Get Request
              |                           |
              v                           v
      requests.json              requests.json diperbarui
      (status: open)             (status: taken)
```

---

## Struktur Proyek

| File | Fungsi utama |
|---|---|
| `main.py` | Titik masuk aplikasi, menu utama, dashboard, dan logout |
| `login.py` | Registrasi, penyimpanan pengguna, hashing password, dan login |
| `post_request.py` | Pemilihan kategori, validasi data, dan pembuatan request |
| `get_request.py` | Pemilihan request terbuka dan pembaruan status request |
| `users.json` | Penyimpanan username dan hash password |
| `requests.json` | Penyimpanan seluruh request beserta statusnya |
| `README.md` | Dokumentasi penggunaan dan pengembangan |

### Hubungan modul

- `main.py` mengimpor fungsi `register()` dan `login()` dari `login.py`.
- `main.py` mengimpor `post_request()` dari `post_request.py`.
- `main.py` mengimpor `get_request()` dari `get_request.py`.
- `login.py` membaca dan menulis `users.json`.
- `post_request.py` membaca dan menulis `requests.json`.
- `get_request.py` membaca dan menulis `requests.json`.

---

## Persyaratan Sistem

- Python 3.8 atau versi yang lebih baru direkomendasikan.
- Terminal atau command prompt yang mendukung input password tersembunyi
  melalui `getpass`.
- Tidak ada dependensi pihak ketiga.
- Aplikasi menggunakan pustaka bawaan Python: `json`, `hashlib`, `getpass`, dan
  `os`.

Periksa versi Python dengan:

```bash
python --version
```

---

## Instalasi dan Menjalankan

### 1. Pastikan folder proyek tersedia

Salin atau kloning repositori ke komputer Anda. Masuk ke folder utama proyek:

```bash
cd /lokasi/tolongUPI
```

Contoh Windows:

```powershell
cd E:\tolongUPI
```

### 2. Jalankan aplikasi

Gunakan salah satu perintah berikut:

```bash
python main.py
```

atau, tergantung konfigurasi Python pada sistem:

```bash
py main.py
```

### 3. Pastikan direktori kerja benar

Masuk ke folder proyek sebelum menjalankan aplikasi. Hal ini penting karena
`get_request.py` saat ini membaca `requests.json` melalui jalur relatif.

Setelah menu utama muncul, pilih nomor yang tersedia lalu tekan Enter.

---

## Panduan Penggunaan

### Registrasi akun

1. Pilih `1. Register`.
2. Masukkan username.
3. Masukkan password.
4. Masukkan ulang password untuk konfirmasi.
5. Password harus berisi minimal 6 karakter.

Aturan registrasi:

- Username tidak boleh kosong.
- Username harus belum terdaftar.
- Password dan konfirmasi password harus sama.
- Jika registrasi berhasil, akun langsung tersimpan pada `users.json`.

Contoh:

```text
=== CREATE NEW ACCOUNT ===
Enter username: budi
Enter password:
Confirm password:

Account 'budi' successfully registered!
```

### Login

1. Pilih `2. Login`.
2. Masukkan username yang terdaftar.
3. Masukkan password.

Jika sesuai, aplikasi menampilkan dashboard atas nama pengguna. Jika tidak,
pesan `Invalid username or password.` akan ditampilkan.

### Membuat request

1. Login terlebih dahulu.
2. Pilih `1. Create Request`.
3. Pilih kategori dengan memasukkan angka 1 sampai 4.
4. Isi deskripsi bantuan.
5. Isi imbalan dalam rupiah sebagai angka bulat.

Contoh:

```text
Select a category:
1. Desain
2. Akademik
3. Programming
4. Editing
Choose category number: 3
Description: Perbaiki error pada program Python
Reward (Rp): 30000

Request successfully created! (ID: 9)
```

Pengecekan yang dilakukan:

- Pilihan kategori harus bernilai 1–4.
- Deskripsi tidak boleh kosong.
- Imbalan harus berupa angka bulat.
- Imbalan harus lebih besar dari nol.

### Mengambil request

1. Pilih `3. Get Request`.
2. Lihat daftar request berstatus `open` milik pengguna lain.
3. Masukkan ID request yang ingin diambil.
4. Jika berhasil, status berubah menjadi `taken`.

Informasi yang ditampilkan untuk setiap request meliputi:

- ID
- Username pemberi request
- Kategori
- Deskripsi
- Imbalan dalam format rupiah

Request milik pengguna yang sedang login tidak ditampilkan sebagai opsi dan
tidak dapat diambil.

### Logout dan keluar

- Pilih `4. Logout` pada dashboard untuk kembali ke menu utama.
- Pilih `3. Exit` pada menu utama untuk menutup aplikasi.

---

## Format Penyimpanan Data

### `users.json`

File pengguna memiliki format objek JSON. Setiap key adalah username dan setiap
nilainya adalah hash SHA-256 dari password.

Contoh struktur:

```json
{
    "budi": "2c04ae44eb7489574d4237cb82ea1d0ff64250510fe878d3ab19608835abb09c"
}
```

Penting:

- Jangan mengubah atau mengganti hash password secara manual.
- Nilai hash tidak dapat dikonversi langsung menjadi password.
- Proses login menghitung ulang hash password yang dimasukkan lalu mencocokkannya
  dengan nilai pada file.

### `requests.json`

File request menggunakan array JSON. Setiap elemen merupakan satu request.

Contoh request terbuka:

```json
{
    "id": 9,
    "pemberi": "budi",
    "jenis": "Programming",
    "deskripsi": "Perbaiki error pada program Python",
    "imbalan": 30000,
    "status": "open",
    "penerima": null
}
```

Contoh request yang sudah diambil:

```json
{
    "id": 9,
    "pemberi": "budi",
    "jenis": "Programming",
    "deskripsi": "Perbaiki error pada program Python",
    "imbalan": 30000,
    "status": "taken",
    "penerima": "andi"
}
```

Penjelasan field:

| Field | Tipe | Keterangan |
|---|---|---|
| `id` | `integer` | ID unik dan selalu bertambah saat request dibuat |
| `pemberi` | `string` | Username pengguna yang membuat request |
| `jenis` | `string` | Salah satu dari empat kategori yang tersedia |
| `deskripsi` | `string` | Rincian bantuan yang dibutuhkan |
| `imbalan` | `integer` | Nilai imbalan dalam rupiah |
| `status` | `string` | `open` jika masih tersedia atau `taken` jika sudah diambil |
| `penerima` | `string` atau `null` | Username pengambil; `null` sebelum diambil |

### Pengelolaan file JSON

- Beri aplikasi waktu untuk menyelesaikan penulisan file sebelum menutup terminal.
- Jangan menjalankan dua instance yang menulis file JSON pada saat bersamaan.
- Buat cadangan `users.json` dan `requests.json` sebelum mengubah datanya
  secara manual.
- Jika JSON rusak, aplikasi dapat gagal membaca atau menyimpan data.
- Untuk penanganan JSON manual, gunakan editor teks atau JSON yang mampu
  memvalidasi format.

---

## Alur dan Validasi

### Registrasi

| Kondisi | Hasil |
|---|---|
| Username kosong | Registrasi dibatalkan |
| Username sudah ada | Registrasi dibatalkan |
| Password kosong atau kurang dari 6 karakter | Registrasi dibatalkan |
| Password dan konfirmasi berbeda | Registrasi dibatalkan |
| Semua data valid | Akun disimpan pada `users.json` |

### Login

| Kondisi | Hasil |
|---|---|
| Username tidak ditemukan | Login ditolak |
| Password hash tidak sesuai | Login ditolak |
| Username dan password sesuai | Dashboard dibuka |

### Pembuatan request

| Kondisi | Hasil |
|---|---|
| Pilihan bukan angka | Kategori ditolak |
| Pilihan di luar rentang 1–4 | Kategori ditolak |
| Deskripsi kosong | Request dibatalkan |
| Imbalan bukan bilangan bulat | Request dibatalkan |
| Imbalan <= 0 | Request dibatalkan |
| JSON request tidak valid | Request tidak dibuat |
| Semua data valid | Request ditambahkan ke daftar |

### Pengambilan request

| Kondisi | Hasil |
|---|---|
| Tidak ada request terbuka milik pengguna lain | Pesan tidak ada request tersedia |
| ID bukan angka | Pemilihan ditolak |
| ID tidak ditemukan | Pesan ID tidak ditemukan |
| Request sudah `taken` | Permintaan ditolak |
| Request milik pengguna sendiri | Permintaan ditolak |
| Semua syarat memenuhi | Status diubah menjadi `taken` |

---

## Contoh Skenario

### Skenario 1: Mengambil kertas HVS

1. Hasan membuat akun atau login.
2. Hasan membuat request kategori `Akademik`.
3. Deskripsi diisi: `Membelikan Kertas HVS A4 Satu pack`.
4. Imbalan diisi `20000`.
5. Pengguna lain membuka menu `Get Request`.
6. Pengguna lain memilih ID request milik Hasan.
7. Status request berubah menjadi `taken`.
8. Field `penerima` diisi dengan username pengambil.

### Skenario 2: Request milik sendiri

Jika seorang pengguna mencoba mengambil request miliknya sendiri, aplikasi
menolak dengan pesan:

```text
You cannot get your own request.
```

### Skenario 3: Request sudah diambil

Jika request dipilih setelah statusnya berubah menjadi `taken`, aplikasi
menampilkan:

```text
Request is no longer available.
```

---

## Batasan dan Keamanan

### Penyimpanan lokal

Data tidak dienkripsi dan tersimpan dalam bentuk teks atau hash pada file JSON.
Siapa pun yang memiliki akses ke sistem dapat membaca `requests.json` dan file
pengguna.

### Keamanan password

- Password disimpan menggunakan SHA-256.
- SHA-256 cocok untuk proyek pembelajaran, tetapi bukan mekanisme penyimpanan
  password modern.
- Implementasi ini belum menggunakan salt atau password hashing yang sengaja
  dibangun untuk kebutuhan password seperti Argon2, bcrypt, atau scrypt.
- Jangan menggunakan password asli yang digunakan pada akun lain.
- Jangan gunakan aplikasi ini sebagai sistem autentikasi produksi.

### Konsistensi data

- Tidak ada sistem transaksi atau database.
- Tidak ada mekanisme kunci file untuk mencegah pembaruan bersamaan.
- Mengubah file JSON saat aplikasi berjalan dapat menyebabkan data tidak
  konsisten.
- Penggunaan beberapa instance aplikasi secara bersamaan belum didukung.

### Fitur yang belum tersedia

- Tampilan daftar request khusus pada menu `View Requests`.
- Melihat riwayat request milik pengguna.
- Membatalkan atau menyelesaikan request.
- Mengubah atau menghapus akun dan request.
- Pembayaran atau pencatatan transaksi imbalan.
- Komunikasi langsung antara pemberi dan penerima.
- Sinkronisasi antar perangkat.
- Autentikasi berbasis server.

---

## Pemecahan Masalah

### `python` tidak dikenali

Coba perintah:

```bash
py main.py
```

Pastikan Python telah ditambahkan ke `PATH`. Verifikasi instalasi:

```bash
python --version
```

### Password tidak terlihat saat diketik

Ini merupakan perilaku normal dari `getpass`. Terminal menyembunyikan input
password tanpa menampilkan karakter atau tanda bintang. Ketik dengan benar,
lalu tekan Enter.

### `No module named ...`

Aplikasi tidak memerlukan paket eksternal. Jika pesannya melibatkan modul proyek
sendiri seperti `login` atau `get_request`, pastikan Anda berada pada folder
proyek dan menjalankan:

```bash
python main.py
```

### `No requests available`

Kemungkinan penyebabnya:

- Belum ada request.
- Semua request berstatus `taken`.
- Semua request terbuka adalah milik pengguna yang sedang login.

### `Could not create request: requests.json contains invalid JSON`

Perbaiki format JSON pada `requests.json`. Pulihkan dari cadangan jika
tersedia. Pastikan data merupakan array JSON yang valid dan tidak memiliki koma
atau kurung yang salah.

### `requests.json must contain a JSON list`

Isi `requests.json` harus berbentuk array, bukan objek JSON. Bentuk minimal yang
benar adalah:

```json
[]
```

### Perubahan data tidak tersimpan

Pastikan aplikasi memiliki hak tulis pada folder proyek. Jika menggunakan
terminal, jalankan dari folder yang dapat diakses dan tertulis. Jangan membuka
file JSON dalam mode aplikasi lain yang menguncinya saat aplikasi dijalankan.

---

## Pengembangan Selanjutnya

Perbaikan yang disarankan untuk versi berikutnya:

- Mengimplementasikan menu `View Requests`.
- Menambah riwayat request milik setiap pengguna.
- Menambah status `completed` dan `cancelled`.
- Menambah fitur edit atau hapus request.
- Memindahkan penyimpanan ke SQLite atau database lain.
- Menggunakan jalur file berbasis `__file__` secara konsisten pada semua modul.
- Menambahkan unit test untuk registrasi, login, request, dan parsing input.
- Menambahkan password hashing dengan salt dan algoritma khusus password.
- Menyembunyikan data sensitif dari log atau tampilan terminal.
- Menambahkan pembaruan data aman saat beberapa proses berjalan sekaligus.
- Memisahkan lapisan data, logika bisnis, dan antarmuka terminal.

Saat mengembangkan, gunakan data contoh terpisah agar file JSON utama tidak
terisi data percobaan. Jangan membagikan file `users.json` yang berisi data
pengguna nyata.