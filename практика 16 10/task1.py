class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"{self.title}, {self.author}, {self.year} год"


if __name__ == "__main__":
    book = Book("Война и мир", "Лев Толстой", 1869)
    print(book.info())
