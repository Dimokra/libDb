from bookAbstract import Book


class FictionalBook(Book):

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def get_price(self) -> float:
        return self._price

    def get_info(self) -> str:
        return f'Фантастика: {self._title} - {self._author} ({self._price} руб.)'


class ScienceBook(Book):

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def get_price(self) -> float:
        return self._price

    def get_info(self) -> str:
        return f'Научная: {self._title} - {self._author} ({self._price} руб.)'


class ArtBook(Book):

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def get_price(self) -> float:
        return self._price

    def get_info(self) -> str:
        return f'Искусство: {self._title} - {self._author} ({self._price} руб.)'