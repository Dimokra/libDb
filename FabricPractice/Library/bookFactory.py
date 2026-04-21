from bookAbstract import Book
from books import ScienceBook, FictionalBook, ArtBook
from typing import Type


class BookFactory:

    _book_types: dict = {
        "fiction": FictionalBook,
        "science": ScienceBook,
        "art": ArtBook
    }

    @classmethod
    def create_book(cls, book_type: str, title: str, author: str, price: float, **kwargs) -> Book:

        book_type_lowercase = book_type.lower()

        if book_type_lowercase not in cls._book_types:
            raise ValueError(f"Неизвестный тип книги: {book_type}")

        book_class = cls._book_types[book_type_lowercase]

        return book_class(title=title, author=author, price=price, **kwargs)

    @classmethod
    def register_book_type(cls, type_name: str, book_class: Type[Book]):
        if not issubclass(book_class, Book):
            raise TypeError(f'{book_class.__name__} не наследует Book')

        cls._book_types[type_name.lower()] = book_class

    @classmethod
    def get_book_type_name(cls, book: Book) -> str:
        for type_name, book_class in cls._book_types.items():
            if isinstance(book, book_class):
                return type_name

        raise ValueError(f"Неизвестный тип книги: {type(book).__name__}")