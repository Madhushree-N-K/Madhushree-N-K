import re
import tkinter as tk
from tkinter import messagebox

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def check_email():
    email = email_entry.get()  
    if is_valid_email(email):
        messagebox.showinfo("Result", f"{email} is a Ham Email.")
    else:
        messagebox.showwarning("Result", f"{email} is a Spam Email.")

root = tk.Tk()
root.title("Email Validator")
root.geometry("400x200")

email_label = tk.Label(root, text="Enter Email Address:")
email_label.pack(pady=10)

email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Email", command=check_email)
check_button.pack(pady=10)

root.mainloop()
