
import json
import os


DB_FILE = os.path.join(os.path.dirname(__file__), "requests.json")
CATEGORIES = ("Desain", "Akademik", "Programming", "Editing")


def post_request(username):
    """Create a request and save it to requests.json."""
    print("\n===== CREATE REQUEST =====")

    # 1. Select category
    print("\nSelect a category:")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    try:
        category_choice = int(input("Choose category number: ").strip())
    except ValueError:
        print("Invalid category choice.")
        return

    if not 1 <= category_choice <= len(CATEGORIES):
        print("Invalid category choice.")
        return

    jenis = CATEGORIES[category_choice - 1]

    # 2. Input description
    deskripsi = input("Description: ").strip()

    if not deskripsi:
        print("Description cannot be empty.")
        return

    # 3. Input reward
    try:
        imbalan = int(input("Reward (Rp): ").strip())
    except ValueError:
        print("Reward must be a whole number.")
        return

    if imbalan <= 0:
        print("Reward must be greater than zero.")
        return

    # 4. Read existing requests
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            requests = json.load(file)

    except FileNotFoundError:
        requests = []

    except json.JSONDecodeError:
        print("Could not create request: requests.json contains invalid JSON.")
        return

    except OSError as error:
        print(f"Could not read requests.json: {error}")
        return

    if not isinstance(requests, list):
        print("Could not create request: requests.json must contain a JSON list.")
        return

    # 5. Generate request ID
    request_id = max(
        (
            request["id"]
            for request in requests
            if isinstance(request, dict)
            and isinstance(request.get("id"), int)
            and not isinstance(request.get("id"), bool)
        ),
        default=0,
    ) + 1

    # 6. Preview request
    print("\n===== REQUEST PREVIEW =====")
    print(f"Request ID  : {request_id}")
    print(f"Posted by   : {username}")
    print(f"Category    : {jenis}")
    print(f"Description : {deskripsi}")
    print(f"Reward      : Rp{imbalan:,}")
    print("Status      : open")

    # 7. Confirmation
    confirmation = input("\nSubmit this request? (y/n): ").strip().lower()

    if confirmation not in ("y", "yes"):
        print("Request creation cancelled.")
        return

    # 8. Create request data
    new_request = {
        "id": request_id,
        "pemberi": username,
        "jenis": jenis,
        "deskripsi": deskripsi,
        "imbalan": imbalan,
        "status": "open",
        "penerima": None,
    }

    requests.append(new_request)

    # 9. Save request
    try:
        with open(DB_FILE, "w", encoding="utf-8") as file:
            json.dump(requests, file, indent=4, ensure_ascii=False)

    except OSError as error:
        print(f"Could not save request: {error}")
        return

    print(f"\nRequest successfully created! (ID: {request_id})")
