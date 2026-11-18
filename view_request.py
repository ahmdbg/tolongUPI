
import json
import os


DB_FILE = os.path.join(os.path.dirname(__file__), "requests.json")


def view_request(username):
    """Display all requests created by the logged-in user."""

    # 1. Read request database
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            requests = json.load(file)

    except FileNotFoundError:
        print("\nNo requests available.")
        return

    except json.JSONDecodeError:
        print("\nCould not load requests: invalid JSON.")
        return

    # 2. Filter requests by username
    my_requests = [
        request for request in requests
        if isinstance(request, dict)
        and request.get("pemberi") == username
    ]

    # 3. Check if user has any requests
    if not my_requests:
        print("\n===== MY REQUESTS =====")
        print("You haven't created any requests yet.")
        return

    # 4. Display user's requests
    print("\n===== MY REQUESTS =====")

    for request in my_requests:
        print(f"\nID       : {request['id']}")
        print(f"Category : {request['jenis']}")
        print(f"Detail   : {request['deskripsi']}")
        print(f"Reward   : Rp{request['imbalan']:,}")
        print(f"Status   : {request['status'].upper()}")

        receiver = request.get("penerima")

        if receiver is None:
            receiver = "Not assigned"

        print(f"Receiver : {receiver}")
        print("-" * 35)

    # 5. Display total requests
    print(f"\nTotal Requests: {len(my_requests)}")
