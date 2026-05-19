from Service.file_service import load_books, save_books, load_users, save_users
from Service.library import Library
from utils.helpers import print_books, print_users, print_menu, get_int_input

BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"


def main():
    books = load_books(BOOKS_FILE)
    users = load_users(USERS_FILE)
    library = Library(books, users)

