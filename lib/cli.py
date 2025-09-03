from helpers import (
    exit_program,
    list_authors, find_author_by_id, create_author, delete_author, list_author_books,
    list_books, find_book_by_id, create_book, delete_book
)
from models.author import Author
from models.book import Book

def main():
    # Initialize database tables
    Author.create_table()
    Book.create_table()
    
    print("Welcome to Library Management System!")
    
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            author_menu()
        elif choice == "2":
            book_menu()
        else:
            print("Invalid choice")

def menu():
    print("\n=== MAIN MENU ===")
    print("0. Exit the program")
    print("1. Author Management")
    print("2. Book Management")

def author_menu():
    while True:
        print("\n=== AUTHOR MANAGEMENT ===")
        print("0. Back to main menu")
        print("1. List all authors")
        print("2. Find author by id")
        print("3. Create new author")
        print("4. Delete author")
        print("5. List author's books")
        
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_authors()
        elif choice == "2":
            find_author_by_id()
        elif choice == "3":
            create_author()
        elif choice == "4":
            delete_author()
        elif choice == "5":
            list_author_books()
        else:
            print("Invalid choice")

def book_menu():
    while True:
        print("\n=== BOOK MANAGEMENT ===")
        print("0. Back to main menu")
        print("1. List all books")
        print("2. Find book by id")
        print("3. Create new book")
        print("4. Delete book")
        
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_books()
        elif choice == "2":
            find_book_by_id()
        elif choice == "3":
            create_book()
        elif choice == "4":
            delete_book()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()