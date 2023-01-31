from typing import List, Dict, Union
from .database_connection import DatabaseConnection

book = Dict[str, Union[str, int]]

def create_movie_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS movies(name CHAR PRIMARY KEY, director CHAR, seen INTEGER)')

    
def add_movie(name: str, director: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO movies VALUES(?, ?, 0)', (name, director))

    
def get_all_movies() -> List[book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM movies')
        # list comprehension to dictionary
        movies = [ {'name': row[0], 'director': row[1], 'seen': row[2]} for row in cursor.fetchall()]
    
    return movies

def mark_movie_as_seen(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE movies SET seen=1 WHERE name=?', (name,))
    
    
def delete(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM movies WHERE name=?', (name,))
    
