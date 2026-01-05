CREATE TABLE books (
    id NUMBER PRIMARY KEY,
    title VARCHAR2(100),
    author VARCHAR2(50),
    price NUMBER(6,2),
    available NUMBER(1) DEFAULT 1
);
