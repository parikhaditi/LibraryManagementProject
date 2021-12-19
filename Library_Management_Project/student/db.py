import sqlite3

name = 'nauka'
password = '12345'
role = 'student'
Title = 'book1'
Author = 'author1'
Status = 'available'
user_id = 1

conn = None
conn = sqlite3.connect('library_info.db')
conn.execute("PRAGMA foreign_keys = 1")
cur = conn.cursor()
try:
    cur.execute('''CREATE TABLE IF NOT EXISTS Users(User_id INTEGER PRIMARY KEY NOT NULL,
                                            Username TEXT UNIQUE,
                                            Password TEXT, 
                                            Role TEXT)''')
    conn.commit()

except sqlite3.Error as err:
    print('Database Error ', err)

print("creating another table..")
cur.execute('''CREATE TABLE IF NOT EXISTS Books(Book_id INTEGER PRIMARY KEY NOT NULL, Title TEXT,
                                            Author TEXT,
                                            Status TEXT,
                                            User_id INTEGER NOT NULL,
                                            FOREIGN KEY (User_id) REFERENCES Users (User_id)
                                            ON DELETE CASCADE
                                            ON UPDATE CASCADE)''')

# cur.execute('''INSERT INTO Users(Username, Password, Role)
#                               VALUES(?, ? , ?)''', (name, password, role))
#
# cur.execute('''INSERT INTO Users(Username, Password, Role)
#                               VALUES(?, ? , ?)''', ("Aditi", "67890", "student"))
#
# cur.execute('''INSERT INTO Books(Title, Author, Status, User_id)
#                                       VALUES(?, ? , ?, ?)''', (Title, Author, Status, user_id))

# cur.execute('''INSERT INTO Users(Username, Password, Role)
#                                VALUES(?, ? , ?)''', ("nauka_shah", "12345", "librarian"))
#
# cur.execute('''INSERT INTO Users(Username, Password, Role)
#                                VALUES(?, ? , ?)''', ("aditi_parikh", "67890", "librarian"))


conn.commit()