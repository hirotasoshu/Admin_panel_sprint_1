-- создание бд movies
CREATE DATABASE movies;

-- переключение на созданную бд
\c movies

-- создание схемы content
CREATE SCHEMA content;

-- создание enum типа type
CREATE TYPE film_type AS ENUM ('movie', 'tv_show');

-- создание таблицы film_work
CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title varchar(255) NOT NULL,
    description text,
    creation_date date,
    certificate text,
    file_path varchar(100),
    rating float,
    type film_type,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- создание таблицы genre
CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name varchar(255) NOT NULL,
    description text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- создание таблицы genre_film_work
CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    genre_id uuid NOT NULL,
    created_at timestamp with time zone
);

/*
Создание уникального композитного индекса
Для колонок film_work_id и genre_id для таблицы genre_film_work
Для того, чтобы нельзя было добавить один жанр несколько раз для одного фильма
*/

CREATE UNIQUE INDEX film_work_genre ON content.genre_film_work (film_work_id, genre_id);

-- создание таблицы person
CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name varchar(255),
    birth_date date,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- создание enum типа person_role
CREATE TYPE person_role AS ENUM ('director', 'writer', 'actor');

-- создание таблицы person_film_work
CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role person_role,
    created_at timestamp with time zone
);

/*
Создание уникального композитного индекса
Для колонок film_work_id, person_id и role для таблицы person_film_work
Для того, чтобы нельзя было добавить одного человека с одной и той же ролью для одного фильма
При этом добавить одного человека с разными ролями можно
Пример: Джозеф Гордон-Левитт в фильме «Страсти Дон Жуана», где он является режиссером, сценаристом и исполнителем главной роли
*/
CREATE UNIQUE INDEX film_work_person_role ON content.person_film_work (film_work_id, person_id, role);
