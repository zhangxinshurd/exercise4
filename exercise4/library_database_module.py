import sqlite3

def create_database():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT NOT NULL,
        status TEXT NOT NULL
    )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Reservations (
        reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (book_id) REFERENCES Books (book_id),
        FOREIGN KEY (user_id) REFERENCES Users (user_id)
    )''')

    connection.commit()
    connection.close()

def get_book_detail(book_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT status FROM Books WHERE book_id=?", (book_id,))
    status = cursor.fetchone()[0]
    if status == "On the shelf":
        cursor.execute("SELECT * FROM Books WHERE book_id=?", (book_id,))
    else:
        cursor.execute('''SELECT books.*, users.* FROM Books
                    Inner Join Reservations ON Books.book_id = Reservations.book_id 
                    Inner Join Users ON Reservations.user_id = Users.user_id WHERE Books.book_id=?''', (book_id,))
    books = cursor.fetchall()
    connection.close()
    return books

def get_books_detail():
    connection = sqlite3.connect("library.db")
    cursor1 = connection.cursor()
    cursor2=connection.cursor()
    cursor1.execute("SELECT * FROM Books where status='On the shelf'")
    cursor2.execute('''SELECT books.*, users.* FROM Books
                   Inner Join Reservations ON Books.book_id = Reservations.book_id 
                   Inner Join Users ON Reservations.user_id = Users.user_id''')
    books = cursor1.fetchall()+cursor2.fetchall()
    connection.close()
    return books

def add_book(title, author, isbn):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    status="On the shelf"
    cursor.execute("INSERT INTO Books (title, author, isbn, status) VALUES (?, ?, ?, ?)", (title, author, isbn, status))
    connection.commit()
    connection.close()


def add_user(name, email):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (name, email) VALUES (?, ?)", (name, email))
    connection.commit()
    connection.close()

def add_reservation(book_id, user_id, status):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Reservations (book_id, user_id, status) VALUES (?, ?, ?)", (book_id, user_id, status))
    connection.commit()
    connection.close()

def get_books():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    connection.close()
    return books

def get_book(book_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Books WHERE book_id=?", (book_id,))
    book = cursor.fetchone()
    connection.close()
    return book


def get_reservations():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Reservations")
    reservations = cursor.fetchall()
    connection.close()
    return reservations

def get_book(book_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Books WHERE book_id=?", (book_id,))
    book = cursor.fetchone()
    connection.close()
    return book


def get_reservation_by_id(reservation_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Reservations WHERE reservation_id=?", (reservation_id,))
    reservation = cursor.fetchone()
    connection.close()
    return reservation

def get_reservation_by_user(user_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Reservations WHERE user_id=?", (user_id,))
    reservations = cursor.fetchall()
    connection.close()
    return reservations

def get_reservation_by_book(book_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Reservations WHERE book_id=?", (book_id,))
    reservations = cursor.fetchall()
    connection.close()
    return reservations

def get_reservation_by_title(title):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE title=?", (title,))
    id = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM Reservations WHERE book_id=?", (id,))
    reservations = cursor.fetchall()
    connection.close()
    return reservations

def update_book(book_id, title, author, isbn):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Books SET title=?, author=?, isbn=? WHERE book_id=?", (title, author, isbn, book_id))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0

def update_book_status(book_id, title, author, isbn, status, user_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    if status == "On reservation":
        cursor.execute("UPDATE Books SET title=?, author=?, isbn=?, status=? WHERE book_id=?", (title, author, isbn, status, book_id))
        cursor.execute("INSERT INTO Reservations (book_id, user_id, status) VALUES (?, ?, ?)", (book_id, user_id, status))
    else:
        cursor.execute("UPDATE Books SET title=?, author=?, isbn=?, status=? WHERE book_id=?", (title, author, isbn, status, book_id))
        cursor.execute("DELETE FROM Reservations WHERE book_id=?", (book_id,))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0

def update_reservation(reservation_id, book_id, user_id, status):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Reservations SET book_id=?, user_id=?, status=? WHERE reservation_id=?", (book_id, user_id, status, reservation_id))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0

def delete_book(book_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Books Inner Join Reservations on books.book_id = reservations.book_id  WHERE book_id=? ", (book_id,))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0

def delete_reservation(reservation_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Reservations WHERE reservation_id=?", (reservation_id,))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0
