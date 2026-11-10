
from login import register, login


def dashboard(username):
    while True:
        print(f"\n=== TOLONG UPI | {username} ===")
        print("1. Create Request")
        print("2. View Requests")
        print("3. Logout")

        choice = input("Select an option: ")

        if choice == "1":
            print("Opening Create Request...")

        elif choice == "2":
            print("Opening View Requests...")

        elif choice == "3":
            print("Logging out...")
            break

        else:
            print("Invalid option.")


def main():
    while True:
        print("\n====================")
        print("     TOLONG UPI")
        print("====================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            register()

        elif choice == "2":
            username = login()

            if username:
                dashboard(username)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()