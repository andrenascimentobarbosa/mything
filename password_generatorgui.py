#!/usr/bin/python3

import tkinter as tk
from random import shuffle
import string

def generate_password(length=12):
    letters = string.ascii_letters  # Includes lowercase and uppercase letters
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets into one list
    characters = list(letters + digits + punctuation)

    # Shuffle the characters to randomize their order
    shuffle(characters)

    # Generate a random password by picking characters randomly from the shuffled list
    password = ''.join(characters[:length])
    
    return password

def generate_password_gui():
    length = int(length_entry.get())
    password = generate_password(length)
    result_label.config(text=password)

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")

# Create and place widgets in the window
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password_gui)
generate_button.pack()

result_label = tk.Label(window, text="Generated Password will appear here")
result_label.pack()

# Start the GUI event loop
window.mainloop()

