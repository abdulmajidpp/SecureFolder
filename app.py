import tkinter as tk
from tkinter import messagebox
import subprocess
import sqlite3
import time
import os

# Function to initialize the SQLite database
def init_db():
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()  # Commit any changes

def open_folder():
    folder_path = "C:\\Users\\Administrator\\Desktop\\secure folder"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    
    subprocess.run(f'attrib +h "{folder_path}"', shell=True)
    print(f"Folder '{folder_path}' set as hidden.")
    subprocess.Popen(['explorer', folder_path])

# Function for handling login
def on_button_click():
    username = user_name_entry.get()
    password = pass_name_entry.get()
    
    if username and password:
        with sqlite3.connect('users.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
            user = c.fetchone()
        
        if user:
            open_folder()
            # Log user access (Optional)
            with open('C:\\Users\\Administrator\\Desktop\\login.txt', 'a') as logins:
                logins.write(f"\n{username} accessed the system at {time.asctime()}")
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    else:
        messagebox.showwarning("Input Error", "Please enter both username and password")

# Function for handling new user registration
def new_user():
    username = new_user_name_entry.get()
    password = new_user_pass_entry.get()
    re_enter_password = new_user_reenter_pass_entry.get()
    
    if username and password and re_enter_password:
        if password == re_enter_password:
            try:
                with sqlite3.connect('users.db') as conn:
                    c = conn.cursor()
                    # Insert the new user into the database
                    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                    conn.commit()
                messagebox.showinfo("Success", f"New user {username} created successfully!")
                show_login_page()  # Go back to login page after registration
            except sqlite3.IntegrityError:
                messagebox.showerror("Registration Failed", "Username already exists")
        else:
            messagebox.showwarning("Password Mismatch", "Passwords do not match")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields")

# Function to close the application
def quit_application():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Login")
init_db()

# Initial Login Page
def show_login_page():
    # Clear any existing widgets
    for widget in root.winfo_children():
        widget.destroy()
    
    # Username and Password fields for login
    global user_name_entry, pass_name_entry
    user_name_label = tk.Label(root, text="User name ")
    user_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    user_name_entry = tk.Entry(root, width=30)
    user_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    pass_name_label = tk.Label(root, text="Password ")
    pass_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    pass_name_entry = tk.Entry(root, width=30, show="*")
    pass_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    login_button = tk.Button(root, text="Login", command=on_button_click)
    login_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    
    quit_button = tk.Button(root, text="Quit", command=quit_application)
    quit_button.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    new_user_button = tk.Button(root, text="New User", command=show_new_user_page)
    new_user_button.grid(row=2, column=3, padx=10, pady=10, sticky="w")

# New User Page
def show_new_user_page():
    # Clear any existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Username and Password fields for new user registration
    global new_user_name_entry, new_user_pass_entry, new_user_reenter_pass_entry
    new_user_name_label = tk.Label(root, text="User name ")
    new_user_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    new_user_name_entry = tk.Entry(root, width=30)
    new_user_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    new_user_pass_label = tk.Label(root, text="Password ")
    new_user_pass_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    new_user_pass_entry = tk.Entry(root, width=30, show="*")
    new_user_pass_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    new_user_reenter_pass_label = tk.Label(root, text="Re-enter Password ")
    new_user_reenter_pass_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    new_user_reenter_pass_entry = tk.Entry(root, width=30, show="*")
    new_user_reenter_pass_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    new_user_button = tk.Button(root, text="Register", command=new_user)
    new_user_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    
    quit_button = tk.Button(root, text="Quit", command=quit_application)
    quit_button.grid(row=3, column=2, padx=10, pady=10, sticky="w")

    back_button = tk.Button(root, text="Back to Login", command=show_login_page)
    back_button.grid(row=3, column=3, padx=10, pady=10, sticky="w")

# Start with the login page
show_login_page()

# Run the Tkinter event loop
root.mainloop()
