# Aggregation is a relationship where: One object contains another object,
#             but both can exist independently.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_book(self):
        return [f"{book.title} For {book.auther}" for book in self.books]


class Book:
    def __init__(self, title, auther ):
        self.auther = auther
        self.title = title


library = Library("Yemen Official Library")
book1 = Book("Harry Potter", "Johnathan R kooky")
book2 = Book("Manage Your Money", "Robert Saki")

library.add_book(book1)
library.add_book(book2)


for book in library.list_book():
    print(book)