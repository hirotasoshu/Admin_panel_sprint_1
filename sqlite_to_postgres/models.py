from dataclasses import astuple, dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, Iterator, Optional, Tuple, TypeVar
from uuid import UUID

T = TypeVar("T", bound="Table")
Data = Dict[str, Iterator[T]]


@dataclass
class Table:
    @property
    def values(self) -> Tuple[Any, ...]:
        return astuple(self)


class FilmType(str, Enum):
    movie = "movie"
    tv_show = "tv_show"


class PersonRole(str, Enum):
    director = "director"
    writer = "writer"
    actor = "actor"


@dataclass
class FilmWork(Table):
    __slots__ = (
        "id",
        "title",
        "description",
        "creation_date",
        "certificate",
        "file_path",
        "rating",
        "type",
    )
    id: UUID
    title: str
    description: Optional[str]
    creation_date: Optional[date]
    certificate: Optional[str]
    file_path: Optional[str]
    rating: Optional[float]
    type: Optional[FilmType]
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Genre(Table):
    __slots__ = (
        "id",
        "name",
        "description",
    )
    id: UUID
    name: str
    description: Optional[str]
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class GenreFilmWork(Table):
    __slots__ = (
        "id",
        "film_work_id",
        "genre_id",
    )
    id: UUID
    film_work_id: UUID
    genre_id: UUID
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Person(Table):
    __slots__ = (
        "id",
        "full_name",
        "birth_date",
    )
    id: UUID
    full_name: str
    birth_date: Optional[date]
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class PersonFilmWork(Table):
    __slots__ = (
        "id",
        "film_work_id",
        "person_id",
        "role",
    )
    id: UUID
    film_work_id: UUID
    person_id: UUID
    role: Optional[PersonRole]
    created_at: datetime = field(default_factory=datetime.utcnow)
