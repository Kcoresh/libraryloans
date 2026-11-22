# === Stage 10: Сортировка записей ===
# Project: LibraryLoans
def sort_books_by_title(records, ascending=True):
    return sorted(records, key=lambda r: r['title'], reverse=not ascending)


def sort_books_by_created_at(records, ascending=True):
    return sorted(records, key=lambda r: r['created_at'], reverse=not ascending)


def sort_books_by_title_then_created(records, ascending=True):
    return sorted(
        records,
        key=lambda r: (r['title'], r['created_at']),
        reverse=not ascending,
    )


def sort_books(records, field='title', ascending=True):
    if field == 'title':
        return sort_books_by_title_then_created(records, ascending)
    raise ValueError(f'Неизвестное поле для сортировки: {field}')


if __name__ == '__main__':
    data = [
        {'title': 'Анна Каренина', 'created_at': '2024-01-05'},
        {'title': 'Мастер и Маргарита', 'created_at': '2024-01-02'},
        {'title': 'Преступление и наказание', 'created_at': '2024-01-10'},
    ]

    print('По названию (возрастание):')
    for book in sort_books(data, 'title', ascending=True):
        print(book['title'])

    print('По названию (убывание):')
    for book in sort_books(data, 'title', ascending=False):
        print(book['title'])

    print('По дате создания (возрастание):')
    for book in sort_books(data, 'created_at', ascending=True):
        print(book['title'])

    print('По названию, затем по дате (возрастание):')
    for book in sort_books(data, 'title', ascending=True):
        print(book['title'])
