BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """Класс описывает модель книги."""
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация экземпляра класса.
        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id_ = id_
        self.name = name
        self.pages = pages


class Library:
    """Класс описывает модель библиотеки."""
    def __init__(self, books=[]):
        """
        Инициализация экземпляра класса.
        :param books: Список книг.
        По умолчанию параметр равен пустому списку.
        """
        self.books = books

    def get_next_book_id(self):
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку."""
        if self.books == []:
            return 1  # Книга будет первой в пустом списке
        else:
            max_id = 1
            for i in self.books:
                if i.id_ > max_id:
                    max_id = i.id_
            return max_id + 1

    def get_index_by_book_id(self, id_):
        """
        Метод, возвращающий индекс книги в списке,
        который хранится в атрибуте экземпляра класса.
        """
        for index, value in enumerate(self.books):
            if value.id_ == id_:
                return index
        else:
            raise ValueError("Книга с запрашиваемым id не существует")


if __name__ == '__main__':
    # Инициализируем пустую библиотеку
    empty_library = Library()
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Инициализируем библиотеку с книгами
    library_with_books = Library(books=list_books)

    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1
