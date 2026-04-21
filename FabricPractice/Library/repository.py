from abc import ABC, abstractmethod
from typing import List, Optional
from bookAbstract import Book


class BookRepository(ABC):
    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Book]:
        pass

    @abstractmethod
    def delete(self, title: str) -> None:
        pass