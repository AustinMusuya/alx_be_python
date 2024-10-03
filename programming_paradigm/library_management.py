"""
Objective: Solidify understanding of basic OOP concepts in Python 
by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

Your Task: library_management.py
Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. 
Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
Provided for Testing: main.py
This script demonstrates how to interact with your Book and Library classes.

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()

Expected Outputs for Each Step in main.py:

After Initial Setup:
   Available books after setup:
   Brave New World by Aldous Huxley
   1984 by George Orwell
After Checking Out ‘1984’:
   Available books after checking out '1984':
   Brave New World by Aldous Huxley
After Returning ‘1984’:
   Available books after returning '1984':
   Brave New World by Aldous Huxley
   1984 by George Orwell

Note for you:

Your Book class should provide methods to check a book out and return it, affecting its availability.
Your Library class needs to manage a collection of books, 
including adding new books to the collection, checking a book out (which marks it as unavailable), 
returning it (making it available again), and listing all available books.
Implementing these functionalities requires careful thought about how objects interact with each other in terms of state and behavior.
Use the provided main.py for testing your implementation. 
The expected outputs give you a clear indication of how your program should behave if implemented correctly.


"""

"""
Objective: Solidify understanding of basic OOP concepts in Python 
by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

Your Task: library_management.py
Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.

Implement a Library class with a private list _books to store instances of Book. 
Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
Provided for Testing: main.py
This script demonstrates how to interact with your Book and Library classes.

"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self.book = book
        self._books.append(self.book)

    def check_out_book(self, title):
        self.title = title
        for book in self._books:
            if book.title == self.title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        self.title = title
        for book in self._books:
            if book.title == self.title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            return ("No books available in Library")
        else:
            for book in available_books:
                return f"{book.title} by {book.author}"


# library = Library()

# library.add_book(Book('Harry Potter', "J.K Rowlings"))
# library.add_book(Book('Song of Ice & Fire', "R.R Martin"))

# library.check_out_book("Harry Potter")

# print(library.list_available_books())
