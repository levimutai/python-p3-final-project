#!/usr/bin/env python3
import ipdb
from models.author import Author
from models.book import Book

if __name__ == '__main__':
    # Initialize database
    Author.create_table()
    Book.create_table()
    
    # Create sample data
    author1 = Author.create("J.K. Rowling", 1965)
    author2 = Author.create("George Orwell", 1903)
    
    book1 = Book.create("Harry Potter", "Fantasy", author1.id)
    book2 = Book.create("1984", "Dystopian", author2.id)
    
    ipdb.set_trace()