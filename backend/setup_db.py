from config.database import get_connection

def setup_database():
    with get_connection() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS games CASCADE;")
            cursor.execute("DROP TABLE IF EXISTS developers CASCADE;")

            cursor.execute("""
                CREATE TABLE developers (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(120) NOT NULL,
                    country VARCHAR(80) NOT NULL,
                    foundation_year INTEGER NOT NULL
                );
            """)

            cursor.execute("""
                CREATE TABLE games (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(150) NOT NULL,
                    genre VARCHAR(60) NOT NULL,
                    price NUMERIC(10, 2) DEFAULT 0.00,
                    release_year INTEGER NOT NULL,
                    consoles VARCHAR(255) NOT NULL,
                    developer_id INTEGER REFERENCES developers(id) ON DELETE CASCADE
                );
            """)

            cursor.execute("""
                INSERT INTO developers (id, name, country, foundation_year) VALUES
                (1, 'Nintendo EPD', 'Japón', 1889),
                (2, 'Rockstar North', 'Reino Unido', 1988),
                (3, 'Mojang Studios', 'Suecia', 2009),
                (4, 'CD Projekt Red', 'Polonia', 2002),
                (5, 'Sony Interactive Entertainment', 'Estados Unidos', 1994),
                (6, 'Valve', 'Estados Unidos', 1996),
                (7, 'Capcom', 'Japón', 1979);
            """)

            cursor.execute("""
                INSERT INTO games (title, genre, price, release_year, consoles, developer_id) VALUES
                ('The Legend of Zelda: Breath of the Wild', 'Aventura', 59.99, 2017, 'Nintendo Switch, Wii U, Nintendo 64, GameCube, NES', 1),
                ('Super Mario Odyssey', 'Plataformas', 49.99, 2017, 'Nintendo Switch, Wii U, 3DS, DS, Wii', 1),
                ('Grand Theft Auto V', 'Acción', 29.99, 2013, 'PS3, PS4, Xbox 360, Xbox One, PC', 2),
                ('Grand Theft Auto: San Andreas', 'Acción', 14.99, 2004, 'PS2, Xbox, PC, iOS, Android', 2),
                ('Minecraft', 'Supervivencia', 26.99, 2011, 'PC, Xbox 360, PS3, Nintendo Switch, PS Vita', 3),
                ('Cyberpunk 2077', 'RPG', 39.99, 2020, 'PC, PS4, PS5, Xbox One, Xbox Series X/S', 4),
                ('The Witcher 3: Wild Hunt', 'RPG', 39.99, 2015, 'PC, PS4, Xbox One, Nintendo Switch, PS5', 4),
                ('God of War', 'Acción', 39.99, 2018, 'PS4, PS5, PC, PS3, PS2', 5),
                ('Marvel''s Spider-Man', 'Acción', 49.99, 2018, 'PS4, PS5, PC, Xbox Series X, Switch', 5),
                ('Counter-Strike 2', 'Shooter', 0.00, 2023, 'PC, Mac, Linux, Steam Deck, Xbox 360', 6),
                ('Portal 2', 'Puzle', 9.99, 2011, 'PC, Xbox 360, PS3, Mac, Linux', 6),
                ('Resident Evil 4', 'Survival Horror', 39.99, 2005, 'GameCube, PS2, PC, Wii, PS4', 7),
                ('Monster Hunter: World', 'Acción RPG', 29.99, 2018, 'PS4, Xbox One, PC, PS5, Xbox Series X/S', 7),
                ('Super Smash Bros. Ultimate', 'Lucha', 59.99, 2018, 'Nintendo Switch, Wii U, 3DS, Wii, N64', 1),
                ('Red Dead Redemption 2', 'Acción', 49.99, 2018, 'PS4, Xbox One, PC, Stadia, PS5', 2);
            """)
            conexion.commit()
            print("Base de datos configurada con éxito.")

if __name__ == "__main__":
    setup_database()