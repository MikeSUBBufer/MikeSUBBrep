class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def set_name(self):
        return self._name

    @property
    def set_author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, _pages: int):
        super().__init__(name, author)
        self._pages = None

    @property
    def set_pages(self):
        return self._pages

    @set_pages.setter
    def set_pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError("Kоличество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Kоличество страниц должно быть больше 0")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, _duration: float):
        if not isinstance(_duration, int):
            raise TypeError("Длителность должна быть типа float")
        if _duration <= 0:
            raise ValueError("Длительность должна быть больше 0")
        self._duration = _duration


if __name__ == '__main__':
    book = AudioBook('1', 2, -1.1)
    print(book.duration)