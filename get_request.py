
import json
import os


DB_FILE = os.path.join(os.path.dirname(__file__), "requests.json")


def get_request(username):
    """Display available requests and allow users to take a request."""

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

    except OSError as error:
        print(f"\nCould not read requests.json: {error}")
        return

    if not isinstance(requests, list):
        print("\nInvalid database format.")
        return

    # 2. Filter available requests
    available_requests = [
        request for request in requests
        if isinstance(request, dict)
        and request.get("status") == "open"
        and request.get("pemberi") != username
    ]

    if not available_requests:
        print("\nNo requests available.")
        return

    # 3. Display available requests
    print("\n===== AVAILABLE REQUESTS =====")

    for request in available_requests:
        print(f"\nID       : {request.get('id')}")
        print(f"Provider : {request.get('pemberi')}")
        print(f"Category : {request.get('jenis')}")
        print(f"Detail   : {request.get('deskripsi')}")
        print(f"Reward   : Rp{request.get('imbalan'):,}")
        print("-" * 35)

    # 4. Select request ID
    try:
        request_id = int(input("\nEnter Request ID to get: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    # 5. Find selected request
    selected_request = next(
        (
            request for request in requests
            if isinstance(request, dict)
            and request.get("id") == request_id
        ),
        None
    )

    if selected_request is None:
        print("Request ID not found.")
        return

    # 6. Validate request
    if selected_request.get("status") != "open":
        print("Request is no longer available.")
        return

    if selected_request.get("pemberi") == username:
        print("You cannot get your own request.")
        return

    # 7. Confirm request
    print("\n===== REQUEST CONFIRMATION =====")
    print(f"Provider : {selected_request.get('pemberi')}")
    print(f"Category : {selected_request.get('jenis')}")
    print(f"Detail   : {selected_request.get('deskripsi')}")
    print(f"Reward   : Rp{selected_request.get('imbalan'):,}")

    confirmation = input(
        "\nAre you sure you want to take this request? (y/n): "
    ).strip().lower()

    if confirmation not in ("y", "yes"):
        print("Request taking cancelled.")
        return

    # 8. Update request status
    selected_request["status"] = "taken"
    selected_request["penerima"] = username

    # 9. Save changes
    try:
        with open(DB_FILE, "w", encoding="utf-8") as file:
            json.dump(requests, file, indent=4, ensure_ascii=False)

    except OSError as error:
        print(f"Could not save request: {error}")

        # Restore original values if saving fails
        selected_request["status"] = "open"
        selected_request["penerima"] = None
        return

    print("\nRequest successfully taken!")
    print(f"Request ID : {request_id}")
    print(f"Your username : {username}")
    print("Status     : TAKEN")
