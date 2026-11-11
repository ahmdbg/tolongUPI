
from database import baca_requests, simpan_requests
from menu_request.view import tampilkan_request


def konfirmasi_request(user):
    print("\n===== KONFIRMASI HASIL =====")

    data = baca_requests()

    menunggu = [
        item for item in data
        if item["pemberi"] == user["username"]
        and item["status"] == "Menunggu Konfirmasi"
    ]

    if not menunggu:
        print("Belum ada hasil yang menunggu konfirmasi.")
        return

    for item in menunggu:
        tampilkan_request(item)
        print(f"Penerima: {item['penerima']}")

    id_pilihan = input(
        "Masukkan ID request yang akan dikonfirmasi: "
    ).strip()

    for item in data:
        if (
            item["id"] == id_pilihan
            and item["pemberi"] == user["username"]
            and item["status"] == "Menunggu Konfirmasi"
        ):
            pilihan = input(
                "Apakah hasil sudah sesuai? "
                "(y = selesai, n = perlu diperbaiki): "
            ).strip().lower()

            if pilihan == "y":
                item["status"] = "Selesai"
                simpan_requests(data)
                print("Request dikonfirmasi dan selesai!")

            elif pilihan == "n":
                item["status"] = "Sedang Dikerjakan"
                simpan_requests(data)
                print("Request dikembalikan kepada penerima untuk diperbaiki.")

            else:
                print("Pilihan tidak valid. Status tidak berubah.")

            return

    print("ID tidak valid atau request bukan milikmu.")
