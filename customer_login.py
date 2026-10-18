import tkinter as tk
from tkinter import messagebox

products = [
    ("Laptop", 55000),
    ("Smartphone", 25000),
    ("Headphones", 2000),
    ("Smart Watch", 3500),
    ("Keyboard", 1200)
]

cart = []


def browse_products():
    product_window = tk.Toplevel(root)
    product_window.title("Flipkart - Products")
    product_window.geometry("600x500")
    product_window.configure(bg="white")

    tk.Label(
        product_window,
        text="Available Products",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="blue"
    ).pack(pady=20)

    for name, price in products:
        frame = tk.Frame(product_window, bg="white")
        frame.pack(fill="x", padx=30, pady=8)

        tk.Label(
            frame,
            text=f"{name} - ₹{price}",
            font=("Arial", 13),
            bg="white"
        ).pack(side="left")

        tk.Button(
            frame,
            text="Add to Cart",
            command=lambda n=name, p=price: add_to_cart(n, p)
        ).pack(side="right")


def add_to_cart(name, price):
    cart.append((name, price))
    messagebox.showinfo(
        "Cart",
        f"{name} added to cart successfully!"
    )


def view_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("Shopping Cart")
    cart_window.geometry("500x450")

    tk.Label(
        cart_window,
        text="My Cart",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    if not cart:
        tk.Label(
            cart_window,
            text="Your cart is empty",
            font=("Arial", 14)
        ).pack(pady=20)
        return

    total = 0

    for name, price in cart:
        tk.Label(
            cart_window,
            text=f"{name} - ₹{price}",
            font=("Arial", 13)
        ).pack(pady=5)

        total += price

    tk.Label(
        cart_window,
        text=f"Total: ₹{total}",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    tk.Button(
        cart_window,
        text="Checkout",
        font=("Arial", 13),
        command=lambda: checkout(cart_window)
    ).pack(pady=10)


def checkout(window):
    if not cart:
        messagebox.showwarning("Checkout", "Cart is empty!")
        return

    messagebox.showinfo(
        "Order Confirmed",
        "Your order has been placed successfully!"
    )

    cart.clear()
    window.destroy()


def login():
    email = email_entry.get()
    password = password_entry.get()

    if email != "" and password != "":
        messagebox.showinfo("Success", "Login Successful!")

        dashboard = tk.Toplevel(root)
        dashboard.title("Flipkart Dashboard")
        dashboard.geometry("600x500")
        dashboard.configure(bg="white")

        tk.Label(
            dashboard,
            text="Welcome to Flipkart",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="blue"
        ).pack(pady=30)

        tk.Button(
            dashboard,
            text="Browse Products",
            font=("Arial", 14),
            width=20,
            command=browse_products
        ).pack(pady=10)

        tk.Button(
            dashboard,
            text="View Cart",
            font=("Arial", 14),
            width=20,
            command=view_cart
        ).pack(pady=10)

    else:
        messagebox.showwarning(
            "Login",
            "Please enter Email and Password"
        )


# Main Login Window
root = tk.Tk()
root.title("Flipkart Customer Login")
root.geometry("500x400")
root.configure(bg="white")

tk.Label(
    root,
    text="Flipkart Login",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="blue"
).pack(pady=30)

tk.Label(
    root,
    text="Email",
    font=("Arial", 13),
    bg="white"
).pack()

email_entry = tk.Entry(root, width=35)
email_entry.pack(pady=8)

tk.Label(
    root,
    text="Password",
    font=("Arial", 13),
    bg="white"
).pack()

password_entry = tk.Entry(root, width=35, show="*")
password_entry.pack(pady=8)

tk.Button(
    root,
    text="Login",
    font=("Arial", 14, "bold"),
    width=15,
    command=login
).pack(pady=20)

root.mainloop()