from abc import ABC, abstractmethod
from datetime import date


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"{self.title}, {self.author}, {self.year} год"

    def print_info(self):
        print(self.info())

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)

    @property
    def age(self):
        return date.today().year - self.year

    @classmethod
    def from_string(cls, text):
        title, author, year = (part.strip() for part in text.split(","))
        return cls(title, author, int(year))


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"{self.title}, {self.author}, {self.year} год, формат: {self.format}"


if __name__ == "__main__":
    book = Book.from_string("Война и мир, Лев Толстой, 1869")
    book.print_info()
    print(book.age)
    print(book == Book("Война и мир", "Лев Толстой", 1869))

    ebook = Ebook("Война и мир", "Лев Толстой", 1869, "EPUB")
    ebook.print_info()

    try:
        Printable()
    except TypeError as error:
        print(error)
