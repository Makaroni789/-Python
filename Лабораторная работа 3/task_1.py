class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name  # Присваиваем значения параметров name и author защищённым атрибутам (с двойным подчеркиванием) класса, чтобы предотвратить их изменение.
        self.__author = author

    @property  # позволяет создать только геттеры, без сеттеров это делает атрибуты name и author неизменяемыми после инициализации
    def name(self):
        # свойство для имени книги
        return self.__name

    @property
    def author(self):
        # свойство для автора книги
        return self.__author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book): # Применяем наследование
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author) # Вызываем конструктор родительского класса Book для инициализации name и author.
        self.pages = pages # Устанавливаем значение для атрибута pages, используя соответствующее свойство.

    @property
    def pages(self):
        # свойство для количества страниц
        return self.__pages

    @pages.setter
    def pages(self, value:int):
        # Декоратор @pages.setter позволяет задать значение для pages.
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.__pages = value

    def __str__(self): # Переопределяем метод __str__ для отображения информации о бумажной книге.
        # Вызываем __str__ родительского класса и добавляем информацию о количестве страниц.
        return f"{super().__str__()}, Страницы: {self.pages}"

    def __repr__(self): # Переопределяем метод __repr__.
        # Возвращаем строку с названием, автором и страницами книги.
        return f'PaperBook(name={self.name}, author={self.author}, pages={self.pages})'

class AudioBook(Book): # Определяем класс AudioBook, который также наследует от Book.
    def __init__(self, name: str, author: str, duration: float): # Конструктор этого класса принимает название, автора и продолжительность книги.
        super().__init__(name, author) # Вызываем конструктор родительского класса для инициализации name и author.
        self.duration = duration # будет вызван сеттер duration

    @property
    def duration(self): # Свойство для продолжительности аудиокниги
        return self.__duration

    @duration.setter
    def duration(self, value):
        # сеттер для задания продолжительности с проверками
        if not isinstance(value, (float, int)): # Проверяем, что value является числом (целым или с плавающей запятой). Если нет, выбрасывается ошибка.
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:  # Проверяем, чтобы значение было положительным. В противном случае выбрасываем ValueError.
            raise ValueError("Продолжительность должна быть положительной")
        self.__duration = value


    def __str__(self): # Переопределяем метод __str__ для аудиокниги.
        # Вызываем __str__ родительского класса и добавляем информацию о длительности.
        return f'{super().__str__()}, Длительность: {self.duration}'

    def __repr__(self): # Переопределяем метод __repr__.
        # Возвращаем строку с названием, автором и длительностью книги.
        return f'AudioBook(name={self.name}, author={self.author}, duration={self.duration})'
