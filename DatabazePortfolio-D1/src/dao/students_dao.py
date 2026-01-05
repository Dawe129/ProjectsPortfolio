import oracledb
from dao.base_dao import BaseDAO
from models.Student import Student

class StudentsDAO(BaseDAO):
    def get_all(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, active FROM students")
        rows = cursor.fetchall()
        students = [Student(id=row[0], name=row[1], active=row[2]) for row in rows]
        cursor.close()
        conn.close()
        return students

    def get_by_id(self, student_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, active FROM students WHERE id = :id", {'id': student_id})
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Student(id=row[0], name=row[1], active=row[2])
        return None

    def insert(self, student):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, active) VALUES (:name, :active)", {'name': student.name, 'active': student.active})
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, student):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name = :name, active = :active WHERE id = :id", {'name': student.name, 'active': student.active, 'id': student.id})
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, student_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = :id", {'id': student_id})
        conn.commit()
        cursor.close()
        conn.close()