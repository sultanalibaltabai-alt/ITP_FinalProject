class User:
    def __init__(self, user_id, name, borrowed_books=None):
        self.__user_id = user_id
        self.__name = name
        self.__borrowed_books = borrowed_books if borrowed_books is not None else []

    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_id):
        if book_id in self.__borrowed_books:
            raise ValueError(f"User already has book ID {book_id}")
        self.__borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id not in self.__borrowed_books:
            raise ValueError(f"User does not have book ID {book_id}")
        self.__borrowed_books.remove(book_id)

    def to_dict(self):
        return {
            "user_id": self.__user_id,
            "name": self.__name,
            "borrowed_books": self.__borrowed_books
        }

    def __str__(self):
        return f"[{self.__user_id}] {self.__name} | Borrowed: {self.__borrowed_books}"


class Admin(User):
    def __init__(self, user_id, name, borrowed_books=None):
        super().__init__(user_id, name, borrowed_books)
        self.role = "admin"

    def to_dict(self):
        data = super().to_dict()
        data["role"] = self.role
        return data

    def __str__(self):
        return f"[ADMIN] {super().__str__()}"