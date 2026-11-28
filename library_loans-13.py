# === Stage 13: Постраничный вывод ===
# Project: LibraryLoans
def paginate_books(books, page, per_page):
    page = max(1, page)
    per_page = max(1, per_page)
    total = len(books)
    total_pages = (total + per_page - 1) // per_page if total else 0
    if page > total_pages:
        page = max(1, total_pages)
    start = (page - 1) * per_page
    return {
        "items": books[start:start + per_page],
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
    }


def format_book(book):
    return (
        f"Название: {book['title']}, "
        f"Автор: {book['author']}, "
        f"Жанр: {book['genre']}, "
        f"Статус: {book['status']}"
    )


def render_books_page(books, page, per_page):
    result = paginate_books(books, page, per_page)
    items_html = "\n".join(f"  - {format_book(b)}" for b in result["items"])
    return (
        f"Страница {result['page']}/{result['total_pages']}, "
        f"всего {result['total']} книг, по {result['per_page']} за страницу:\n{items_html}"
    )
