import unittest
from models.book import Book
from models.user import User, Admin
from Service.library import Library


class TestBook(unittest.TestCase):

    def test_book_available_by_default(self):
        book = Book(1, "Clean Code", "Robert Martin")
        self.assertTrue(book.is_available())

    def test_book_set_unavailable(self):
        book = Book(1, "Clean Code", "Robert Martin")
        book.set_available(False)
        self.assertFalse(book.is_available())

    def test_book_to_dict(self):
        book = Book(1, "Clean Code", "Robert Martin", True)
        result = book.to_dict()
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["title"], "Clean Code")
        self.assertEqual(result["available"], True)
class TestUser(unittest.TestCase):

    def test_borrow_book(self):
        user = User(1, "Alice")
        user.borrow_book(101)
        self.assertIn(101, user.get_borrowed_books())

    def test_return_book(self):
        user = User(1, "Alice", [101])
        user.return_book(101)
        self.assertNotIn(101, user.get_borrowed_books())

    def test_borrow_same_book_twice(self):
        user = User(1, "Alice", [101])
        with self.assertRaises(ValueError):
            user.borrow_book(101)

    def test_return_book_not_borrowed(self):
        user = User(1, "Alice")
        with self.assertRaises(ValueError):
            user.return_book(999)
class TestAdmin(unittest.TestCase):

    def test_admin_role(self):
        admin = Admin(1, "Bob")
        self.assertEqual(admin.role, "admin")

    def test_admin_to_dict_has_role(self):
        admin = Admin(1, "Bob")
        result = admin.to_dict()
        self.assertEqual(result["role"], "admin")
class TestLibrary(unittest.TestCase):

    def setUp(self):
        books = [
            Book(1, "Clean Code", "Robert Martin", True),
            Book(2, "Python Crash Course", "Eric Mattes", False)
        ]
        users = [
            User(1, "Alice", [2]),
            User(2, "Bob")
        ]
        self.library = Library(books, users)

    def test_borrow_available_book(self):
        result = self.library.borrow_book(2, 1)
        self.assertTrue(result)

    def test_borrow_unavailable_book(self):
        result = self.library.borrow_book(2, 2)
        self.assertFalse(result)

    def test_return_book(self):
        result = self.library.return_book(1, 2)
        self.assertTrue(result)

    def test_borrow_nonexistent_book(self):
        result = self.library.borrow_book(1, 999)
        self.assertFalse(result)

    def test_borrow_nonexistent_user(self):
        result = self.library.borrow_book(999, 1)
        self.assertFalse(result)

    def test_get_available_books(self):
        available = list(self.library.get_available_books())
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].get_id(), 1)


if __name__ == "__main__":
    unittest.main()