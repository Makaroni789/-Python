from task_1 import Artist, Garden, Person

# Класс Garden
try:
    garden = Garden(100, 10)
    print(garden.plant_flowers(5))  # Ожидается: Теперь в саду 15 цветов.
    print(garden.harvest(5))  # Ожидается: Теперь в саду 5 цветов.
    print(f"Площадь сада: {garden.check_area()}")  # Ожидается: 100
    # Проверяем валидацию в методе harvest
    print(garden.harvest(15))  # Ожидается исключение, нельзя собрать больше, чем есть
except ValueError:
    print('Ошибка: неправильные данные')

# Класс Artist
try:
    artist = Artist("Би-2", "Рок", 10)
    print(artist.get_info())  # Ожидается: Артист: Би-2, жанр: Рок, альбомов: 10

    artist.change_genre("Поп")
    print(artist.get_info())  # Ожидается: Артист: Би-2, жанр: Поп, альбомов: 10

    # Проверяем валидацию в методе change_genre
    artist.change_genre("")  # Ожидается исключение, Новый жанр не может быть пустым.
except ValueError:
    print('Ошибка: неправильные данные')

# Класс Person
try:
    person = Person("Alice", 30)
    print(person.get_info())  # Ожидается: Имя: Alice, Возраст: 30
    person.celebrate_birthday()  # Ожидается увеличение возраста на 1
    print(person.get_info())  # Ожидается: Имя: Alice, Возраст: 31

    # Проверяем валидацию в конструкторе
    person_invalid = Person("Bob", -1)  # Это должно вызвать ValueError
except ValueError as e:
    print('Ошибка: неправильные данные')
