from Service.file_service import load_books, save_books, load_users, save_users
from Service.library import Library
from utils.helpers import print_books, print_users, print_menu, get_int_input

BOOKS_FILE = "data/books.json"
USERS_FILE = "data/users.json"


def main():
    books = load_books(BOOKS_FILE)
    users = load_users(USERS_FILE)
    library = Library(books, users)

    while True:
        print_menu()
        choice = get_int_input("Enter choice: ")

        if choice == 1:
            print("\n--- All Books ---")
            print_books(library.get_all_books())

        elif choice == 2:
            print("\n--- Available Books ---")
            print_books(list(library.get_available_books()))

        elif choice == 3:
            print("\n--- Borrowed Books ---")
            print_books(list(library.get_borrowed_books()))

        elif choice == 4:
            user_id = get_int_input("Enter user ID: ")
            book_id = get_int_input("Enter book ID: ")
            library.borrow_book(user_id, book_id)
            save_books(BOOKS_FILE, library.get_all_books())
            save_users(USERS_FILE, library.get_all_users())

        elif choice == 5:
            user_id = get_int_input("Enter user ID: ")
            book_id = get_int_input("Enter book ID: ")
            library.return_book(user_id, book_id)
            save_books(BOOKS_FILE, library.get_all_books())
            save_users(USERS_FILE, library.get_all_users())

        elif choice == 6:
            user_id = get_int_input("Enter user ID: ")
            print("\n--- User History ---")
            print_books(library.get_user_history(user_id))

        elif choice == 7:
            print("\n--- All Users ---")
            print_users(library.get_all_users())

        elif choice == 0:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()