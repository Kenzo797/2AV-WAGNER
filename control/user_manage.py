from model.user import User

class UserManager:
    def __init__(self):
        self.user_model = User()

    def register_user(self):
        username = input("\nEnter a username: ")
        password = input("Enter a password: ")
        self.user_model.create_user(username, password)

    def login_user(self):
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")
        if self.user_model.authenticate_user(username, password):
            print("\nLogin successful!")
            return True
        else:
            print("\nInvalid username or password.")
            return False
