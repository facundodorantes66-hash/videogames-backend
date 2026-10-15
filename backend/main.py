from fastapi import FastAPI, HTTPException
from config.database import get_connection

app = FastAPI(
    title="Biblioteca de Videojuegos",
    description="API de consultas GET con FastAPI y PostgreSQL",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a la Biblioteca de Videojuegos",
        "documentacion": "/docs"
    }

@app.get("/games")
def obtener_videojuegos():
    with get_connection() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT g.id, g.title, g.genre, g.price,
                       g.release_year, g.consoles, g.developer_id,
                       d.name AS developer_name
                FROM games AS g
                JOIN developers AS d
                ON g.developer_id = d.id
                ORDER BY g.id;
            """)
            return cursor.fetchall()

@app.get("/games/genre/{genre}")
def obtener_por_genero(genre: str):
    with get_connection() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT g.id, g.title, g.genre, g.price,
                       g.release_year, g.consoles, g.developer_id,
                       d.name AS developer_name
                FROM games AS g
                JOIN developers AS d
                ON g.developer_id = d.id
                WHERE LOWER(g.genre) = LOWER(%s)
                ORDER BY g.id;
            """, (genre,))
            return cursor.fetchall()

@app.get("/games/{id}")
def obtener_videojuego(id: int):
    with get_connection() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT g.id, g.title, g.genre, g.price,
                       g.release_year, g.consoles, g.developer_id,
                       d.name AS developer_name
                FROM games AS g
                JOIN developers AS d
                ON g.developer_id = d.id
                WHERE g.id = %s;
            """, (id,))
            juego = cursor.fetchone()

    if juego is None:
        raise HTTPException(
            status_code=404,
            detail="Videojuego no encontrado"
        )

    return juego

@app.get("/developers")
def obtener_desarrolladores():
    with get_connection() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, name, country, foundation_year
                FROM developers
                ORDER BY id;
            """)
            return cursor.fetchall()

@app.get("/developers/{id}")
def obtener_desarrollador(id: int):
    with get_connection() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, name, country, foundation_year
                FROM developers
                WHERE id = %s;
            """, (id,))
            desarrollador = cursor.fetchone()

    if desarrollador is None:
        raise HTTPException(
            status_code=404,
            detail="Desarrollador no encontrado"
        )

    return desarrollador