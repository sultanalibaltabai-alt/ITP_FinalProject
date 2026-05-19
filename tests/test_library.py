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