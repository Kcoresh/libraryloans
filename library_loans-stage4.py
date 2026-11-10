# === Stage 4: Редактирование записей ===
# Project: LibraryLoans
ALLOWED_BOOK_FIELDS = {"title", "author", "genre"}


def edit_book(book_id, changes):
    books = _load_books()
    updated = None
    for book in books:
        if book["id"] == book_id:
            updated = book
            break
    if updated is None:
        raise KeyError(f"Книга с id={book_id} не найдена")
    for field in changes:
        if field not in ALLOWED_BOOK_FIELDS:
            raise ValueError(f"Поле '{field}' для редактирования недоступно")
        updated[field] = changes[field]
    _save_books(books)
    return updated


def _load_books():
    import os
    import json

    path = os.path.join(os.path.dirname(__file__), "books.json")
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_books(books):
    import os
    import json

    path = os.path.join(os.path.dirname(__file__), "books.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
