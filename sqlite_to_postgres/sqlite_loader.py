from sqlite3 import Connection
from typing import Iterator, Type

from models import Data, FilmWork, Genre, GenreFilmWork, Person, PersonFilmWork, T


class SQLiteLoader:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        self.cursor = self.connection.cursor()

    def _load_table(self, table_name: str, table_model: Type[T]) -> Iterator[T]:
        for row in self.cursor.execute(f"SELECT * from {table_name}"):
            yield table_model(*row)

    def load_movies(self) -> Data:
        movies = {}
        movies["film_work"] = self._load_table("film_work", FilmWork)
        movies["genre"] = self._load_table("genre", Genre)
        movies["genre_film_work"] = self._load_table("genre_film_work", GenreFilmWork)
        movies["person"] = self._load_table("person", Person)
        movies["person_film_work"] = self._load_table(
            "person_film_work", PersonFilmWork
        )

        return movies

    def __del__(self) -> None:
        self.cursor.close()
