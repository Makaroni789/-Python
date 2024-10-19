# TODO Найдите количество книг, которое можно разместить на дискете
size_of_diskette = 1.44
pages = 100
strings = 50
symbols = 25
size_of_symbol = 4
size_of_book_in_mb = (size_of_symbol * symbols * strings * pages) / 1024 / 1024
books_in_one_diskette = int(size_of_diskette // size_of_book_in_mb)
print("Количество книг, помещающихся на дискету:", books_in_one_diskette)