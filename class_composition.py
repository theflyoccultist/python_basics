class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} Books."
    
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    
book = Book("The land is inhospitable")
book2 = Book("Charli")
shelf = Bookshelf(book, book2)

print(shelf)