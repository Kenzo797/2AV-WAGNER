from db.connection import DatabaseConnection

def setup_database():
    db = DatabaseConnection()
    connection = db.connect()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Criação do banco de dados
            cursor.execute("CREATE DATABASE IF NOT EXISTS game_store")
            cursor.execute("USE game_store")
            
            # Criação da tabela de jogos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS games (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    price DECIMAL(10, 2) NOT NULL
                )
            """)
            
            # Criação da tabela de usuários
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                )
            """)
            print("Database and tables setup completed successfully!")
        except Exception as e:
            print(f"Error setting up the database: {e}")
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    setup_database()
