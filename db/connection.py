import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def connect(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  
                password="",  
                database="game_store"
            )
            return connection
        except Error as e:
            print(f"Error connecting to the database: {e}")
            return None
