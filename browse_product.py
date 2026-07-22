import tkinter as tk
from tkinter import messagebox

def search_product():
    product = search_entry.get()

    if product != "":
        messagebox.showinfo(
            "Search Result",
            f"{product} is available in Flipkart."
        )
    else:
        messagebox.showwarning(
            "Warning",
            "Please enter a product name."
        )

root = tk.Tk()
root.title("Browse Products")
root.geometry("600x500")
root.configure(bg="white")

heading = tk.Label(
    root,
    text="Flipkart Product Search",
    font=("Arial",18,"bold"),
    bg="white",
    fg="blue"
)
heading.pack(pady=20)

tk.Label(root, text="Search Product", bg="white").pack()

search_entry = tk.Entry(root, width=35)
search_entry.pack(pady=5)

tk.Button(
    root,
    text="Search",
    command=search_product,
    bg="blue",
    fg="white",
    width=15
).pack(pady=15)

tk.Label(
    root,
    text="Available Products",
    font=("Arial",14,"bold"),
    bg="white"
).pack(pady=10)

products = [
    "Laptop",
    "Mobile",
    "Headphones",
    "Shoes",
    "Watch",
    "T-Shirt",
    "Keyboard",
    "Mouse"
]

listbox = tk.Listbox(root, width=40, height=10)

for item in products:
    listbox.insert(tk.END, item)

listbox.pack(pady=10)

root.mainloop()