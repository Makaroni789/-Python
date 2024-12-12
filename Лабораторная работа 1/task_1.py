# TODO: Подробно описать три произвольных класса
import doctest

class Artist:
    def __init__(self, name: str, genre: str, albums: int):
        """Инициализируем объект Artist.

        :param name: имя артиста (не может быть пустым).
        :param genre: жанр музыки (не может быть пустым).
        :param albums: количество альбомов (должно быть неотрицательным).
        """
        if not name or not genre:
            raise ValueError("Имя и жанр не могут быть пустыми строками.")
        if albums < 0:
            raise ValueError("Количество альбомов не может быть отрицательным.")

        self.name = name
        self.genre = genre
        self.albums = albums

    def get_info(self) -> str:
        """Возвращает информацию об артистe.

        :return: строка с информацией об артисте.

        >>> artist = Artist("Би-2", "Рок", 10)
        >>> artist.get_info()
        'Артист: Би-2, жанр: Рок, альбомов: 10'
        """
        return f'Артист: {self.name}, жанр: {self.genre}, альбомов: {self.albums}'

    def change_genre(self, new_genre: str) -> None:
        """Меняет жанр артиста на новый.

        :param new_genre: новый жанр (не может быть пустым).

        >>> artist = Artist("Би-2", "Рок", 10)
        >>> artist.change_genre("Поп")
        """
        if not new_genre:
            raise ValueError("Новый жанр не может быть пустым.")
        self.genre = new_genre


class Garden:
    def __init__(self, area: float, flower_count: int):
        if area <= 0:
            raise ValueError("Площадь сада должна быть больше 0 квадратных метров")
        if flower_count < 0:
            raise ValueError("Количество цветов не может быть отрицательным")
        self.area = area
        self.flower_count = flower_count

    def plant_flowers(self, count: int) -> str:
        """Сажает указанное количество цветов.

        :param count: количество цветов для посадки.
        :return: сообщение о новом количестве цветов.
        Примеры:
        >>> garden = Garden(100, 10)
        >>> garden.plant_flowers(5)
        'Теперь в саду 15 цветов.'
        """
        if count < 1:
            raise ValueError("Количество цветов должно быть положительным")
        self.flower_count += count
        return f"Теперь в саду {self.flower_count} цветов."

    def harvest(self, count: int) -> str:
        """Собирает указанное количество цветов.

        :param count: количество цветов для сбора.
        :return: сообщение о новом количестве цветов.
        Примеры:
        >>> garden = Garden(100, 10)
        >>> garden.harvest(5)
        'Теперь в саду 5 цветов.'
        """
        if count < 1:
            raise ValueError("Количество собираемых цветов должно быть положительным")
        if count > self.flower_count:
            raise ValueError("Невозможно собрать больше цветов, чем есть")
        self.flower_count -= count
        return f"Теперь в саду {self.flower_count} цветов."

    def check_area(self) -> float:
        """Метод для получения площади сада.

        :return: площадь сада в квадратных метрах.
        Примеры:
        >>> garden = Garden(100, 10)
        >>> garden.check_area()
        100
        """
        return self.area



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

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
