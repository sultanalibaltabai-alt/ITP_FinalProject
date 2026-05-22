import json
from models.book import Book
from models.user import User, Admin


def load_books(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

    books = []
    for item in data:
        books.append(Book(item["id"], item["title"], item["author"], item["available"]))
    return books


def save_books(filepath, books):
    data = []
    for book in books:
        data.append(book.to_dict())

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def load_users(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

    users = []
    for item in data:
        if item.get("role") == "admin":
            users.append(Admin(item["user_id"], item["name"], item.get("borrowed_books", [])))
        else:
            users.append(User(item["user_id"], item["name"], item.get("borrowed_books", [])))
    return users


def save_users(filepath, users):
    data = []
    for user in users:
        data.append(user.to_dict())

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)