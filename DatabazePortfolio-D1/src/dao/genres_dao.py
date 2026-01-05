import oracledb
from dao.base_dao import BaseDAO
from models.Genre import Genre

class GenresDAO(BaseDAO):
    def get_all(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM genres")
        rows = cursor.fetchall()
        genres = [Genre(id=row[0], name=row[1]) for row in rows]
        cursor.close()
        conn.close()
        return genres

    def get_by_id(self, genre_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM genres WHERE id = :id", {'id': genre_id})
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Genre(id=row[0], name=row[1])
        return None

    def insert(self, genre):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO genres (name) VALUES (:name)", {'name': genre.name})
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, genre):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE genres SET name = :name WHERE id = :id", {'name': genre.name, 'id': genre.id})
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, genre_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM genres WHERE id = :id", {'id': genre_id})
        conn.commit()
        cursor.close()
        conn.close()