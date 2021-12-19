from bookHome import *
from db import *
import issueBook
import returnBook
from tkinter import messagebox

connection = sqlite3.connect('library_info.db')
cursor = conn.cursor()

root = Tk()
root.title("Library Management System - Login")
root.minsize(width=400, height=400)
root.geometry("600x500")


def currentLogin():
    name = entry1.get()
    password = entry2.get()

    cur.execute('''SELECT User_id FROM Users WHERE Users.Username = ? AND Users.Password = ?''', (name, password))
    result = cur.fetchall()
    for row in result:
        print(f'from login : id {row[0]:<3}')

    return result


def validate():
    print("in validate function 2")
    name = entry1.get()
    password = entry2.get()

    cur.execute('''SELECT * FROM Users WHERE Users.Username = ? AND Users.Password = ?''', (name, password))
    results = cur.fetchall()

    if len(results) == 1:
        print("validation matches and perform book operations")
        cur.execute('''SELECT User_id FROM Users WHERE Users.Username = ? AND Users.Password = ?''',
                    (name, password))
        result = cur.fetchall()

        global logged_in_id
        issueBook.logged_in_id = result
        returnBook.logged_in_id = result

        manageBookOperations()
    else:
        messagebox.showerror("Error", "Invalid Credentials,Please try again!")

def UserLogin():

    headingFrame1 = Frame(root, bg="green", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Welcome to Library Management", fg='black')
    headingLabel.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.5)

    global entry1, entry2, submit_button

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.3)

    # Name
    label1 = Label(labelFrame, text="User Name : ", bg='white', fg='black')
    label1.place(relx=0.05, rely=0.3)

    entry1 = Entry(labelFrame)
    entry1.place(relx=0.3, rely=0.3, relwidth=0.62)

    # Password
    lable2 = Label(labelFrame, text="Password : ", bg='white', fg='black')
    lable2.place(relx=0.05, rely=0.5)

    entry2 = Entry(labelFrame)
    entry2.config(show="*")
    entry2.place(relx=0.3, rely=0.5, relwidth=0.62)

    quitbtn2 = Button(root, text="Quit", bg='#455A64', fg='blue', command=root.quit)
    quitbtn2.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    enter_button2 = Button(root, text="Login", bg='#455A64', fg='blue', command=lambda: validate())
    enter_button2.place(relx=0.75, rely=0.9, relwidth=0.18, relheight=0.08)


UserLogin()
root.mainloop()
