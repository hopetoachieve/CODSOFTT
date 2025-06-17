# password_generator.py

import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------- FUNCTIONS ----------
def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    characters = ''
    if use_upper.get(): characters += string.ascii_uppercase
    if use_lower.get(): characters += string.ascii_lowercase
    if use_digits.get(): characters += string.digits
    if use_symbols.get(): characters += string.punctuation

    if not characters:
        messagebox.showwarning("No Options Selected", "Select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------- UI SETUP ----------
root = tk.Tk()
root.title("Fun Password Generator")
root.geometry("400x400")
root.configure(bg="#f7f7f7")
root.resizable(False, False)

# ---------- VARIABLES ----------
length_var = tk.StringVar(value='12')
password_var = tk.StringVar()

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

# ---------- WIDGETS ----------

tk.Label(root, text="Generate a Strong Password", font=("Segoe UI", 16, "bold"), bg="#f7f7f7").pack(pady=10)

frame = tk.Frame(root, bg="#f7f7f7")
frame.pack(pady=10)

tk.Label(frame, text="Password Length:", font=("Segoe UI", 12), bg="#f7f7f7").grid(row=0, column=0, sticky='w')
tk.Entry(frame, textvariable=length_var, font=("Segoe UI", 12), width=5, justify='center').grid(row=0, column=1, padx=10)

tk.Checkbutton(frame, text="Include Uppercase (A-Z)", variable=use_upper, bg="#f7f7f7", font=("Segoe UI", 11)).grid(row=1, column=0, columnspan=2, sticky='w')
tk.Checkbutton(frame, text="Include Lowercase (a-z)", variable=use_lower, bg="#f7f7f7", font=("Segoe UI", 11)).grid(row=2, column=0, columnspan=2, sticky='w')
tk.Checkbutton(frame, text="Include Numbers (0-9)", variable=use_digits, bg="#f7f7f7", font=("Segoe UI", 11)).grid(row=3, column=0, columnspan=2, sticky='w')
tk.Checkbutton(frame, text="Include Symbols (!@#$)", variable=use_symbols, bg="#f7f7f7", font=("Segoe UI", 11)).grid(row=4, column=0, columnspan=2, sticky='w')

tk.Button(root, text="Generate Password", font=("Segoe UI", 12, "bold"), bg="#4CAF50", fg="white",
          command=generate_password).pack(pady=15)

output_entry = tk.Entry(root, textvariable=password_var, font=("Consolas", 14), width=32, justify='center', fg="#333", bd=2, relief="solid")
output_entry.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", font=("Segoe UI", 11), bg="#2196F3", fg="white",
          command=copy_to_clipboard).pack(pady=5)

# ---------- RUN ----------
root.mainloop()
