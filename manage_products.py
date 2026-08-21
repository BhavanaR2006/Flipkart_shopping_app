import tkinter as tk
from tkinter import messagebox

def save_product():
    messagebox.showinfo("Success", "Product Saved Successfully!")

root = tk.Tk()
root.title("Manage Products")
root.geometry("500x500")
root.configure(bg="white")

title = tk.Label(
    root,
    text="Manage Product Listings",
    font=("Arial",18,"bold"),
    bg="white",
    fg="blue"
)
title.pack(pady=20)

tk.Label(root,text="Product Name",bg="white").pack()
product = tk.Entry(root,width=35)
product.pack()

tk.Label(root,text="Category",bg="white").pack()
category = tk.Entry(root,width=35)
category.pack()

tk.Label(root,text="Price",bg="white").pack()
price = tk.Entry(root,width=35)
price.pack()

tk.Label(root,text="Stock Quantity",bg="white").pack()
stock = tk.Entry(root,width=35)
stock.pack()

save_btn = tk.Button(
    root,
    text="Save Product",
    command=save_product,
    bg="green",
    fg="white",
    width=20
)

save_btn.pack(pady=25)

root.mainloop()