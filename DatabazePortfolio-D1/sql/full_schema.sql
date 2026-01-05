CREATE TABLE authors (
  id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR2(100) NOT NULL,
  birth_date DATE,
  rating FLOAT(2,1) CHECK(rating >=0 AND rating <=5)
);

CREATE TABLE genres (
  id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR2(20) CHECK(name IN ('Fantasy','SciFi','Thriller','Romance'))
);

CREATE TABLE books (
  id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  title VARCHAR2(200) NOT NULL,
  author_id NUMBER REFERENCES authors(id),
  genre_id NUMBER REFERENCES genres(id),
  price FLOAT(6,2),
  available NUMBER(1) DEFAULT 1
);

CREATE TABLE students (
  id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR2(100),
  active NUMBER(1) DEFAULT 1
);

CREATE TABLE loans (
  id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  student_id NUMBER REFERENCES students(id),
  book_id NUMBER REFERENCES books(id),
  loan_date DATE DEFAULT SYSDATE,
  return_date DATE
);

CREATE OR REPLACE VIEW available_books AS
SELECT b.title, a.name author, g.name genre, b.available
FROM books b 
JOIN authors a ON b.author_id = a.id
JOIN genres g ON b.genre_id = g.id;

CREATE OR REPLACE VIEW student_stats AS
SELECT s.name, COUNT(l.id) loans, AVG(b.price) avg_price
FROM students s 
LEFT JOIN loans l ON s.id = l.student_id
LEFT JOIN books b ON l.book_id = b.id
GROUP BY s.id, s.name;
