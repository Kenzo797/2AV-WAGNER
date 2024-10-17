from model.user import register_user, validate_login

def register_new_user():
    username = input("\nEnter a new username: ")
    password = input("Enter a password: ")
    register_user(username, password)
    print("\nUser successfully registered!")

def login_user():
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    if validate_login(username, password):
        print(f"\nLogin successful! Welcome, {username}.")
        return True
    else:
        print("\nIncorrect username or password. Please try again.")
        return False
