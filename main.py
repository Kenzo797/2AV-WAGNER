from control.user_manage import register_new_user, login_user
from control.game_manage import display_games, add_new_game, delete_game_by_id
from db.database import create_tables

def main_menu():
    print("\n")
    print("Welcome to the Game Store System!")
    create_tables()

    while True:
        print("\nMain Menu")
        print("\n")
        print("1. Login")
        print("2. Register User")
        print("3. Exit")
        print("\n")
        choice = input("Select an option: ")

        if choice == "1":
            if login_user():
                game_menu()

        elif choice == "2":
            register_new_user()

        elif choice == "3":
            print("\nExiting the system. Goodbye!")
            break

        else:
            print("\nInvalid option. Please try again.")

def game_menu():
    while True:
        print("\nGame Management Menu")
        print("\n1. List Games")
        print("2. Add Game")
        print("3. Delete Game")
        print("4. Logout to Main Menu")
        choice = input("\nSelect an option: ")

        if choice == "1":
            display_games()

        elif choice == "2":
            add_new_game()

        elif choice == "3":
            delete_game_by_id()

        elif choice == "4":
            print("\nReturning to the Main Menu.")
            break

        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
