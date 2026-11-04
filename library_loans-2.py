# === Stage 2: Проверка полей ===
# Project: LibraryLoans
from datetime import date


def normalize_input(value):
    if value is None:
        return ""
    return value.strip()


def normalize_title(title):
    title = normalize_input(title)
    if not title:
        raise ValueError("Название книги не может быть пустым.")
    return title


def normalize_author(author):
    author = normalize_input(author)
    if not author:
        raise ValueError("Автор книги не может быть пустым.")
    return author


def normalize_genre(genre):
    genre = normalize_input(genre)
    if not genre:
        raise ValueError("Жанр книги не может быть пустым.")
    return genre


def normalize_status(status):
    valid_statuses = {"доступна", "выдана"}
    normalized = normalize_input(status)
    if not normalized:
        raise ValueError("Статус книги не может быть пустым.")
    if normalized not in valid_statuses:
        raise ValueError(
            f"Недопустимый статус '{normalized}'. "
            "Допустимые значения: 'доступна', 'выдана'."
        )
    return normalized


def validate_book(book):
    errors = []
    title = book.get("title")
    author = book.get("author")
    genre = book.get("genre")
    status = book.get("status")

    try:
        normalize_title(title)
    except ValueError as exc:
        errors.append(str(exc))

    try:
        normalize_author(author)
    except ValueError as exc:
        errors.append(str(exc))

    try:
        normalize_genre(genre)
    except ValueError as exc:
        errors.append(str(exc))

    try:
        normalize_status(status)
    except ValueError as exc:
        errors.append(str(exc))

    return errors
