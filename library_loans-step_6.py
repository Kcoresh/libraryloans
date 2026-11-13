# === Stage 6: Связанная сущность ===
# Project: LibraryLoans
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = "доступна"

    def lend(self, borrower):
        if self.status != "доступна":
            return False
        self.status = "выдана"
        return True

    def return_book(self):
        self.status = "доступна"


class Loan:
    def __init__(self, book_id, borrower, due_date):
        self.book_id = book_id
        self.borrower = borrower
        self.due_date = due_date
        self.returned = False

    def return_loan(self):
        self.returned = True

    def is_overdue(self):
        import datetime
        return datetime.date.today() > self.due_date


def add_loan(books, loan_id, book_id, borrower, due_date):
    if book_id not in books:
        raise KeyError(f"Книга с id {book_id} не найдена")
    books[book_id].status = "выдана"
    loan = Loan(book_id, borrower, due_date)
    books[book_id].loans.append(loan)
    return loan


def list_active_loans(books):
    active = []
    for book in books.values():
        for loan in book.loans:
            if not loan.returned:
                active.append(loan)
    return active
