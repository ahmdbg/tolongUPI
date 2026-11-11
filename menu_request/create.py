
from database import baca_requests, simpan_requests


def create_request(user):
    print("\n===== BUAT REQUEST =====")

    jenis = input("Jenis request (Mengambil Barang/Membeli Barang/Lainnya): ").strip()
    deskripsi = input("Deskripsi request: ").strip()

    if not jenis or not deskripsi:
        print("Jenis dan deskripsi tidak boleh kosong.")
        return

    print("\nJenis imbalan:\n1. Monetary (Uang)\n2. Object (Barang)")
    pilihan = input("Pilih imbalan: ").strip()

    if pilihan == "1":
        imbalan = "Monetary"
        nilai = input("Nominal uang (contoh 15000): Rp ").strip()

        if not nilai.isdigit():
            print("Nominal harus berupa angka.")
            return

    elif pilihan == "2":
        imbalan = "Object"
        nilai = input("Barang imbalan: ").strip()

        if not nilai:
            print("Barang imbalan tidak boleh kosong.")
            return

    else:
        print("Pilihan imbalan tidak valid.")
        return

    data = baca_requests()
    id_baru = max([int(item["id"]) for item in data], default=0) + 1

    data.append({
        "id": str(id_baru),
        "pemberi": user["username"],
        "jenis": jenis,
        "deskripsi": deskripsi,
        "imbalan": imbalan,
        "nilai": nilai,
        "status": "Tersedia",
        "penerima": ""
    })

    simpan_requests(data)
    print("Request berhasil dibuat!")
