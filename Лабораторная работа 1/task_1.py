# TODO: Подробно описать три произвольных класса

class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "книга"

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц, должно быть положительным числом.
        :param ValueError: Если количество страниц меньше или равно 0.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self) -> str:
        """
        метод для получения краткого описания книги.

        :return: Описание в формате "Название: {title}, Автор: {author}, Страницы: {pages}".
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_summary()
        'Название: 1984, Автор: George Orwell, Страницы: 328'
        """
        return f"Название: {self.title}, Автор: {self.author}, Страницы: {self.pages}"

    def read_pages(self, number_of_pages: int) -> str:
        """
        Прочитать заданное количество страниц.

        :param number_of_pages: Количество страниц для чтения, должно быть положительным числом.
        :raises ValueError: Если количество страниц меньше или равно 0.
        :return: Строка с сообщением о прочитанных страницах.
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_pages(50)
        'Вы прочитали 50 страниц из 328.'
        """
        if number_of_pages <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным числом.")
        return f"Вы прочитали {number_of_pages} страниц из {self.pages}."



class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "автомобиль"

        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска, должен быть не меньше 1886 (первый год автомобиля).
        :raises ValueError: Если год выпуска меньше 1886.
        """
        if year < 1886:
            raise ValueError("Год выпуска автомобиля не может быть менее 1886.")
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        """
        Получить информацию об автомобиле.

        :return: Строка с информацией о автомобиле.
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.get_info()
        'Toyota Camry, 2020'
        """
        return f"{self.make} {self.model}, {self.year}"

    def update_year(self, new_year: int) -> None:
        """
        Обновить год выпуска автомобиля.

        :param new_year: Новый год выпуска, должен быть не меньше 1886.
        :raises ValueError: Если новый год меньше 1886.
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.update_year(2021)
        >>> car.get_info()
        'Toyota Camry, 2021'
        """
        if new_year < 1886:
            raise ValueError("Год выпуска автомобиля не может быть менее 1886.")
        self.year = new_year


class Person:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "человек"

        :param name: Имя человека.
        :param age: Возраст человека, должен быть неотрицательным.
        :raises ValueError: Если возраст отрицательный.
        """
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.name = name
        self.age = age

    def celebrate_birthday(self) -> None:
        """
        Отметить день рождения и увеличить возраст на 1 год.
        >>> p = Person("Alice", 30)
        >>> p.celebrate_birthday()
        >>> p.age
        31
        """
        self.age += 1

    def get_info(self) -> str:
        """
        Получить информацию о человеке.

        :return: Строка с информацией о человеке.
        >>> p = Person("Alice", 30)
        >>> p.get_info()
        'Имя: Alice, Возраст: 30'
        """
        return f"Имя: {self.name}, Возраст: {self.age}"