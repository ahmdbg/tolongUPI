from database import baca_requests, simpan_requests
from menu_request.view import tampilkan_request

def submit_request(user):
    print("\n===== SUBMIT HASIL =====")
    data = baca_requests()
    milik_saya = [i for i in data if i["penerima"] == user["username"] and i["status"] == "Sedang Dikerjakan"]

    if not milik_saya:
        return print("Tidak ada request yang sedang kamu kerjakan.")

    for item in milik_saya:
        tampilkan_request(item)

    id_pilihan = input("Masukkan ID request yang selesai: ").strip()
    target = next((i for i in milik_saya if i["id"] == id_pilihan), None)

    if not target:
        return print("ID tidak valid atau request bukan milikmu.")

    if input("Kirim hasil untuk dikonfirmasi pemberi? (y/n): ").strip().lower() == "y":
        target["status"] = "Menunggu Konfirmasi"
        simpan_requests(data)
        print("Hasil berhasil disubmit. Menunggu konfirmasi pemberi.")
    else:
        print("Submit dibatalkan.")