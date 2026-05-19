def print_books(books):
    if not books:
        print("No books found.")
        return
    for book in books:
        print(book)


def print_users(users):
    if not users:
        print("No users found.")
        return
    for user in users:
        print(user)


def print_menu():
    print("\n=== Library Management System ===")
    print("1. Show all books")
    print("2. Show available books")
    print("3. Show borrowed books")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Show user history")
    print("7. Show all users")
    print("0. Exit")
    print("=================================")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")