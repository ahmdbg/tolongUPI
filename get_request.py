
import json

def get_request(username):
    # Membaca database request
    with open("requests.json", "r") as file:
        requests = json.load(file)

    # Menampilkan request yang masih tersedia
    available_requests = []

    for request in requests:
        if request["status"] == "open" and request["pemberi"] != username:
            available_requests.append(request)

    if not available_requests:
        print("\nNo requests available.")
        return

    print("\n===== AVAILABLE REQUESTS =====")

    for request in available_requests:
        print(f"\nID       : {request['id']}")
        print(f"Provider : {request['pemberi']}")
        print(f"Category : {request['jenis']}")
        print(f"Detail   : {request['deskripsi']}")
        print(f"Reward   : Rp{request['imbalan']:,}")
        print("-" * 35)

    # Memilih request
    try:
        request_id = int(input("\nEnter Request ID to get: "))
    except ValueError:
        print("Invalid ID.")
        return

    # Mencari request berdasarkan ID
    for request in requests:
        if request["id"] == request_id:
            if request["status"] != "open":
                print("Request is no longer available.")
                return

            if request["pemberi"] == username:
                print("You cannot get your own request.")
                return

            request["status"] = "taken"
            request["penerima"] = username

            # Menyimpan perubahan ke database
            with open("requests.json", "w") as file:
                json.dump(requests, file, indent=4)

            print("\nRequest successfully taken!")
            return

    print("Request ID not found.")
