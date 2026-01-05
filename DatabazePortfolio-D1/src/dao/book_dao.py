import oracledb
from dao.base_dao import BaseDAO
from models.Book import Book

class BookDAO(BaseDAO):
    def get_all(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, genre_id, price, available FROM books")
        rows = cursor.fetchall()
        books = [Book(id=row[0], title=row[1], author_id=row[2], genre_id=row[3], price=row[4], available=row[5]) for row in rows]
        cursor.close()
        conn.close()
        return books

    def get_by_id(self, book_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, genre_id, price, available FROM books WHERE id = :id", {'id': book_id})
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Book(id=row[0], title=row[1], author_id=row[2], genre_id=row[3], price=row[4], available=row[5])
        return None

    def insert(self, book):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author_id, genre_id, price, available) VALUES (:title, :author_id, :genre_id, :price, :available)", 
                       {'title': book.title, 'author_id': book.author_id, 'genre_id': book.genre_id, 'price': book.price, 'available': book.available})
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, book):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title = :title, author_id = :author_id, genre_id = :genre_id, price = :price, available = :available WHERE id = :id", 
                       {'title': book.title, 'author_id': book.author_id, 'genre_id': book.genre_id, 'price': book.price, 'available': book.available, 'id': book.id})
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, book_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = :id", {'id': book_id})
        conn.commit()
        cursor.close()
        conn.close()

    def get_available_books(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT b.title, a.name author, g.name genre, b.available FROM books b JOIN authors a ON b.author_id = a.id JOIN genres g ON b.genre_id = g.id WHERE b.available = 1")
        rows = cursor.fetchall()
        books = [{"title": row[0], "author": row[1], "genre": row[2], "available": row[3]} for row in rows]
        cursor.close()
        conn.close()
        return books
