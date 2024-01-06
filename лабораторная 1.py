# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Paper:
    """Класс описывает модель листа бумаги."""
    def __init__(self, square: (int, float), occupied_square: (int, float)):
        """
        Инициализация экземпляра класса.
        : param square: Площадь листа бумаги.
        : param occupied_square: Занимаемая площадь на листе.
        Пример:
        >>> paper_1 = Paper(1000, 0)
        """
        if not isinstance(square, (int, float)):
            raise TypeError("Неправильный тип данных.")
        if occupied_square < 0:
            raise ValueError("Площадь не может быть отрицательной.")
        self.square = square

        if not isinstance(occupied_square, (int, float)):
            raise TypeError("Неправильный тип данных.")
        if occupied_square < 0:
            raise ValueError("Площадь не может быть отрицательной.")
        self.occupied_square = occupied_square

    def increment_occupied_square(self, increment_square: (int, float)):
        """
        Метод увеличивает занимаемую площадь на листе бумаги.
        : param increment_square: Добавляемая площадь.
        Пример:
        >>> paper_1 = Paper(1000, 0)
        >>> paper_1.increment_occupied_square(200)
        """
        if not isinstance(increment_square, (int, float)):
            raise TypeError("Неправильный тип данных.")
        if self.occupied_square + increment_square > self.square:
            raise ValueError("Занимаемая площадь на листе не должна превышать площадь листа.")
        self.occupied_square += increment_square

    def decrement_occupied_square(self, decrement_square: (int, float)):
        """
        Метод уменьшает занимаемую площадь на листе бумаги.
        : param decrement_square: Убираемая площадь.
        Пример:
        >>> paper_1 = Paper(1000, 800)
        >>> paper_1.decrement_occupied_square(200)
        """
        if not isinstance(decrement_square, (int, float)):
            raise TypeError("Неправильный тип данных.")
        if self.occupied_square - decrement_square < 0:
            raise ValueError("Убираемая площадь на листе не может быть больше занимаемой.")
        self.occupied_square -= decrement_square


class Fridge:
    """Класс описывает модель холодильника."""
    def __init__(self, company: str, volume: (int, float), occupied_volume: (int, float)):
        """
        Инициализация экземпляра класса.
        : param company: Фирма холодильника.
        : param volume: Объем холодильника.
        : param occupied_volume: Занимаемый объем.
        Пример:
        >>> fridge_1 = Fridge("Atlant", 300, 0)
        """
        if not isinstance(company, str):
            raise TypeError("Неправильный тип данных.")
        self.company = company

        if not isinstance(volume, (int, float)):
            raise TypeError("Неправильный тип данных.")
        if occupied_volume < 0:
            raise ValueError("Объем не может быть отрицательным.")
        self.volume = volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Неправильный тип данных.")
        if occupied_volume < 0:
            raise ValueError("Объем не может быть отрицательным.")
        self.occupied_volume = occupied_volume

    def increment_occupied_volume(self, increment_volume: (int, float)):
        """
        Метод увеличивает занимаемый объем в холодильнике.
        : param increment_volume: Добавляемый объем.
        Пример:
        >>> fridge_1 = Fridge("Atlant", 300, 0)
        >>> fridge_1.increment_occupied_volume(200)
        """
        if not isinstance(increment_volume, (int, float)):
            raise TypeError("Неправильный тип данных.")
        if self.occupied_volume + increment_volume > self.volume:
            raise ValueError("Занимаемый объем не должен превышать объем холодильника.")
        self.occupied_volume += increment_volume

    def decrement_occupied_volume(self, decrement_volume: (int, float)):
        """
        Метод уменьшает занимаемый объем в холодильнике.
        : param decrement_volume: Убираемый объем.
        Пример:
        >>> fridge_1 = Fridge("Atlant", 300, 200)
        >>> fridge_1.decrement_occupied_volume(100)
        """
        if not isinstance(decrement_volume, (int, float)):
            raise TypeError("Неправильный тип данных.")
        if self.occupied_volume - decrement_volume < 0:
            raise ValueError("Убираемый объем в холодильнике не может быть больше занимаемого.")
        self.occupied_volume -= decrement_volume


class Messenger:
    """Класс описывает модель мессенджера."""
    def __init__(self, title: str, users: int, new_users: int):
        """
        Инициализация экземпляра класса.
        : param title: Название мессенджера.
        : param users: Количество пользователей.
        : param new_users: Количество новых пользователей.
        Пример:
        >>> messenger_1 = Messenger("Одноклассники", 3000000, 100)
        """
        if not isinstance(title, str):
            raise TypeError("Неправильный тип данных.")
        self.title = title

        if not isinstance(users, int):
            raise TypeError("Неправильный тип данных.")
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.users = users

        if not isinstance(new_users, int):
            raise TypeError("Неправильный тип данных.")
        if new_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.new_users = new_users

    def increment_new_users(self, increment_users: int):
        """
        Метод увеличивает количество пользователей мессенджера.
        : param increment_users: Прирост пользователей.
        Пример:
        >>> messenger_1 = Messenger("Одноклассники", 3000000, 0)
        >>> messenger_1.increment_new_users(200)
        """
        if not isinstance(increment_users, int):
            raise TypeError("Неправильный тип данных.")
        self.new_users += increment_users

    def decrement_users(self, decrement_us: int):
        """
        Метод уменьшает количество пользователей мессенджера.
        : param decrement_us: Убыль пользователей.
        Пример:
        >>> messenger_1 = Messenger("Одноклассники", 3000000, 0)
        >>> messenger_1.decrement_users(200)
        """
        if not isinstance(decrement_us, int):
            raise TypeError("Неправильный тип данных.")
        if self.users - decrement_us < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.users -= decrement_us


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров из документации
