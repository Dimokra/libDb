from typing import List
from bookAbstract import Book


class BookCollection(Book):
    def __init__(self, theme: str = "Без темы"):
        super().__init__(title=theme, author="Коллекция", price=0.0)
        self._books: List[Book] = []
        self._theme: str = theme
        self.custom_price: float = 0.0

    def add_book(self, book: Book):
        self._books.append(book)

    def get_title(self) -> str:
        return self._theme

    def get_author(self) -> str:
        authors = [book.get_author() for book in self._books]
        return ', '.join(sorted(set(authors)))

    def get_price(self) -> float:
        if self.custom_price > 0:
            return self.custom_price
        return sum(book.get_price() for book in self._books)

    def get_info(self) -> str:
        info = f'Коллекция: {self._theme}\n'
        info += f'Цена: {self.get_price()} руб.\n'
        info += f'Количество книг: {len(self._books)}\n'
        info += f'Авторы: {self.get_author()}\n'
        info += '\nКниги:\n'

        for i, book in enumerate(self._books, 1):
            info += f'  {i}. {book.get_title()} ({book.get_author()}) - {book.get_price()} руб.\n'

        return info


class BookCollectionBuilder:

    def __init__(self):
        self._collection = BookCollection()

    def add_book(self, book: Book):
        self._collection.add_book(book)
        return self

    def set_theme(self, theme: str):
        self._collection._theme = theme
        return self

    def set_custom_price(self, price: float):
        self._collection.custom_price = price
        return self

    def build(self) -> BookCollection:
        return self._collection