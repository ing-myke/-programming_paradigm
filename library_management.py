library_management.py
# library_management.py

class Book:
    """Represents a book with a title, author, and availability status."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned."""
        self._is_checked_out = False

    def is_available(self) -> bool:
        """Checks if the book is available."""
        return not self._is_checked_out

class Library:
    """
    Manages a collection of books, including adding, checking out, and returning books.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        """Adds a Book instance to the library's collection."""
        self._books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title: str):
        """
        Finds a book by title and checks it out if available.
        """
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Successfully checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Error: '{title}' was not found in the library.")

    def return_book(self, title: str):
        """
        Finds a book by title and returns it to the library.
        """
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Successfully returned '{title}'.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Error: '{title}' was not found in the library.")

    def list_available_books(self):
        """
        Prints a list of all books that are currently available.
        """
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_count += 1
        if available_count == 0:
            print("No books are currently available.")

