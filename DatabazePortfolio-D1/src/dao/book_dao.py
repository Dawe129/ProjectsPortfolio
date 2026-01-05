import oracledb
from dao.base_dao import BaseDAO

class BookDAO(BaseDAO):
    def get_all_books(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM available_books")
        books = [{"title": row[0], "author": row[1], "genre": row[2]} for row in cursor]
        cursor.close()
        conn.close()
        return books
    
    def create_loan(self, student_id, book_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO loans (student_id, book_id) VALUES (:1, :2)",
            (student_id, book_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
