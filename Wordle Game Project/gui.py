import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

# Create the application window
window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text="Let's play a game of Wordle")
my_label.grid(row=100, column=100)

# Start the GUI event loop
window.mainloop()

application_window = tk.Tk()

answer = simpledialog.askstring("Input", "What is your first name?",
                                parent=application_window)
if answer is not None or answer == '':
    print("Your name is", answer)
else:
    print("You don't have a name? ok...")