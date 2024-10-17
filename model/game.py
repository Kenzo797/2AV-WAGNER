from db.database import connect_database

def add_game(title, price):
    
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO games (title, price) VALUES (?, ?)', (title, price))
    conn.commit()
    conn.close()

def list_games():
    
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()
    conn.close()
    return games

def delete_game(game_id):
    
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM games WHERE id = ?', (game_id,))
    conn.commit()
    conn.close()
