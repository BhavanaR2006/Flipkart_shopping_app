import tkinter as tk
from tkinter import messagebox

def login():
    email = email_entry.get()
    password = password_entry.get()

    if email != "" and password != "":
        messagebox.showinfo("Success", "Login Successful!")

        dashboard = tk.Toplevel(root)
        dashboard.title("Customer Dashboard")
        dashboard.geometry("600x450")
        dashboard.configure(bg="white")

        tk.Label(
            dashboard,
            text="Welcome to Flipkart",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="blue"
        ).pack(pady=20)

        tk.Button(
            dashboard,
            text="Browse Products",
            width=25,
            height=2
        ).pack(pady=10)

        tk.Button(
            dashboard,
            text="My Wishlist",
            width=25,
            height=2
        ).pack(pady=10)

        tk.Button(
            dashboard,
            text="My Orders",
            width=25,
            height=2
        ).pack(pady=10)

        tk.Button(
            dashboard,
            text="Account Details",
            width=25,
            height=2
        ).pack(pady=10)

    else:
        messagebox.showerror("Error", "Please enter Email and Password")

root = tk.Tk()
root.title("Flipkart Customer Login")
root.geometry("450x400")
root.configure(bg="white")

tk.Label(
    root,
    text="Flipkart Customer Login",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="blue"
).pack(pady=20)

tk.Label(root, text="Email / Phone Number", bg="white").pack()

email_entry = tk.Entry(root, width=35)
email_entry.pack(pady=5)

tk.Label(root, text="Password", bg="white").pack()

password_entry = tk.Entry(root, show="*", width=35)
password_entry.pack(pady=5)

tk.Button(
    root,
    text="Login",
    command=login,
    bg="blue",
    fg="white",
    width=18
).pack(pady=20)

root.mainloop()