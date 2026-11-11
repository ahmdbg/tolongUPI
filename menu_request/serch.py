
from database import baca_requests
from menu_request.view import tampilkan_request


def serch_request(user):
    print("\n===== serch REQUEST =====")

    keyword = input(
        "Masukkan kata kunci jenis/deskripsi (kosong = semua): "
    ).strip().lower()

    data = baca_requests()
    ditemukan = False

    for item in data:
        cocok = (
            keyword in item["jenis"].lower()
            or keyword in item["deskripsi"].lower()
        )

        if (
            cocok
            and item["status"] == "Tersedia"
            and item["pemberi"] != user["username"]
        ):
            tampilkan_request(item)
            ditemukan = True

    if not ditemukan:
        print("Request tidak ditemukan atau tidak tersedia.")
