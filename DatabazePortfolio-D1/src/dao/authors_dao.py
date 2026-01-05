import oracledb
from dao.base_dao import BaseDAO
from models.Author import Author

class AuthorsDAO(BaseDAO):
    def get_all(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, birth_date, rating FROM authors")
        rows = cursor.fetchall()
        authors = [Author(id=row[0], name=row[1], birth_date=row[2], rating=row[3]) for row in rows]
        cursor.close()
        conn.close()
        return authors

    def get_by_id(self, author_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, birth_date, rating FROM authors WHERE id = :id", {'id': author_id})
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Author(id=row[0], name=row[1], birth_date=row[2], rating=row[3])
        return None

    def insert(self, author):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name, birth_date, rating) VALUES (:name, :birth_date, :rating)", 
                       {'name': author.name, 'birth_date': author.birth_date, 'rating': author.rating})
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, author):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE authors SET name = :name, birth_date = :birth_date, rating = :rating WHERE id = :id", 
                       {'name': author.name, 'birth_date': author.birth_date, 'rating': author.rating, 'id': author.id})
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, author_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id = :id", {'id': author_id})
        conn.commit()
        cursor.close()
        conn.close()