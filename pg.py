import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")
    
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    
    all_characters = letters + digits + special_characters
    password = [
        random.choice(letters), 
        random.choice(digits), 
        random.choice(special_characters)
    ]
    
    password += [random.choice(all_characters) for _ in range(length - 3)]
    random.shuffle(password)
    
    return ''.join(password)

def on_generate_button_click():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Password length must be at least 1")
        password = generate_password(length)
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

# Set up the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Enter the desired password length:").pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password",bg="light green",fg="black", command=on_generate_button_click)
generate_button.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Courier", 14), fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()