#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import mysql.connector

# create connection to database
mydb = mysql.connector.connect(
 host="localhost",
 user="yourusername",
 password="yourpassword",
 database="yourdatabase"
)

def check_credentials(username, password):
    cursor = mydb.cursor()
    query = "SELECT * FROM your_table WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return result is not None

def login_function():
    global username_entry, password_entry
    username = username_entry.get()
    password = password_entry.get()

    if check_credentials(username, password):
        messagebox.showinfo("Success", "Login successful!")
        window.destroy()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# create window
window = Tk()
window.title("Login")

# create widgets
username_label = Label(window, text="Username:")
username_entry = Entry(window)
password_label = Label(window, text="Password:")
password_entry = Entry(window, show="*")
login_button = Button(window, text="Login", command=login_function)

# position widgets
username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, column=1)

# start program
window.mainloop()
