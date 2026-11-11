
from database import baca_requests, simpan_requests
from menu_request.view import tampilkan_request


def submit_request(user):
    print("\n===== SUBMIT HASIL =====")

    data = baca_requests()

    milik_saya = [
        item for item in data
        if item["penerima"] == user["username"]
        and item["status"] == "Sedang Dikerjakan"
    ]

    if not milik_saya:
        print("Tidak ada request yang sedang kamu kerjakan.")
        return

    for item in milik_saya:
        tampilkan_request(item)

    id_pilihan = input("Masukkan ID request yang selesai: ").strip()

    for item in data:
        if (
            item["id"] == id_pilihan
            and item["penerima"] == user["username"]
            and item["status"] == "Sedang Dikerjakan"
        ):
            konfirmasi = input(
                "Kirim hasil untuk dikonfirmasi pemberi? (y/n): "
            ).strip().lower()

            if konfirmasi == "y":
                item["status"] = "Menunggu Konfirmasi"
                simpan_requests(data)
                print("Hasil berhasil disubmit. Menunggu konfirmasi pemberi.")

            else:
                print("Submit dibatalkan.")

            return

    print("ID tidak valid atau request bukan milikmu.")
