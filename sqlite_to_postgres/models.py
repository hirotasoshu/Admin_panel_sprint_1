from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Optional
from uuid import UUID


class FilmType(str, Enum):
    movie = "movie"
    tv_show = "tv_show"


class PersonRole(str, Enum):
    director = "director"
    writer = "writer"
    actor = "actor"


@dataclass
class FilmWork:
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
    creation_date: Optional[date] = None
    certificate: Optional[str] = None
    file_path: Optional[str] = None
    rating: Optional[float] = None
    type: Optional[FilmType] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Genre:
    __slots__ = (
        "id",
        "name",
        "description",
    )
    id: UUID
    name: str
    description: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class GenreFilmWork:
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
class Person:
    __slots__ = (
        "id",
        "full_name",
        "birth_date",
    )
    id: UUID
    full_name: str
    birth_date: Optional[date] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class PersonFilmWork:
    __slots__ = (
        "id",
        "film_work_id",
        "person_id",
        "role",
    )
    id: UUID
    film_work_id: UUID
    person_id: UUID
    role: Optional[PersonRole] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
