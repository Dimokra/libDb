from bookFactory import BookFactory
from dbRepository import DBRepository  # ⬅️ Импортируем из файла dbRepository.py


if __name__ == '__main__':
    try:
        repository = DBRepository()

    # Создаём книги
        book1 = BookFactory.create_book("fiction", "Дюна", "Фрэнк Герберт", 1200.0)
        book2 = BookFactory.create_book("science", "Космос", "Карл Саган", 950.0)
        book3 = BookFactory.create_book("art", "Искусство цвета", "Иоханнес Иттен", 1500.0)

        print("Добавляем книги в PostgreSQL")
        repository.add(book1)
        repository.add(book2)
        repository.add(book3)
        print("Книги добавлены!")

        print("\n Все книги в базе:")
        all_books = repository.get_all()
        for book in all_books:
            print(f"  - {book.get_info()}")

        print("\n Ищем 'Дюна'...")
        found = repository.get_by_title("Дюна")
        if found:
            print(f"✅ Найдено: {found.get_info()}")

        print("\n Удаляем 'Космос'")
        repository.delete("Космос")
        print("✅ Удалено!")

        print("\n Книги после удаления:")
        remaining = repository.get_all()
        for book in remaining:
            print(f"  - {book.get_info()}")
    
    except Exception as e:
        print(f"Ошибка: {e}")