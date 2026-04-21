from bookAbstract import Book
from bookCollection import BookCollection

class BookCollectionBuilder:

    def __init__(self):
        self._collection = BookCollection()

    def add_book(self, book: Book):
        self._collection.add_book(book)
        return self

    def set_theme(self, theme: str):
        self._collection._theme = theme
        return self

    def set_price(self, price: float = 0.0):
        self._collection.custom_price = price
        return self

    def build(self) -> BookCollection:
        return self._collection