from control.user_manage import UserManager
from control.game_manage import GameManager

def main():
    user_controller = UserManager()
    game_controller = GameManager()

    print("Welcome to Game Store Management System!")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_controller.register_user()
        elif choice == "2":
            if user_controller.login_user():
                while True:
                    print("\n1. List Games")
                    print("2. Add New Game")
                    print("3. Delete Game")
                    print("4. Logout")
                    game_choice = input("Enter your choice: ")

                    if game_choice == "1":
                        game_controller.display_games()
                    elif game_choice == "2":
                        game_controller.add_new_game()
                    elif game_choice == "3":
                        game_controller.delete_game_by_id()
                    elif game_choice == "4":
                        print("\nLogged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
