@app.route('/books')
def get_books():
    dao = BookDAO()
    books = dao.get_all_books()
    return {"books": books}

@app.route('/loans', methods=['POST'])
def create_loan():
    data = request.json
    dao = BookDAO()
    dao.create_loan(data['student_id'], data['book_id'])
    return {"status": "OK"}
