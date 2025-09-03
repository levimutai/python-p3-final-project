# Library Management System CLI

A command-line interface application for managing a library's authors and books, built with Python and SQLite.

## Features

- **Author Management**: Create, view, update, and delete authors
- **Book Management**: Create, view, update, and delete books
- **Relationship Tracking**: View all books by a specific author
- **Input Validation**: Comprehensive error handling and data validation
- **Interactive Menus**: User-friendly navigation system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/levimutai/python-p3-final-project.git
cd python-p3-final-project
```

2. Install dependencies:
```bash
pipenv install
pipenv shell
```

3. Run the application:
```bash
python lib/cli.py
```

## Usage

The CLI provides an interactive menu system:

### Main Menu
- **Author Management**: Access all author-related operations
- **Book Management**: Access all book-related operations
- **Exit**: Close the application

### Author Operations
- List all authors
- Find author by ID
- Create new author
- Delete author
- View author's books

### Book Operations
- List all books
- Find book by ID
- Create new book
- Delete book

## Project Structure

```
.
├── Pipfile
├── README.md
└── lib/
    ├── models/
    │   ├── __init__.py     # Database connection
    │   ├── author.py       # Author model with ORM methods
    │   └── book.py         # Book model with ORM methods
    ├── cli.py              # Main CLI interface
    ├── helpers.py          # Helper functions for CLI operations
    └── debug.py            # Debug script for testing
```

## Models

### Author
- **Attributes**: name (string), birth_year (integer)
- **Relationships**: One-to-many with Books
- **Validations**: Name must be non-empty string, birth year must be > 1000

### Book
- **Attributes**: title (string), genre (string), author_id (foreign key)
- **Relationships**: Many-to-one with Author
- **Validations**: Title and genre must be non-empty strings, author_id must reference existing author

## Database Schema

```sql
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name TEXT,
    birth_year INTEGER
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);
```

## Key Files

### `lib/cli.py`
The main entry point of the application. Contains the interactive menu system and navigation logic. Initializes database tables and provides separate menus for author and book management.

### `lib/helpers.py`
Contains all the helper functions that handle user input, data validation, and database operations. Each function corresponds to a specific CLI operation like creating, reading, updating, or deleting records.

### `lib/models/author.py`
Defines the Author class with full ORM functionality including property validation, CRUD operations, and relationship methods. Includes methods for creating, finding, updating, and deleting authors, as well as retrieving associated books.

### `lib/models/book.py`
Defines the Book class with full ORM functionality and foreign key relationship to Author. Includes property validation and all standard CRUD operations.

### `lib/debug.py`
A debugging script that creates sample data and opens an interactive debugger for testing the models and their relationships.

## Requirements Met

✅ **ORM Requirements**:
- Database created with Python ORM methods
- 2 model classes (Author, Book)
- One-to-many relationship (Author → Books)
- Property methods with validation constraints
- Full CRUD operations for each model

✅ **CLI Requirements**:
- Interactive menus with user navigation
- Loops to keep user in application
- CRUD operations for each model class
- Input validation and error handling
- Clean separation of concerns

✅ **Code Quality**:
- Follows OOP best practices
- Organized file structure
- Appropriate imports
- Comprehensive README documentation