# GUI
import tkinter as tk
from tkinter import ttk
from tkinter import *

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    print(inp)

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
    my_label = ttk.Label(gamewindow, text=guess1.get())
    my_label.grid(row=4, column=1)
    content = tk.StringVar()

    go_button = tk.Button(gamewindow, text="Check")
    go_button.grid(row=5, column=1)
    go_button.after(33, evaluate_guess,guess1)

    printButton = tk.Button(gamewindow,
                        text = "Print", 
                        command = print(guess1.get))
    printButton.grid(row=7, column=1)

def evaluate_guess(guess1):

    print('you guessed ', guess1.get() ,'!')

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

#root = Tk()
#root.geometry("300x300")
#root.title(" Q&A ")
 
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if(INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")
     
    l = Label(text = "What is 24 * 5 ? ")
    inputtxt = Text(root, height = 10,
                    width = 25,
                    bg = "light yellow")
    
    Output = Text(root, height = 5,
                width = 25,
                bg = "light cyan")
    
    Display = Button(root, height = 2,
                    width = 20,
                    text ="Show",
                    command = lambda:Take_input())
    
    l.pack()
    inputtxt.pack()
    Display.pack()
    Output.pack()