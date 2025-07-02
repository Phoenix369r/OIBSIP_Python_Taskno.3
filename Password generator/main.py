import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip
from tkinter import PhotoImage
from PIL import Image, ImageTk

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character set!"

    # Guarantee at least one of each selected type
    password = []
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    while len(password) < length:
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def on_generate():
    try:
        length = int(length_var.get())
        if not (8 <= length <= 64):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Length must be a number between 8 and 64.")
        return

    password = generate_password(
        length,
        upper_var.get(),
        lower_var.get(),
        digits_var.get(),
        symbols_var.get()
    )
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Main GUI Window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("600x500")
root.resizable(False, False)

# Load and display the image
# Load and resize the image using Pillow
try:
    original = Image.open("logo.png")
    resized = original.resize((150, 150))  # Set width, height as desired
    logo = ImageTk.PhotoImage(resized)
    tk.Label(root, image=logo).pack(pady=10)
except Exception as e:
    print("Image failed to load:", e)


# Variables
length_var = tk.StringVar(value="12")
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# Layout
tk.Label(root, text="Password Length (8–64):").pack(pady=5)
tk.Entry(root, textvariable=length_var, width=10, justify='center').pack()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', padx=40)

tk.Button(root, text="Generate Password", command=on_generate, bg="#4CAF50", fg="white").pack(pady=10)

password_entry = tk.Entry(root, font=("Courier", 12), justify='center', width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()
