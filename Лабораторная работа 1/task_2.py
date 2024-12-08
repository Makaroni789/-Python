from task_1 import Book, Car, Person

# Класс Book
try:
    book = Book("1984", "George Orwell", 328)
    print(book.get_summary())  # Ожидается: Название: 1984, Автор: George Orwell, Страницы: 328
    print(book.read_pages(50))  # Ожидается: Вы прочитали 50 страниц из 328.

    # Проверяем валидацию в методе read_pages
    book.read_pages(-5)  # Это должно вызвать ValueError
except ValueError as e:
    print(f"Ошибка при чтении страниц: {e}")

# Класс Car
try:
    car = Car("Toyota", "Camry", 2020)
    print(car.get_info())  # Ожидается: Toyota Camry, 2020

    car.update_year(2021)  # Ожидается обновление года
    print(car.get_info())  # Ожидается: Toyota Camry, 2021

    # Проверяем валидацию в методе update_year
    car.update_year(1800)  # Это должно вызвать ValueError
except ValueError as e:
    print(f"Ошибка при обновлении года: {e}")

# Класс Person
try:
    person = Person("Alice", 30)
    print(person.get_info())  # Ожидается: Имя: Alice, Возраст: 30
    person.celebrate_birthday()  # Ожидается увеличение возраста на 1
    print(person.get_info())  # Ожидается: Имя: Alice, Возраст: 31

    # Проверяем валидацию в конструкторе
    person_invalid = Person("Bob", -1)  # Это должно вызвать ValueError
except ValueError as e:
    print(f"Ошибка при создании человека: {e}")
