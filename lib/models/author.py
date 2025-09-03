from models.__init__ import CURSOR, CONN

class Author:
    all = {}

    def __init__(self, name, birth_year, id=None):
        self.id = id
        self.name = name
        self.birth_year = birth_year

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, birth_year):
        if isinstance(birth_year, int) and birth_year > 1000:
            self._birth_year = birth_year
        else:
            raise ValueError("Birth year must be an integer > 1000")

    def __repr__(self):
        return f"<Author {self.id}: {self.name}, {self.birth_year}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            birth_year INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS authors;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = "INSERT INTO authors (name, birth_year) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.birth_year))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, birth_year):
        author = cls(name, birth_year)
        author.save()
        return author

    @classmethod
    def instance_from_db(cls, row):
        author = cls.all.get(row[0])
        if author:
            author.name = row[1]
            author.birth_year = row[2]
        else:
            author = cls(row[1], row[2])
            author.id = row[0]
            cls.all[author.id] = author
        return author

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM authors"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM authors WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def delete(self):
        sql = "DELETE FROM authors WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    def books(self):
        from models.book import Book
        sql = "SELECT * FROM books WHERE author_id = ?"
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Book.instance_from_db(row) for row in rows]