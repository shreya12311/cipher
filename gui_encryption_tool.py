# =========================================================
# WORKING GUI ENCRYPTION & DECRYPTION TOOL
# DecodeLabs Internship Project 2
# Python + Tkinter
# =========================================================

import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------
# Caesar Cipher Functions
# ---------------------------------------------------------

def caesar_encrypt(text, shift):

    result = ""

    for char in text:

        if char.isalpha():

            shift_base = 65 if char.isupper() else 97

            result += chr(
                (ord(char) - shift_base + shift) % 26 + shift_base
            )

        else:
            result += char

    return result


def caesar_decrypt(text, shift):

    result = ""

    for char in text:

        if char.isalpha():

            shift_base = 65 if char.isupper() else 97

            result += chr(
                (ord(char) - shift_base - shift) % 26 + shift_base
            )

        else:
            result += char

    return result


# ---------------------------------------------------------
# Encrypt Button
# ---------------------------------------------------------

def encrypt_message():

    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showerror("Error", "Please enter a message")
        return

    try:
        shift = int(shift_entry.get())

    except:
        messagebox.showerror("Error", "Shift key must be a number")
        return

    encrypted = caesar_encrypt(text, shift)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted)


# ---------------------------------------------------------
# Decrypt Button
# ---------------------------------------------------------

def decrypt_message():

    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showerror("Error", "Please enter encrypted text")
        return

    try:
        shift = int(shift_entry.get())

    except:
        messagebox.showerror("Error", "Shift key must be a number")
        return

    decrypted = caesar_decrypt(text, shift)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted)


# ---------------------------------------------------------
# Clear Function
# ---------------------------------------------------------

def clear_all():

    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)


# ---------------------------------------------------------
# Main Window
# ---------------------------------------------------------

root = tk.Tk()

root.title("Encryption & Decryption Tool")
root.geometry("700x500")
root.configure(bg="#121212")

# ---------------------------------------------------------
# Heading
# ---------------------------------------------------------

title = tk.Label(
    root,
    text="ADVANCED ENCRYPTION TOOL",
    font=("Arial", 20, "bold"),
    fg="cyan",
    bg="#121212"
)

title.pack(pady=15)

# ---------------------------------------------------------
# Input Section
# ---------------------------------------------------------

input_label = tk.Label(
    root,
    text="Enter Message",
    font=("Arial", 12),
    fg="white",
    bg="#121212"
)

input_label.pack()

input_text = tk.Text(
    root,
    height=7,
    width=70,
    font=("Arial", 11),
    bg="#1f1f1f",
    fg="white",
    insertbackground="white"
)

input_text.pack(pady=10)

# ---------------------------------------------------------
# Shift Key
# ---------------------------------------------------------

shift_label = tk.Label(
    root,
    text="Enter Shift Key",
    font=("Arial", 12),
    fg="white",
    bg="#121212"
)

shift_label.pack()

shift_entry = tk.Entry(
    root,
    width=10,
    font=("Arial", 12),
    justify="center"
)

shift_entry.pack(pady=10)

# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------

button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=10)

encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    width=12,
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=encrypt_message
)

encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    width=12,
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=decrypt_message
)

decrypt_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=clear_all
)

clear_btn.grid(row=0, column=2, padx=10)

# ---------------------------------------------------------
# Output Section
# ---------------------------------------------------------

output_label = tk.Label(
    root,
    text="Output",
    font=("Arial", 12),
    fg="white",
    bg="#121212"
)

output_label.pack()

output_text = tk.Text(
    root,
    height=7,
    width=70,
    font=("Arial", 11),
    bg="#1f1f1f",
    fg="cyan",
    insertbackground="white"
)

output_text.pack(pady=10)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

footer = tk.Label(
    root,
    text="DecodeLabs Internship Project 2",
    font=("Arial", 10),
    fg="gray",
    bg="#121212"
)

footer.pack(pady=10)

# ---------------------------------------------------------
# Run Window
# ---------------------------------------------------------

root.mainloop()