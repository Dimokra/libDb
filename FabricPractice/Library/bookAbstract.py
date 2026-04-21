from abc import ABC, abstractmethod

class Book(ABC):

    def __init__(self, title: str, author: str, price: float):
        self._title = title
        self._author = author
        self._price = price

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_author(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass