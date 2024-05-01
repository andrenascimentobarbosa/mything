#!/usr/bin/python3

import tkinter as tk
from random import shuffle
import string


def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    
    characters = list(letters + digits + punctuation)

    
    shuffle(characters)

    password = ''.join(characters[:length])
    
    return password


def generate_password_gui():
    length = int(length_entry.get())
    password = generate_password(length)
    result_label.config(text=password)


window = tk.Tk()
window.title('p4$sw0rd-g3nr4t0r')

length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password_gui)
generate_button.pack()

result_label = tk.Label(window, text="************")
result_label.pack()


window.mainloop()

