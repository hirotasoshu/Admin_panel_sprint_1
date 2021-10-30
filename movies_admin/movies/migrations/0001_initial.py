# Generated by Django 3.2.8 on 2021-10-29 22:44

import uuid

import django.core.validators
import django.db.models.deletion
import movies.utils.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FilmWork",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "creation_date",
                    models.DateField(blank=True, null=True, verbose_name="Дата выхода"),
                ),
                (
                    "certificate",
                    models.TextField(blank=True, null=True, verbose_name="Cертификат"),
                ),
                (
                    "file_path",
                    models.FileField(
                        blank=True, upload_to="film_works/", verbose_name="Файл"
                    ),
                ),
                (
                    "rating",
                    models.FloatField(
                        default=0.0,
                        validators=[movies.utils.validators.validate_rating],
                        verbose_name="Рейтинг",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("movie", "фильм"), ("tv_show", "ТВ шоу")],
                        max_length=20,
                        verbose_name="Тип фильма",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фильм",
                "verbose_name_plural": "Фильмы",
                "db_table": '"content"."film_work"',
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
                "db_table": '"content"."genre"',
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "full_name",
                    models.CharField(
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(3)],
                        verbose_name="Полное имя",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
            ],
            options={
                "verbose_name": "Личность",
                "verbose_name_plural": "Личности",
                "db_table": '"content"."person"',
            },
        ),
        migrations.CreateModel(
            name="PersonFilmWork",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("actor", "актер"),
                            ("director", "режиссер"),
                            ("writer", "сценарист"),
                        ],
                        max_length=20,
                        verbose_name="role",
                    ),
                ),
                (
                    "film_work",
                    models.ForeignKey(
                        db_column="film_work_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        db_column="person_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.person",
                    ),
                ),
            ],
            options={
                "verbose_name": "Роль личности",
                "verbose_name_plural": "Роли личностей",
                "db_table": '"content"."person_film_work"',
            },
        ),
        migrations.CreateModel(
            name="GenreFilmWork",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "film_work",
                    models.ForeignKey(
                        db_column="film_work_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        db_column="genre_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.genre",
                    ),
                ),
            ],
            options={
                "verbose_name": "Жанр фильма",
                "verbose_name_plural": "Жанры фильмов",
                "db_table": '"content"."genre_film_work"',
            },
        ),
        migrations.AddField(
            model_name="filmwork",
            name="genres",
            field=models.ManyToManyField(
                through="movies.GenreFilmWork", to="movies.Genre"
            ),
        ),
        migrations.AddIndex(
            model_name="personfilmwork",
            index=models.Index(
                fields=["film_work_id", "person_id", "role"],
                name="film_work_person_role",
            ),
        ),
        migrations.AddIndex(
            model_name="genrefilmwork",
            index=models.Index(
                fields=["film_work_id", "genre_id"], name="film_work_genre"
            ),
        ),
    ]
