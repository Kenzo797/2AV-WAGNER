from db.connection import DatabaseConnection

class User:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_user(self, username, password):
        connection = self.db.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(query, (username, password))
                connection.commit()
                print("User created successfully!")
            except Exception as e:
                print(f"Error creating user: {e}")
            finally:
                cursor.close()
                connection.close()

    def authenticate_user(self, username, password):
        connection = self.db.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM users WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()
                return user is not None
            except Exception as e:
                print(f"Error authenticating user: {e}")
                return False
            finally:
                cursor.close()
                connection.close()
