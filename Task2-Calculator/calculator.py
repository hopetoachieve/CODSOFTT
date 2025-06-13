# calculator_gui.py

import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")
root.resizable(False, False)

# Configure rows and columns to make the layout responsive
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Entry widget to display expressions/results
entry = tk.Entry(root, font=("Arial", 24), borderwidth=0, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Button press handler
def press(key):
    entry.insert(tk.END, key)

# Clear button
def clear():
    entry.delete(0, tk.END)

# Evaluation
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        clear()
    except:
        messagebox.showerror("Error", "Invalid input.")
        clear()

# Buttons list
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons using loop
for i, row in enumerate(buttons):
    for j, val in enumerate(row):
        if val == '=':
            btn = tk.Button(root, text=val, font=("Arial", 18), bg="#4CAF50", fg="white",
                            command=calculate)
        else:
            btn = tk.Button(root, text=val, font=("Arial", 18), bg="#f0f0f0", fg="black",
                            command=lambda v=val: press(v))
        btn.grid(row=i+1, column=j, sticky="nsew", padx=5, pady=5)

# Clear button at the bottom
clear_btn = tk.Button(root, text="Clear", font=("Arial", 16), bg="#f44336", fg="white", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Keyboard bindings
def key_handler(event):
    key = event.char

    if key in '0123456789.+-*/':
        press(key)
    elif event.keysym == 'Return':  # Enter key
        calculate()
    elif event.keysym == 'BackSpace':
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])
    elif event.keysym == 'Escape':
        clear()

# Bind keys to the window
root.bind('<Key>', key_handler)

# Run app
root.mainloop()
