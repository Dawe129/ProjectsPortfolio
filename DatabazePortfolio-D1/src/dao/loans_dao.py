import oracledb
from dao.base_dao import BaseDAO
from models.Loan import Loan

class LoansDAO(BaseDAO):
    def get_all(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, student_id, book_id, loan_date, return_date FROM loans")
        rows = cursor.fetchall()
        loans = [Loan(id=row[0], student_id=row[1], book_id=row[2], loan_date=row[3], return_date=row[4]) for row in rows]
        cursor.close()
        conn.close()
        return loans

    def get_by_id(self, loan_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, student_id, book_id, loan_date, return_date FROM loans WHERE id = :id", {'id': loan_id})
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Loan(id=row[0], student_id=row[1], book_id=row[2], loan_date=row[3], return_date=row[4])
        return None

    def insert(self, loan):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO loans (student_id, book_id, loan_date, return_date) VALUES (:student_id, :book_id, :loan_date, :return_date)", 
                       {'student_id': loan.student_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date})
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, loan):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE loans SET student_id = :student_id, book_id = :book_id, loan_date = :loan_date, return_date = :return_date WHERE id = :id", 
                       {'student_id': loan.student_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date, 'id': loan.id})
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, loan_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM loans WHERE id = :id", {'id': loan_id})
        conn.commit()
        cursor.close()
        conn.close()