# === Stage 12: Теги ===
# Project: LibraryLoans
class BookTag:
    def __init__(self, name):
        self.name = name.lower()


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.tags = []

    def add_tag(self, tag_name):
        new_tag = BookTag(tag_name)
        if new_tag not in self.tags:
            self.tags.append(new_tag)

    def remove_tag(self, tag_name):
        for tag in self.tags:
            if tag.name == tag_name.lower():
                self.tags.remove(tag)
                return True
        return False

    def find_by_tag(self, tag_name):
        for tag in self.tags:
            if tag.name == tag_name.lower():
                return tag
        return None


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_tag(self, tag_name):
        return [book for book in self.books if book.find_by_tag(tag_name)]
