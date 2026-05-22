class Book:
    def __init__(self, book_id, title, author, available=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available = available

    def get_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def set_available(self, value):
        self.__available = value

    def to_dict(self):
        return {
            "id": self.__book_id,
            "title": self.__title,
            "author": self.__author,
            "available": self.__available
        }

    def __str__(self):
        status = "Available" if self.__available else "Borrowed"
        return f"[{self.__book_id}] '{self.__title}' by {self.__author} - {status}"