class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name  # инициализируем защищенные атрибуты
        self._author = author

    @property
    def name(self):
        """Возвращает название книги."""
        return self._name

    @property
    def author(self):
        """Возвращает автора книги."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс. Бумажная книга."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    # 1 вариант: наследование метода __str__ (можно, но не совсем корректно)
    # перегрузка метода __repr__ из-за нового атрибута
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Дочерний класс. Аудио книга."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        """Возвращает длительность книги."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        """Устанавливает длительность книги."""
        if not isinstance(new_duration, float):
            raise TypeError("Длительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = new_duration

    # 2 вариант: перегрузка метода __str__ (с упоминанием типа книги и нового атрибута)
    def __str__(self):
        return f"Аудио книга {self.name}. Автор {self.author}. Длительность {self.duration}."

    # перегрузка метода __repr__ из-за нового атрибута
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
