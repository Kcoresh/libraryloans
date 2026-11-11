# === Stage 5: Удаление и восстановление ===
# Project: LibraryLoans
import uuid
from datetime import datetime


class Book:
    def __init__(self, title, author, genre, status="на полке"):
        self.id = uuid.uuid4().hex
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def delete(self):
        self.status = "удалена"
        self.deleted_at = datetime.now()

    def restore(self):
        if self.status == "удалена":
            self.status = "на полке"
            self.deleted_at = None
        else:
            raise ValueError("Книга не была удалена")

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title!r}, status={self.status!r})"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.id] = book

    def get_book(self, book_id):
        return self.books.get(book_id)

    def delete_book(self, book_id):
        book = self.books.get(book_id)
        if book:
            book.delete()
            return True
        return False

    def restore_book(self, book_id):
        book = self.books.get(book_id)
        if book and book.status == "удалена":
            book.restore()
            return True
        return False

    def active_books(self):
        return [b for b in self.books.values() if b.status != "удалена"]
