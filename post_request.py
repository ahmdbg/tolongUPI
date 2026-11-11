import json
import os


DB_FILE = os.path.join(os.path.dirname(__file__), "requests.json")
CATEGORIES = ("Desain", "Akademik", "Programming", "Editing")


def post_request(username):
    """Create a request and save it to requests.json."""
    print("\n===== CREATE REQUEST =====")

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

    deskripsi = input("Description: ").strip()
    if not deskripsi:
        print("Description cannot be empty.")
        return

    try:
        imbalan = int(input("Reward (Rp): ").strip())
    except ValueError:
        print("Reward must be a whole number.")
        return

    if imbalan <= 0:
        print("Reward must be greater than zero.")
        return

    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            requests = json.load(file)
    except FileNotFoundError:
        requests = []
    except json.JSONDecodeError:
        print("Could not create request: requests.json contains invalid JSON.")
        return

    if not isinstance(requests, list):
        print("Could not create request: requests.json must contain a JSON list.")
        return

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

    requests.append(
        {
            "id": request_id,
            "pemberi": username,
            "jenis": jenis,
            "deskripsi": deskripsi,
            "imbalan": imbalan,
            "status": "open",
            "penerima": None,
        }
    )

    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(requests, file, indent=4, ensure_ascii=False)

    print(f"\nRequest successfully created! (ID: {request_id})")