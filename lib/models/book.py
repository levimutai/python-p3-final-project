from models.__init__ import CURSOR, CONN
from models.author import Author

class Book:
    all = {}

    def __init__(self, title, genre, author_id, id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.author_id = author_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str) and len(genre):
            self._genre = genre
        else:
            raise ValueError("Genre must be a non-empty string")

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        if isinstance(author_id, int) and Author.find_by_id(author_id):
            self._author_id = author_id
        else:
            raise ValueError("author_id must reference an author in the database")

    def __repr__(self):
        return f"<Book {self.id}: {self.title}, {self.genre}, Author: {self.author_id}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            genre TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS books;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO books (title, genre, author_id) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.title, self.genre, self.author_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, genre, author_id):
        book = cls(title, genre, author_id)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.genre = row[2]
            book.author_id = row[3]
        else:
            book = cls(row[1], row[2], row[3])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM books"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM books WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def delete(self):
        sql = "DELETE FROM books WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    def author(self):
        return Author.find_by_id(self.author_id)