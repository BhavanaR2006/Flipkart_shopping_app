from tkinter import *
import os

root = Tk()

root.title("Flipkart Shopping App")
root.geometry("500x500")
root.configure(bg="white")

Label(
    root,
    text="Flipkart Shopping App",
    font=("Arial",20,"bold"),
    bg="white",
    fg="blue"
).pack(pady=20)

def open_admin():
    os.system("python admin_records.py")

def open_manage():
    os.system("python manage_products.py")

def open_seller():
    os.system("python seller_login.py")

def open_browse():
    os.system("python browse_product.py")

def open_customer():
    os.system("python customer_login.py")

def open_orders():
    os.system("python orders_tracking.py")

Button(root,text="Admin Records",width=30,command=open_admin).pack(pady=5)

Button(root,text="Manage Products",width=30,command=open_manage).pack(pady=5)

Button(root,text="Seller Login",width=30,command=open_seller).pack(pady=5)

Button(root,text="Browse Product",width=30,command=open_browse).pack(pady=5)

Button(root,text="Customer Login",width=30,command=open_customer).pack(pady=5)

Button(root,text="Orders Tracking",width=30,command=open_orders).pack(pady=5)

Button(root,text="Exit",width=30,bg="red",fg="white",command=root.destroy).pack(pady=20)

root.mainloop()