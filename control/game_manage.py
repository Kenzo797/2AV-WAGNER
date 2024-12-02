from model.game import Game
import re

class GameManager:
    def __init__(self):
        self.game_model = Game()

    def display_games(self):
        games = self.game_model.list_games()
        if games:
            print("\nGame List:")
            for game in games:
                print(f"ID: {game[0]}, Title: {game[1]}, Price: {game[2]:.2f}")
        else:
            print("No games found.")

    def add_new_game(self):
        title = input("\nEnter the game title: ")

        while True:
            price_input = input("Enter the game price (e.g., $10 or R$10): ")
            price_cleaned = re.sub(r'[^\d.]', '', price_input)

            try:
                price = float(price_cleaned)
                if price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the price.")

        self.game_model.add_game(title, price)
        print("\nGame added successfully!")

    def delete_game_by_id(self):
        try:
            game_id = int(input("\nEnter the ID of the game to delete: "))
            self.game_model.delete_game(game_id)
            print("\nGame deleted successfully!")
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")
