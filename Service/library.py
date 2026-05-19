class Library:
    def __init__(self, books, users):
        self.books = {book.get_id(): book for book in books}
        self.users = {user.get_id(): user for user in users}

    def find_book(self, book_id):
        return self.books.get(book_id)

    def find_user(self, user_id):
        return self.users.get(user_id)