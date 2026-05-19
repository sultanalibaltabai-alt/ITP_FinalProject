class Library:
    def __init__(self, books, users):
        self.books = {book.get_id(): book for book in books}
        self.users = {user.get_id(): user for user in users}

    def find_book(self, book_id):
        return self.books.get(book_id)

    def find_user(self, user_id):
        return self.users.get(user_id)

    def borrow_book(self, user_id, book_id):
        user = self.find_user(user_id)
        if user is None:
            print("User not found.")
            return False

        book = self.find_book(book_id)
        if book is None:
            print("Book not found.")
            return False

        if not book.is_available():
            print(f"Book '{book.get_title()}' is not available.")
            return False

        if book_id in user.get_borrowed_books():
            print(f"User already has this book.")
            return False

        book.set_available(False)
        user.borrow_book(book_id)
        print(f"'{book.get_title()}' successfully borrowed by {user.get_name()}.")
        return True

    def return_book(self, user_id, book_id):
        user = self.find_user(user_id)
        if user is None:
            print("User not found.")
            return False

        book = self.find_book(book_id)
        if book is None:
            print("Book not found.")
            return False

        if book_id not in user.get_borrowed_books():
            print(f"User does not have this book.")
            return False

        book.set_available(True)
        user.return_book(book_id)
        print(f"'{book.get_title()}' successfully returned by {user.get_name()}.")
        return True