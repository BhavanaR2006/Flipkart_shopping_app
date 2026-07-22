import tkinter as tk
from tkinter import messagebox

def track_order():
    order = order_entry.get()

    if order != "":
        messagebox.showinfo(
            "Order Status",
            f"Order ID {order}\n\nStatus : Out for Delivery"
        )
    else:
        messagebox.showwarning(
            "Warning",
            "Please enter Order ID."
        )

root = tk.Tk()
root.title("Order Tracking")
root.geometry("500x400")
root.configure(bg="white")

tk.Label(
    root,
    text="Track Your Order",
    font=("Arial",18,"bold"),
    bg="white",
    fg="blue"
).pack(pady=20)

tk.Label(root, text="Order ID", bg="white").pack()

order_entry = tk.Entry(root, width=30)
order_entry.pack(pady=10)

tk.Button(
    root,
    text="Track Order",
    command=track_order,
    bg="blue",
    fg="white",
    width=20
).pack(pady=20)

root.mainloop()