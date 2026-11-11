
from login import register, login
from get_request import get_request
from post_request import post_request


def dashboard(username):
    while True:
        print(f"\n=== TOLONG UPI | {username} ===")
        print("1. Create Request")
        print("2. View Requests")
        print("3. Get Request")
        print("4. Logout")

        choice = input("Select an option: ")

        if choice == "1":
            post_request(username)

        elif choice == "2":
            print("Opening View Requests...")

        elif choice == "3":
            get_request(username)

        elif choice == "4":
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