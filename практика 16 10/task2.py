class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"{self.title}, {self.author}, {self.year} год"


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"{self.title}, {self.author}, {self.year} год, формат: {self.format}"


if __name__ == "__main__":
    ebook = Ebook("Война и мир", "Лев Толстой", 1869, "EPUB")
    print(ebook.info())
