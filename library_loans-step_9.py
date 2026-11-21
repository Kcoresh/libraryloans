# === Stage 9: Фильтрация записей ===
# Project: LibraryLoans
"""LibraryLoans: фильтрация книг по автору и диапазону дат выдачи."""

from datetime import date


def filter_by_author(books, author):
    """Вернуть книги, написанные указанным автором."""
    return [book for book in books if book["author"] == author]


def filter_by_issue_date_range(books, start_date, end_date):
    """Вернуть книги, выданные в заданном диапазоне дат."""
    return [
        book
        for book in books
        if start_date <= book["issue_date"] <= end_date
    ]


def filter_books(books, author=None, start_date=None, end_date=None):
    """Комбинированная фильтрация по автору и диапазону дат выдачи."""
    result = books
    if author is not None:
        result = filter_by_author(result, author)
    if start_date is not None:
        result = filter_by_issue_date_range(result, start_date, end_date)
    return result


def example_usage():
    books = [
        {
            "title": "Война и мир",
            "author": "Толстой",
            "genre": "роман",
            "status": "выдана",
            "issue_date": date(2024, 1, 15),
            "due_date": date(2024, 2, 15),
        },
        {
            "title": "Мастер и Маргарита",
            "author": "Булгаков",
            "genre": "роман",
            "status": "выдана",
            "issue_date": date(2024, 3, 10),
            "due_date": date(2024, 4, 10),
        },
        {
            "title": "Анна Каренина",
            "author": "Толстой",
            "genre": "роман",
            "status": "выдана",
            "issue_date": date(2024, 5, 20),
            "due_date": date(2024, 6, 20),
        },
    ]

    print("Книги автора Толстой:")
    for book in filter_by_author(books, "Толстой"):
        print(f"  {book['title']} ({book['issue_date']})")

    print("Книги, выданные с 2024-03 по 2024-05:")
    for book in filter_by_issue_date_range(books, date(2024, 3, 1), date(2024, 5, 31)):
        print(f"  {book['title']} ({book['issue_date']})")

    print("Книги автора Толстой, выданные в 2024 году:")
    for book in filter_books(books, author="Толстой", start_date=date(2024, 1, 1), end_date=date(2024, 12, 31)):
        print(f"  {book['title']} ({book['issue_date']})")


if __name__ == "__main__":
    example_usage()
