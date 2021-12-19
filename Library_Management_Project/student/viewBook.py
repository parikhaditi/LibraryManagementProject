from tkinter import *
from tkinter import messagebox
from db import *


def close():
    window.destroy()


def viewBooks():
    global window

    window = Tk()
    window.title('Library Management System - List of Books')
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    headingFrame1 = Frame(window, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="List of Books", fg='black')
    headingLabel.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.5)

    tableFrame1 = Frame(window, bg="white", bd=5)
    tableFrame1.place(relx=0.1, rely=0.3)

    submitbtn = Button(window, text="Close", bg="#455A64", fg="blue", command=close)
    submitbtn.place(relx=0.60, rely=0.7, relwidth=0.30, relheight=0.08)

    try:
        conn = None
        conn = sqlite3.connect('library_info.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Books')
        results = cur.fetchall()
        total_rows = len(results)
        total_columns = len(results[0])

        lst = [('ID', 'Title', 'Author', 'Status', 'Assigned To')]
        for k in range(0, 5):
            e = Entry(tableFrame1, width=10, fg='black')
            e.grid(row=0, column=k)
            e.insert(END, lst[0][k])

        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(tableFrame1, width=10, fg='black')

                e.grid(row=i + 1, column=j)
                e.insert(END, results[i][j])

    except:
        messagebox.showerror("Error", "Cannot Fetch data.")

    finally:
        if conn != None:
            conn.close()

    print("view")
