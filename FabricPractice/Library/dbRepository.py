import psycopg2
from typing import List, Optional
from psycopg2.extras import execute_batch, RealDictCursor

from repository import BookRepository
from bookFactory import BookFactory
from bookAbstract import Book
from config import POSTGRES_CONFIG

class DBRepository(BookRepository): 
    def __init__(self):
        try:
            self.connection = psycopg2.connect(**POSTGRES_CONFIG)
            self.create_table()
        except psycopg2.OperationalError as e:
            print(f"Ошибка подключения: {e}")
            print("Проверьте параметры в config.py")
            print("Сервер PostgreSQL запущен")
            print("Пароль и имя базы в config.py верны")
            raise 
        

    def __del__(self):
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()

    def create_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    type VARCHAR(50) NOT NULL,
                    title VARCHAR(255) NOT NULL,
                    author VARCHAR(255) NOT NULL,
                    price NUMERIC(10, 2) NOT NULL
                )
            ''')
            self.connection.commit()

    def add(self, book: Book) -> None:
        book_type = BookFactory.get_book_type_name(book)
        
        with self.connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO books (type, title, author, price)
                VALUES (%s, %s, %s, %s)
            ''', (book_type, book.get_title(), book.get_author(), book.get_price()))
            
            self.connection.commit()

    def add_many(self, books: List[Book]) -> None:
        books_data = [
            (BookFactory.get_book_type_name(book), 
             book.get_title(), 
             book.get_author(), 
             book.get_price())
            for book in books
        ]
        
        with self.connection.cursor() as cursor:
            execute_batch(cursor, '''
                INSERT INTO books (type, title, author, price)
                VALUES (%s, %s, %s, %s)
            ''', books_data)
            
            self.connection.commit()

    def get_all(self) -> List[Book]:
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()

        books = []
        for row in rows:
            book = BookFactory.create_book(
                row['type'], 
                row['title'], 
                row['author'], 
                float(row['price'])
            )
            books.append(book)
        
        return books

    def get_by_title(self, title: str) -> Optional[Book]:
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT * FROM books WHERE title = %s", 
                (title,)
            )
            row = cursor.fetchone()

        if row:
            return BookFactory.create_book(
                row['type'], 
                row['title'], 
                row['author'], 
                float(row['price'])
            )
        return None

    def delete(self, title: str) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM books WHERE title = %s", (title,))
            self.connection.commit()