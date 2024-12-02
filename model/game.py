from db.connection import DatabaseConnection

class Game:
    def __init__(self):
        self.db = DatabaseConnection()

    def add_game(self, title, price):
        connection = self.db.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO games (title, price) VALUES (%s, %s)"
                cursor.execute(query, (title, price))
                connection.commit()
            except Exception as e:
                print(f"Error adding game: {e}")
            finally:
                cursor.close()
                connection.close()

    def list_games(self):
        connection = self.db.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM games"
                cursor.execute(query)
                games = cursor.fetchall()
                return games
            except Exception as e:
                print(f"Error listing games: {e}")
                return []
            finally:
                cursor.close()
                connection.close()

    def delete_game(self, game_id):
        connection = self.db.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM games WHERE id = %s"
                cursor.execute(query, (game_id,))
                connection.commit()
            except Exception as e:
                print(f"Error deleting game: {e}")
            finally:
                cursor.close()
                connection.close()
