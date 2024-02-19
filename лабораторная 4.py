class Store:
    """Базовый класс магазина одежды, обуви и аксессуаров."""
    def __init__(self, name: str, clothes: list, shoes: list, accessories: list, review_list: list = None,
                 workers_dict: dict = None):
        """
        Инициализация экземпляра класса.
        :param name: Название магазина.
        :param clothes: Список одежды.
        :param shoes: Список обуви.
        :param accessories: Список аксессуаров.
        :param review_list: Список отзывов.
        :param workers_dict: Словарь персонала.

        Пример:
        >>> store = Store('Mon Shu-Shu', ['пиджаки', 'брюки'], ['туфли', 'ботинки'], ['очки', 'часы'])
        """
        self._name = name
        self._clothes = clothes
        self._shoes = shoes
        self._accessories = accessories
        self.review_list = review_list
        self.workers_dict = workers_dict

    @property
    def name(self) -> str:
        """Возвращает название магазина. Защищенный атрибут доступен только для чтения."""
        return self._name

    @property
    def clothes(self) -> list:
        """Возвращает список одежды."""
        return self._clothes

    @clothes.setter
    def clothes(self, new_clothes: list):
        """Устанавливает список одежды в магазине. Защищенный атрибут доступен для изменения пользователем."""
        if not isinstance(new_clothes, list):
            raise TypeError("Список одежды должен быть типа list")
        self._clothes = new_clothes

    @property
    def shoes(self) -> list:
        """Возвращает список обуви."""
        return self._shoes

    @shoes.setter
    def shoes(self, new_shoes: list):
        """Устанавливает список обуви в магазине. Защищенный атрибут доступен для изменения пользователем."""
        if not isinstance(new_shoes, list):
            raise TypeError("Список обуви должен быть типа list")
        self._clothes = new_shoes

    @property
    def accessories(self) -> list:
        """Возвращает название магазина."""
        return self._accessories

    @accessories.setter
    def accessories(self, new_accessories: list):
        """Устанавливает список аксессуаров в магазине. Защищенный атрибут доступен для изменения пользователем."""
        if not isinstance(new_accessories, list):
            raise TypeError("Список аксессуаров должен быть типа list")
        self._clothes = new_accessories

    def __str__(self) -> str:
        """Возвращает строковое представление экземпляра класса."""
        return f'Магазин одежды, обуви и аксессуаров "{self.name}".'

    def __repr__(self) -> str:
        """Возвращает строку, содержащую валидный код для инициализации экземпляра класса."""
        return (f'{self.__class__.__name__}(name={self.name!r}, clothes={self.clothes!r}, shoes={self.shoes!r}, '
                f'accessories={self.accessories!r}, review_list={self.review_list!r})')

    def write_review(self):
        """Метод, позволяющий оставлять отзывы о магазине."""
        if not self.review_list:
            self.review_list = []
        review = input('Пожалуйста, напишите отзыв 0_0 !\n')
        self.review_list.append(review)

    def add_workers_dict(self):
        """Метод, позволяющий создать словарь персонала магазина."""
        if not self.workers_dict:
            self.workers_dict = {}
        workers = input('Введите имена персонала магазина через пробел в следующем порядке: Директор, '
                        'Менеджер по закупкам, Бухгалтер\n')
        workers_list = workers.split()
        self.workers_dict = {'Директор': workers_list[0],
                             'Менеджер по закупкам': workers_list[1],
                             'Бухгалтер': workers_list[2]}


class OnlineStore(Store):
    """Дочерний класс. Онлайн-магазин."""
    def __init__(self, name: str, clothes: list, shoes: list, accessories: list, discounts: int, delivery: str,):
        """
        Инициализация экземпляра класса.
        :param discounts: Скидка на первый заказ.
        :param delivery: Способ доставки.

        Пример:
        >>> store = OnlineStore('Солнце', ['пиджаки', 'брюки'], ['туфли', 'ботинки'], ['очки', 'часы'], 20, 'почта')
        """
        super().__init__(name, clothes, shoes, accessories)
        self._discounts = discounts
        self._delivery = delivery

    @property
    def discounts(self) -> int:
        """Возвращает значение скидки на первый заказ. Защищенный атрибут доступен только для чтения."""
        return self._discounts

    @property
    def delivery(self) -> str:
        """Возвращает способ доставки. Защищенный атрибут доступен только для чтения."""
        return self._delivery

    def __str__(self) -> str:
        """Перегрузка метода __str__. Обновление строкового представления экземпляра класса."""
        return (f'Онлайн-магазин "{self.name}". Способ доставки заказов: {self.delivery}. '
                f'На первый заказ скидка {self.discounts} %!')

    def __repr__(self) -> str:
        """Перегрузка метода __repr__. Добавление новых атрибутов в дочернем классе."""
        return (f'{self.__class__.__name__}(name={self.name!r}, clothes={self.clothes!r}, shoes={self.shoes!r}, '
                f'accessories={self.accessories!r}, discounts={self.discounts!r}, delivery={self.delivery!r}, '
                f'review_list={self.review_list!r})')

    # Метод write_review наследуется без изменений.

    def add_workers_dict(self):
        """Перегрузка метода add_workers_dict. Добавление нового персонала."""
        super().add_workers_dict()
        workers = input('Введите имена персонала магазина через пробел в следующем порядке: Менеджер по продажам,'
                        ' Программист, Сборщик заказов\n')
        workers_list = workers.split()
        self.workers_dict['Менеджер по продажам'] = workers_list[0]
        self.workers_dict['Программист'] = workers_list[1]
        self.workers_dict['Сборщик заказов'] = workers_list[2]


class SecondHand(Store):
    """Дочерний класс. Секонд-хенд."""
    def __init__(self, name: str, clothes: list, shoes: list, accessories: list, degree_of_wear: int,
                 weight_zone: str):
        """
        Инициализация экземпляра класса.
        :param degree_of_wear: Степень износа.
        :param weight_zone: Цена на овещи в весовой зоне.

        Пример:
        >>> store = SecondHand('Луна', ['пиджаки', 'брюки'], ['туфли', 'ботинки'], ['очки', 'часы'], 30, '999 руб/кг')
        """
        super().__init__(name, clothes, shoes, accessories)
        self._degree_of_wear = degree_of_wear
        self._weight_zone = weight_zone

    @property
    def degree_of_wear(self) -> int:
        """Возвращает значение степени износа. Защищенный атрибут доступен только для чтения."""
        return self._degree_of_wear

    @property
    def weight_zone(self) -> str:
        """Возвращает цену на вещи в весовой зоне. Защищенный атрибут доступен только для чтения."""
        return self._weight_zone

    def __str__(self) -> str:
        """Перегрузка метода __str__. Обновление строкового представления экземпляра класса."""
        return (f'Секонд-хенд "{self.name}". Весовая зона: {self.weight_zone}. '
                f'Принимаем одежду и обувь со степенью износа не более {self.degree_of_wear} %!')

    def __repr__(self) -> str:
        """Перегрузка метода __repr__. Добавление новых атрибутов в дочернем классе."""
        return (f"{self.__class__.__name__}(name={self.name!r}, clothes={self.clothes!r}, shoes={self.shoes!r}, "
                f"accessories={self.accessories!r}, weight_zone={self.weight_zone!r}, "
                f"degree_f_wear={self.degree_of_wear!r}, review_list={self.review_list!r})")

    # Метод write_review наследуется без изменений.

    def add_workers_dict(self):
        """Перегрузка метода add_workers_dict. Добавление нового персонала."""
        super().add_workers_dict()
        workers = input('Введите имена персонала магазина через пробел в следующем порядке: Администратор,'
                        ' Продавец-консультант, Охранник\n')
        workers_list = workers.split()
        self.workers_dict['Администратор'] = workers_list[0]
        self.workers_dict['Продавец-консультант'] = workers_list[1]
        self.workers_dict['Охранник'] = workers_list[2]


if __name__ == "__main__":
    #store = Store('Mon Shu-Shu', ['пиджаки', 'брюки'], ['туфли', 'ботинки'], ['очки', 'часы'])
    #store_online = OnlineStore('Солнце', ['пиджаки', 'брюки'], ['туфли', 'ботинки'], ['очки', 'часы'], 20, 'почта')

    store_second = SecondHand('Луна', ['пиджаки', 'брюки'], ['туфли', 'ботинки'],
                              ['очки', 'часы'], 30, '999 руб/кг')
    print(str(store_second))
    print(repr(store_second))
    store_second.write_review()
    print(store_second.review_list)
    store_second.add_workers_dict()
    print(store_second.workers_dict)
