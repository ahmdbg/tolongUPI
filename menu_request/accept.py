
from database import baca_requests, simpan_requests
from menu_request.view import tampilkan_request


def accept_request(user):
    print("\n===== accept REQUEST =====")

    data = baca_requests()
    tersedia = []

    for item in data:
        if (
            item["status"] == "Tersedia"
            and item["pemberi"] != user["username"]
        ):
            tampilkan_request(item)
            tersedia.append(item)

    if not tersedia:
        print("Belum ada request yang bisa diaccept.")
        return

    id_pilihan = input("\nMasukkan ID request yang ingin diaccept: ").strip()

    for item in data:
        if item["id"] == id_pilihan:
            if item["status"] != "Tersedia":
                print("Request sudah tidak tersedia.")

            elif item["pemberi"] == user["username"]:
                print("Kamu tidak bisa menerima request milik sendiri.")

            else:
                item["penerima"] = user["username"]
                item["status"] = "Sedang Dikerjakan"

                simpan_requests(data)
                print("Request berhasil diaccept!")

            return

    print("ID request tidak ditemukan.")
