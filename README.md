# Установка зависимостей
1. Необходимо установить [Poetry](https://python-poetry.org/docs/)
2. Установить зависимости:
```console
$ poetry install
```
3. (Опционально):
```console
$ poetry run pre-commit install
```
Это нужно для того, чтобы инициализировать git hook'и перед каждым коммитом (линтер, форматер, сортировщик импортов), а так же запустить команду ниже (может пригодиться при использовании ci)
```console
$ poetry run task lint-and-format
```
4. Создать .env файл на основе .env.example

# schema_design
1. Запуск PG:
```console
$ poetry run task run-pg
```
2. Создание базы данных movies и ее таблиц с индексами:
```console
$ poetry run task create-db
```
3. Зайти в PG shell:
```console
$ poetry run task open-pg-shell
```
