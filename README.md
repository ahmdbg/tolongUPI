# Tolong UPI

Aplikasi berbasis terminal untuk menghubungkan pengguna yang membutuhkan bantuan
dengan pengguna yang bersedia mengambil request. Data pengguna dan request
disimpan secara lokal dalam file JSON.

## Fitur

- Mendaftarkan akun dan login.
- Membuat request dengan kategori **Desain**, **Akademik**, **Programming**,
  atau **Editing**.
- Menentukan deskripsi dan imbalan untuk request.
- Mengambil request yang masih terbuka dari pengguna lain.

> Pilihan **View Requests** saat ini belum diimplementasikan.

## Persyaratan

- Python 3
- Tidak memerlukan paket tambahan; aplikasi menggunakan standard library Python.

## Menjalankan aplikasi

Dari folder proyek, jalankan:

```bash
python main.py
```

Pilih **Register** untuk membuat akun, lalu **Login** untuk masuk. Setelah
login, gunakan menu dashboard untuk membuat atau mengambil request.

## Penyimpanan data

- `users.json` menyimpan username dan hash password.
- `requests.json` menyimpan daftar request dalam bentuk JSON.

Request menggunakan field berikut:

| Field | Keterangan |
|---|---|
| `id` | ID unik request |
| `pemberi` | Username pembuat request |
| `jenis` | Kategori request |
| `deskripsi` | Rincian bantuan yang dibutuhkan |
| `imbalan` | Imbalan dalam rupiah |
| `status` | `open` jika tersedia atau `taken` jika sudah diambil |
| `penerima` | Username yang mengambil request, atau `null` jika belum diambil |

File JSON tersebut akan diperbarui ketika akun dibuat, request ditambahkan,
atau request diambil. Jangan menghapus atau mengubah struktur JSON secara
manual saat aplikasi sedang digunakan.

## Catatan

Aplikasi ini merupakan proyek sederhana dengan penyimpanan lokal. Hash password
yang digunakan belum ditujukan untuk penggunaan produksi. Jangan gunakan
password penting atau menyimpan data sensitif di dalamnya.