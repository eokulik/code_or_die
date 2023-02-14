class Book:
    material = 'paper'
    text_presence = True

    def __init__(self, book_name: str, author, number_of_pages: int, isbn, reserved=False):
        self.name = book_name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def print_book_info(self):
        if self.reserved is True:
            print('Name:', self.name, ', Author:', self.author,
                  ', Pages:', self.number_of_pages, ', Material:', self.material, ', the book is reserved')
        else:
            print('Name:', self.name, ', Author:', self.author,
                  ', Pages:', self.number_of_pages, ', Material:', self.material)


idiot = Book('Idiot', 'Fyodor Dostoyevsky', 500, '978-3-16-148410-1')
novel_1984 = Book('1984', 'George Orwell', 320, '978-3-17-153212-3')
algernon_flowers = Book('Flowers for Algernon', 'Daniel Keyes', 382, '978-5-699-55699-1')
google_testing = Book('How Google Tests Software', 'James Whittaker', 320, '978-0321803023')

idiot.reserved = True

idiot.print_book_info()
novel_1984.print_book_info()
algernon_flowers.print_book_info()
google_testing.print_book_info()
