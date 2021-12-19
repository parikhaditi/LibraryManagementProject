import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('library_info.db')
cursor = conn.cursor()
logged_in_id = 0


def return_db():
    global id
    temp_id = 0
    global logged_in_id
    print("return-user-id", logged_in_id)

    bid = id.get()

    print(bid, end='--')
    print("return")

    try:
        # update entered book id's status as available and set user id = tempid
        for i in logged_in_id:
            temp_id = i[0]
        cursor.execute('''UPDATE Books SET Status = ?, User_id = ? WHERE Book_id = ? and Status = ? ''',
                       ("available", int(temp_id), int(bid), "no"))
        conn.commit()
        messagebox.showinfo('Success', "Book returned.")
        window.destroy()

    except:
        messagebox.showerror("Error", "Cannot return given book!")


def returnBooks():
    global id
    global window

    window = Tk()
    window.title('Library Management System - Return a Book')
    window.minsize(width=400, height=400)
    window.geometry("450x300")

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Return a Book", fg='black')
    headingLabel.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.5)

    L = Label(window, text="Enter Book id: ")
    L.place(relx=0.05, rely=0.4)

    id = Entry(window, width=5)
    id.place(relx=0.3, rely=0.4, relwidth=0.62,relheight=0.07)

    submitbtn = Button(window, text="Return", command=return_db, bg="#455A64", fg="blue")
    submitbtn.place(relx=0.60, rely=0.8, relwidth=0.30, relheight=0.08)

    print("return")