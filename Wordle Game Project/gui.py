# GUI
import tkinter as tk
from tkinter import ttk

def Playgame():
    #global name
    gamewindow = tk.Tk()
    print('You clicked Play game!')
    gamewindow['bg'] = 'black'

    my_label = ttk.Label(gamewindow, text="Enter your first guess")
    my_label.grid(row=1, column=1)
    content = ''
    guess1 = ttk.Entry(gamewindow)
    guess1.grid(row=2, column=1)
    #guess1['command'] = Playgame # name is a player object
    print(guess1.get())
    my_label = ttk.Label(gamewindow, text=guess1.get())
    my_label.grid(row=4, column=1)

def runGUI(name):
    print('GUI Launched :)')

    # Create the application window
    window = tk.Tk()

    # Create the user interface
    my_label = ttk.Label(window, text="Let's play a game of Wordle!")
    my_label.grid(row=1, column=1)

    go_button = ttk.Button(window, text="Play")
    go_button.grid(row=2, column=1)
    go_button['command'] = Playgame # name is a player object

    quit_button = ttk.Button(window, text="Quit")
    quit_button.grid(row=3, column=1)
    quit_button['command'] = window.destroy

    # Start the GUI event loop
    window.mainloop()