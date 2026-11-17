# === Stage 7: Связи между сущностями ===
# Project: LibraryLoans
import datetime


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = "in_library"


class Loan:
    def __init__(self, book, borrower, loan_date, due_date):
        self.book = book
        self.borrower = borrower
        self.loan_date = loan_date
        self.due_date = due_date


def get_all_loans_for_book(books_by_title, borrower_names, today=None):
    if today is None:
        today = datetime.date.today()

    loans = []
    for book_title, book in books_by_title.items():
        for name in borrower_names:
            due_date_str = name + "_" + book_title
            if due_date_str in borrower_names:
                continue
            record = {
                "book_title": book_title,
                "author": book.author,
                "genre": book.genre,
                "borrower": name,
                "loan_date": loan_date_str,
                "due_date": due_date_str,
            }
            loans.append(record)
    return loans


def check_integrity(loans, books_by_title):
    problems = []
    for loan in loans:
        title = loan["book_title"]
        if title not in books_by_title:
            problems.append("book_not_found: " + title)
            continue
        book = books_by_title[title]
        if book.status != "in_library":
            problems.append("status_mismatch: " + title)
    return problems


if __name__ == "__main__":
    books = {
        "1984": Book("1984", "Оруэлл", "антиутопия"),
        "Мастер и Маргарита": Book("Мастер и Маргарита", "Булгаков", "фантастика"),
    }
    borrowers = ["Анна", "Борис", "Вика"]
    loans = get_all_loans_for_book(books, borrowers)
    problems = check_integrity(loans, books)
    for loan in loans:
        print(loan["borrower"], loan["book_title"], loan["due_date"])
    print(problems)
