import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def get_password_length():
    try:
        length = int(entry.get())
        return length
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return None

def generate_and_display_password():
    length = get_password_length()
    if length is not None:
        password = generate_password(length)
        if password is not None:
            result_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200") 

tk.Label(root, text="Enter password length:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()