
import csv
import os

FILE_REQUESTS = "requests.csv"

FIELDNAMES = [
    "id", "pemberi", "jenis", "deskripsi",
    "imbalan", "nilai", "status", "penerima"
]


def baca_requests():
    #Membaca seluruh request dari CSV
    if not os.path.exists(FILE_REQUESTS):
        with open(FILE_REQUESTS, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
        return []

    with open(FILE_REQUESTS, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def simpan_requests(data):
    #Menyimpan perubahan request ke CSV
    with open(FILE_REQUESTS, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)
