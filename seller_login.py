import tkinter as tk
from tkinter import messagebox

# Function to open Seller Dashboard
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username != "" and password != "":
        messagebox.showinfo("Login", "Login Successful!")

        dashboard = tk.Toplevel(root)
        dashboard.title("Seller Dashboard")
        dashboard.geometry("500x400")
        dashboard.configure(bg="white")

        title = tk.Label(
            dashboard,
            text="Seller Dashboard",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="blue"
        )
        title.pack(pady=20)

        tk.Button(
            dashboard,
            text="Manage Products",
            width=25,
            height=2
        ).pack(pady=10)

        tk.Button(
            dashboard,
            text="Incoming Orders",
            width=25,
            height=2
        ).pack(pady=10)

        tk.Button(
            dashboard,
            text="Update Order Status",
            width=25,
            height=2
        ).pack(pady=10)

    else:
        messagebox.showerror(
            "Error",
            "Please enter Username and Password"
        )

# Main Window
root = tk.Tk()
root.title("Flipkart Seller Login")
root.geometry("450x350")
root.configure(bg="white")

heading = tk.Label(
    root,
    text="Flipkart Seller Login",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="blue"
)
heading.pack(pady=20)

tk.Label(root, text="Username", bg="white").pack()

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(root, text="Password", bg="white").pack()

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

login_btn = tk.Button(
    root,
    text="Login",
    command=login,
    bg="blue",
    fg="white",
    width=15
)
login_btn.pack(pady=20)

root.mainloop()

