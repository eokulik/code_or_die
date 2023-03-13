
class Library:
    material = 'бумага'
    text = True

    def __init__(self, title, author, pages, ISBN):
        self.title = title
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.reserved = False  # default value for the "reserved" flag

    def __str__(self):
        if self.reserved:
            return f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}, Зарезервирована"
        else:
            return f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}"


# create 5 instances of the Book class
book1 = Library("Мастер и Маргарита", "Михаил Булгаков", 352, "9785389108313")
book2 = Library("451° по Фаренгейту", "Рэй Брэдбери", 256, "9785171202347")
book3 = Library("Каласы пад сярпом тваім", "Уладзімір Караткевіч", 928, "978-985-15-5237-1")
book4 = Library("Roma.A Novel Of Ancient Rome", "Steven Saylor", 598, "978-1250000606")
book5 = Library("1984-ieji", "George Orwell", 256, "9789955135005")

# mark books as reserved
book2.reserved = True
book5.reserved = True

print(book1)
print(book2)
print(book3)
print(book4)
print(book5)
