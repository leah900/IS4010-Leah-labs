# lab06.py

class Book:
    """
    A class representing a book with a title, author, and publication year.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.
        """
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the book.
        
        Returns:
            str: Formatted string with title, author, and year.
        """
        return f'"{self.title}" by {self.author} ({self.year})'

    def get_age(self) -> int:
        """
        Calculate and return the age of the book assuming the current year is 2025.
        
        Returns:
            int: Age of the book in years.
        """
        CURRENT_YEAR: int = 2025
        return CURRENT_YEAR - self.year


class EBook(Book):
    """
    A class representing an electronic book (EBook), inheriting from Book.
    
    Attributes:
        file_size (int): File size of the ebook in megabytes.
    """

    def __init__(self, title: str, author: str, year: int, file_size: int) -> None:
        """
        Initialize an EBook instance, extending the Book class with file_size.
        
        Args:
            title (str): The title of the ebook.
            author (str): The author of the ebook.
            year (int): The year the ebook was published.
            file_size (int): The size of the ebook file in MB.
        """
        super().__init__(title, author, year)
        self.file_size: int = file_size

    def __str__(self) -> str:
        """
        Return a string representation including file size in MB.
        
        Returns:
            str: Formatted string with book info and file size.
        """
        return f"{super().__str__()} ({self.file_size} MB)"


if __name__ == "__main__":
    # --- Book Test ---
    book_example: Book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(book_example)            # "The Hobbit" by J.R.R. Tolkien (1937)
    print(f"Age: {book_example.get_age()} years")  # Age: 88 years

    # --- EBook Test ---
    ebook_example: EBook = EBook("Dune", "Frank Herbert", 1965, 5)
    print(ebook_example)           # "Dune" by Frank Herbert (1965) (5 MB)
    print(f"Age: {ebook_example.get_age()} years")  # Age: 60 years
