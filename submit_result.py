
import json
import os
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(__file__), "requests.json")


def submit_result(username):
    # Load request database
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            requests = json.load(file)
    except FileNotFoundError:
        print("Error: requests.json not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON database.")
        return

    # Find requests taken by the current student
    my_requests = [
        request for request in requests
        if request.get("penerima") == username
        and request.get("status") == "taken"
    ]

    if not my_requests:
        print("\nYou have no tasks waiting for submission.")
        return

    # Display tasks
    print("\n===== MY ACTIVE TASKS =====")

    for request in my_requests:
        print(f"\nRequest ID : {request['id']}")
        print(f"Category   : {request['jenis']}")
        print(f"Description: {request['deskripsi']}")
        print(f"Reward     : Rp{request['imbalan']:,}")
        print("-" * 35)

    # Select task
    try:
        request_id = int(input("\nEnter Request ID: "))
    except ValueError:
        print("Invalid Request ID.")
        return

    # Find selected task
    selected_request = next(
        (
            request for request in my_requests
            if request["id"] == request_id
        ),
        None
    )

    if selected_request is None:
        print("Task not found in your active tasks.")
        return

    # Enter submission details
    print("\n===== SUBMIT TASK RESULT =====")

    description = input("Enter result description: ").strip()

    if not description:
        print("Submission description cannot be empty.")
        return

    file_reference = input(
        "Enter file link/reference (optional): "
    ).strip()

    submission_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Save submission
    selected_request["hasil"] = {
        "deskripsi": description,
        "file_reference": file_reference if file_reference else None,
        "waktu_submit": submission_time
    }

    selected_request["status"] = "submitted"

    try:
        with open(DB_FILE, "w", encoding="utf-8") as file:
            json.dump(
                requests,
                file,
                indent=4,
                ensure_ascii=False
            )
    except OSError:
        print("Error: Failed to save submission.")
        return

    print("\n================================")
    print("Result submitted successfully!")
    print(f"Request ID : {request_id}")
    print(f"Submitted  : {submission_time}")
    print("Status     : submitted")
    print("Waiting for requester confirmation.")
    print("================================")
