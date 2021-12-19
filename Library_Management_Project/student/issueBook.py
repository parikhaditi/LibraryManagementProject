import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('library_info.db')
cursor = conn.cursor()
logged_in_id = 0


def issue_db():
    global id
    global Studentid

    global logged_in_id
    print("issue-id", logged_in_id)

    bid = id.get()
    bStudentId = Studentid.get()
    print("student id to issue book", bStudentId)

    try:
        # get list of all available book, if the one user want to issue
        # is available, user can (update) issue to userid.
        cursor.execute('''SELECT Book_id from Books where Status = 'Available' or Status = 'available' ''')
        result = cursor.fetchall()
        if bid == '':
            messagebox.showinfo('Warning', "Input required!")

        for i in result:
            if int(i[0]) == int(bid):
                print("to change value of flag check each i", i[0], bid)
                cursor.execute('''UPDATE Books SET Status = ?, User_id = ? WHERE Book_id = ? ''',
                               ("no", int(bStudentId), int(bid)))
                conn.commit()
                messagebox.showinfo('Success', "Book issued.")
                window.destroy()
                break
            else:
                print("Error", "Required Book is not available!")
    except:
        messagebox.showerror("Error", "Cannot issue given book!")



def issueBooks():
    global id
    global Studentid
    global window

    window = Tk()
    window.title('Library Management System - Issue a Book')
    window.minsize(width=400, height=400)
    window.geometry("450x400")

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Issue a Book", fg='black')
    headingLabel.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.5)

    # ----------id-------------------

    L = Label(window, text="Enter Book ID: ")
    L.place(relx=0.05, rely=0.4)


    id = Entry(window, width=5)
    id.place(relx=0.3, rely=0.4, relwidth=0.62,relheight=0.07)

    # ----------StudentName-------------------

    L = Label(window, text="Enter Student ID: ")
    L.place(relx=0.05, rely=0.5)

    L = Label(window, text="   ")
    L.grid(row=4, column=2)

    Studentid = Entry(window, width=5)
    Studentid.place(relx=0.3, rely=0.5, relwidth=0.62,relheight=0.07)

    submitbtn = Button(window, text="Issue", command=issue_db, bg="#455A64", fg="blue")
    submitbtn.place(relx=0.60, rely=0.7, relwidth=0.30, relheight=0.08)

    print("issue")