import re  
from model.game import add_game, list_games, delete_game

def display_games():
    games = list_games()
    if games:
        print("\nGame List:")
        print("\n")
        for game in games:
            print(f"ID: {game[0]}, Title: {game[1]}, Price: {game[2]:.2f}")
    else:
        print("No games found.")

def add_new_game():
    title = input("\nEnter the game title: ")

    while True:
        price_input = input("Enter the game price: ")
        # Remove qualquer caractere que não seja dígito ou ponto
        price_cleaned = re.sub(r'[^\d.]', '', price_input)

        try:
            
            price = float(price_cleaned)
            if price <= 0:  # Verifica se o preço é negativo
                print("Please enter a valid price.")
                continue
            break  
        except ValueError:
            print("\nInvalid input. Please enter a numeric value for the price.")

    add_game(title, price)
    print("\nGame added successfully!")

def delete_game_by_id():
    game_id = int(input("\nEnter the ID of the game to delete: "))
    delete_game(game_id)
    print("\nGame deleted successfully!")
