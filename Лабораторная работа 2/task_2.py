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


# TODO: написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

# TODO: написать класс Library
class Library:
    def __init__(self, books=None): # инициализируем books, который по умолчанию является пустым списком.
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self): # Метод get_next_book_id возвращает следующий идентификатор для добавления новой книги в библиотеку.
        if not self.books:
            return 1
        else:
            return max(book.id for book in self.books) + 1 #Если в списке уже есть книги, метод находит максимальный идентификатор среди существующих
            # И возвращает максимальный id + 1, что будет идентификатором для следующей добавляемой книги.

    def get_index_by_book_id(self, book_id): # Метод get_index_by_book_id, который принимает целое число book_id и возвращает индекс книги в списке self.books.
        for index, book in enumerate(self.books): # используем функция enumerate, которая позволяет итерировать по списку книг с получением как самих объектов book, так и их индексов index.
            if book.id == book_id: # Если идентификатор книги (book.id) совпадает с переданным book_id, метод возвращает текущий индекс index этой книги.
                return index
        raise ValueError("Книги с запрашиваемым id не существует") # Если цикл завершился и никакая книга не была найдена с запрашиваемым id, вызывается ошибка


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
