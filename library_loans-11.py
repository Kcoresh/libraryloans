# === Stage 11: Поиск по нескольким словам ===
# Project: LibraryLoans
from typing import List, Dict


def parse_query(query: str) -> List[str]:
    tokens = query.replace("-", " -").split()
    return [token for token in tokens if token != ""]


def extract_exclusions(query: str) -> List[str]:
    tokens = parse_query(query)
    exclusions = []
    for token in tokens:
        if token.startswith("-"):
            exclusions.append(token[1:])
    return exclusions


def extract_inclusions(query: str) -> List[str]:
    tokens = parse_query(query)
    return [token for token in tokens if not token.startswith("-")]


def search_books(query: str, books: List[Dict[str, str]]) -> List[Dict[str, str]]:
    exclusions = extract_exclusions(query)
    inclusions = extract_inclusions(query)
    results = []
    for book in books:
        haystack = " ".join(
            [book.get("title", ""), book.get("author", ""), book.get("genre", "")]
        ).lower()
        if any(exclusion.lower() in haystack for exclusion in exclusions):
            continue
        if any(inclusion.lower() not in haystack for inclusion in inclusions):
            continue
        results.append(book)
    return results


if __name__ == "__main__":
    sample_books = [
        {"title": "Мастер и Маргарита", "author": "Булгаков", "genre": "Фантастика"},
        {"title": "Преступление и наказание", "author": "Достоевский", "genre": "Детектив"},
        {"title": "Война и мир", "author": "Толстой", "genre": "История"},
        {"title": "1984", "author": "Оруэлл", "genre": "Фантастика"},
    ]
    print(search_books("фантастика -орuell", sample_books))
    print(search_books("романтик", sample_books))
