
import os
import json
import hashlib
import getpass

# Always use the same users.json location
DB_FILE = os.path.join(os.path.dirname(__file__), "users.json")


def load_database():
    """Load registered users from users.json."""
    if not os.path.exists(DB_FILE):
        return {}

    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_database(data):
    """Save registered users into users.json."""
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


def hash_password(password):
    """Hash password before storing it."""
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    """Register a new user."""
    print("\n=== CREATE NEW ACCOUNT ===")

    database = load_database()

    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if username in database:
        print("Username already exists!")
        return

    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return

    if len(password) < 6:
        print("Password must be at least 6 characters.")
        return

    # Save the username and hashed password
    database[username] = hash_password(password)

    save_database(database)

    print(f"\nAccount '{username}' successfully registered!")


def login():
    """Verify login credentials."""
    print("\n=== USER LOGIN ===")

    database = load_database()

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    hashed_password = hash_password(password)

    if username in database and database[username] == hashed_password:
        print(f"\nWelcome back, {username}!")
        return username

    print("\nInvalid username or password.")
    return None