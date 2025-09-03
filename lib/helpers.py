from models.author import Author
from models.book import Book

def exit_program():
    print("Goodbye!")
    exit()

# Author helpers
def list_authors():
    authors = Author.get_all()
    if authors:
        for author in authors:
            print(f"{author.id}. {author.name} (Born: {author.birth_year})")
    else:
        print("No authors found.")

def find_author_by_id():
    id_ = input("Enter author's id: ")
    try:
        author = Author.find_by_id(int(id_))
        if author:
            print(f"Found: {author.name} (Born: {author.birth_year})")
        else:
            print(f"Author {id_} not found")
    except ValueError:
        print("Invalid id. Please enter a number.")

def create_author():
    name = input("Enter author's name: ")
    birth_year = input("Enter birth year: ")
    try:
        author = Author.create(name, int(birth_year))
        print(f"Success: Created author {author.name}")
    except ValueError as exc:
        print(f"Error creating author: {exc}")

def delete_author():
    id_ = input("Enter author's id: ")
    try:
        author = Author.find_by_id(int(id_))
        if author:
            author.delete()
            print(f"Author {id_} deleted")
        else:
            print(f"Author {id_} not found")
    except ValueError:
        print("Invalid id. Please enter a number.")

def list_author_books():
    id_ = input("Enter author's id: ")
    try:
        author = Author.find_by_id(int(id_))
        if author:
            books = author.books()
            if books:
                print(f"Books by {author.name}:")
                for book in books:
                    print(f"  - {book.title} ({book.genre})")
            else:
                print(f"{author.name} has no books.")
        else:
            print(f"Author {id_} not found")
    except ValueError:
        print("Invalid id. Please enter a number.")

# Book helpers
def list_books():
    books = Book.get_all()
    if books:
        for book in books:
            author = book.author()
            print(f"{book.id}. {book.title} ({book.genre}) by {author.name}")
    else:
        print("No books found.")

def find_book_by_id():
    id_ = input("Enter book's id: ")
    try:
        book = Book.find_by_id(int(id_))
        if book:
            author = book.author()
            print(f"Found: {book.title} ({book.genre}) by {author.name}")
        else:
            print(f"Book {id_} not found")
    except ValueError:
        print("Invalid id. Please enter a number.")

def create_book():
    title = input("Enter book title: ")
    genre = input("Enter genre: ")
    print("Available authors:")
    list_authors()
    author_id = input("Enter author id: ")
    try:
        book = Book.create(title, genre, int(author_id))
        print(f"Success: Created book {book.title}")
    except ValueError as exc:
        print(f"Error creating book: {exc}")

def delete_book():
    id_ = input("Enter book's id: ")
    try:
        book = Book.find_by_id(int(id_))
        if book:
            book.delete()
            print(f"Book {id_} deleted")
        else:
            print(f"Book {id_} not found")
    except ValueError:
        print("Invalid id. Please enter a number.")