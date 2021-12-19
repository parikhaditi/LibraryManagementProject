from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('library_info.db')
cursor = conn.cursor()


def delete_db():
    global id

    bid = id.get()

    print(bid, end='--')
    print("delete")

    try:
        print(bid)
        if bid == '':
            messagebox.showinfo('Input required', "please enter book id to delete")
        else:
            cursor.execute('''DELETE FROM Books WHERE Book_id = ?''', (bid,))
            conn.commit()
            messagebox.showinfo('Success', "Book deleted")
            window.destroy()

    except:
        messagebox.showerror("Error", "Book with given id does not exist!")


def deleteBooks():
    global id
    global window

    window = Tk()
    window.title('Library Management System - Delete a Book')
    window.minsize(width=400, height=400)
    window.geometry("450x300")

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Delete a Book", fg='black')
    headingLabel.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.5)

    # ----------id-------------------

    L = Label(window, text="Enter Book id: ")
    L.place(relx=0.05, rely=0.4)

    id = Entry(window, width=5)
    id.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.07)

    submitbtn = Button(window, text="Delete", command=delete_db, bg="#455A64", fg="blue")
    submitbtn.place(relx=0.60, rely=0.8, relwidth=0.30, relheight=0.08)

    print("delete")
