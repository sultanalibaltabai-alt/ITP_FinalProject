# Library Management System

A command - line application for managing a library — books, users, borrowing and returning.

## Team Members
- Alikhan Smagul — models/ (Book, User, Admin)
- Ibray Muratbek — Service/file_service.py, utils/helpers.py
- Sultanali Baltabay — Service/library.py
- Rizabek Begen — main.py, tests/test_library.py

## Features

- OOP: classes Book, User, Admin with encapsulation, inheritance, polymorphism
- File handling: read and write JSON files (books.json, users.json)
- Error handling: exceptions for invalid operations (borrowing unavailable book, etc.)
- Generators: get_available_books and get_borrowed_books use yield
- Data structures: dictionaries for O(1) lookup, lists for borrowed books
- Unit testing: 15 tests with unittest
- Modular structure: models, Service, utils, tests

## How to Run

python main.py

## How to Run Tests

python -m unittest tests/test_library.py -v

## Project Structure

```
ITP_FinalProject/
├── models/
│   ├── book.py          # Book class
│   └── user.py          # User and Admin classes
├── Service/
│   ├── file_service.py  # reading and writing JSON files
│   └── library.py       # main logic: borrow, return, search
├── utils/
│   └── helpers.py       # terminal output helpers
├── tests/
│   └── test_library.py  # unit tests
├── data/
│   ├── books.json
│   └── users.json
└── main.py              # entry point
```
