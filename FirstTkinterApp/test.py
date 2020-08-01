import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello")


root = tk.Tk()
root.title('Greeter')

greet_button = ttk.Button(root, text="Hello", command=greet)

root.mainloop()

greet()
