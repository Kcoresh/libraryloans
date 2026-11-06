# === Stage 3: Хранилище в памяти ===
# Project: LibraryLoans
in_memory_books.py

from typing import Dict, List, Optional


class Book:
    def __init__(self, title: str, author: str, genre: str):
        self.id: int = 0
        self.title: str = title
        self.author: str = author
        self.genre: str = genre
        self.status: str = "на полке"

    def __repr__(self) -> str:
        return f"<Book id={self.id!r} title={self.title!r} status={self.status!r}>"


class InMemoryBookStore:
    def __init__(self) -> None:
        self._next_id: int = 1
        self._books: Dict[int, Book] = {}

    def add_book(self, title: str, author: str, genre: str) -> Book:
        book = Book(title, author, genre)
        book.id = self._next_id
        self._next_id += 1
        self._books[book.id] = book
        return book

    def get_book(self, book_id: int) -> Optional[Book]:
        return self._books.get(book_id)

    def list_books(self) -> List[Book]:
        return list(self._books.values())
