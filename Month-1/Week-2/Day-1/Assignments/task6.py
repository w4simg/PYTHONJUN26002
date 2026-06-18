# Task 6: Create a Book Class
# Requirements:
# - Use a constructor.
# - Accept: title, author, price.
# - Create a method called displayBook().

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def displayBook(self):
        print("Book Details:")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: Rs.", self.price)

# Create object
my_book = Book("Python Crash Course", "Eric Matthes", 1200)

# Display details
my_book.displayBook()
