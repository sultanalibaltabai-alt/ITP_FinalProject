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