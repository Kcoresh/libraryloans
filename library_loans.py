# === Stage 1: Каркас модуля ===
# Project: LibraryLoans
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Book:
    title: str
    author: str
    genre: str
    status: str = "available"

    def __str__(self):
        return f"{self.title} — {self.author} ({self.genre}, {self.status})"


def make_demo_books():
    return [
        Book("Мастер и Маргарита", "Михаил Булгаков", "Фантастика"),
        Book("1984", "Джордж Оруэлл", "Антиутопия"),
        Book("Война и мир", "Лев Толстой", "Роман"),
    ]


def main():
    library = make_demo_books()
    print("Добро пожаловать в LibraryLoans!")
    print("Ваша домашняя библиотека:")
    for book in library:
        print(f"  - {book}")
    print(f"Всего книг: {len(library)}")


if __name__ == "__main__":
    main()
