import string
import random
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def get_length():
    global symbols, letters, nums
    letters = int(entry_letters.get())
    nums = int(entry_nums.get())
    symbols = int(entry_symbols.get())

    if letters + nums + symbols == 0:
        messagebox.showerror("Error", "Please enter higher numeric value than (0) for atleast one of these: Letters, Numbers, and Symbols.")
    elif letters + nums + symbols > 64:
        messagebox.showerror("Error", "Please enter a maximum of 64 characters in total.")

def generate_password():

    try:
        get_length() 
        pwd = ''
        for c in range(symbols):
            pwd += random.choice(string.punctuation)
        for c in range(letters):
            pwd += random.choice(string.ascii_letters)
        for c in range(nums):
            pwd += random.choice(string.digits)

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, pwd)
        password_entry.config(bg="#add8e6")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for Letters, Numbers, and Symbols.")

def copy_to_clipboard():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update() 
        messagebox.showinfo("Copy Successful", "Password copied to clipboard!")

    else:
        messagebox.showwarning("No Password", "Generate a password before copying!")

root = tk.Tk()
root.title("Password Generator")


label_letters = Label(root, text="Letters:", font=("Helvetica", 12, "bold"))
label_letters.grid(padx=10, pady=5, row=0, column=0)
entry_letters = Entry(root, width=5, bg="#add8e6")
entry_letters.grid(padx=10, pady=5, row=0, column=1)

label_nums = Label(root, text="Numbers:", font=("Helvetica", 12, "bold"))
label_nums.grid(padx=10, pady=5, row=1, column=0)
entry_nums = Entry(root, width=5, bg="#add8e6")
entry_nums.grid(padx=10, pady=5, row=1, column=1)

label_symbols = Label(root, text="Symbols:", font=("Helvetica", 12, "bold"))
label_symbols.grid(padx=10, pady=5, row=2, column=0)
entry_symbols = Entry(root, width=5, bg="#add8e6")
entry_symbols.grid(padx=10, pady=5, row=2, column=1)

generate_button = Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12, "bold"))
generate_button.grid(pady=10, row=3, column=0, columnspan=2)

password_entry = Entry(root, width=50, bg="#add8e6", font=("Helvetica", 12, "bold"), justify="center")
password_entry.grid(pady=10, row=4, column=0, columnspan=2, ipadx=20)

copy_button = Button(root, text="Copy Password", command=copy_to_clipboard, font=("Helvetica", 12, "bold"))
copy_button.grid(pady=10, row=5, column=0, columnspan=2)


root.mainloop()