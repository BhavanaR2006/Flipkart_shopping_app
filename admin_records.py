import tkinter as tk
from tkinter import messagebox

def view_records():
    messagebox.showinfo("Records", "Customer and Seller Records Loaded Successfully!")

root = tk.Tk()
root.title("Admin Panel")
root.geometry("600x500")
root.configure(bg="black")

tk.Label(
    root,
    text="Admin Dashboard",
    font=("Arial",18,"bold"),
    bg="white",
    fg="blue"
).pack(pady=20)

listbox = tk.Listbox(root, width=60, height=12)

records = [
    "Customer : Rahul",
    "Customer : Priya",
    "Customer : Karthik",
    "Seller : ABC Mobiles",
    "Seller : Fashion World",
    "Seller : Home Appliances"
]

for item in records:
    listbox.insert(tk.END, item)

listbox.pack(pady=10)

tk.Button(
    root,
    text="View Records",
    command=view_records,
    bg="green",
    fg="white",
    width=20
).pack(pady=20)


root.mainloop()