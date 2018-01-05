# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:12:41 2017

@author: RAJARSHI GHOSHAL
"""

import random
import tkinter as tk

window = tk.Tk()
window.title("Greetings _________")
window.geometry("400x400")

#---FUNCTIONS---#
def phraseGenerator():
    phrases = ["Hello ", "What's up ", "Aloha ", "Hafa Adoi "]
    
    name = str(entry1.get())
    
    return phrases[random.randint(0 , 3)] + name

def phraseDisplay():
    greeting = phraseGenerator()
    
    # This creats the text field
    greetingDisplay = tk.Text(master=window, height=10, width=30)
    greetingDisplay.grid(column=0, row=3)
    
    greetingDisplay.insert(tk.END, greeting)

#---LABEL---#
label1 = tk.Label(text="Welcome to my app")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What is your name?!")
label2.grid(column=0, row=1)

#---ENTRY FIELD---#
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

#---BUTTON---#
button1 = tk.Button(text="Click Me", command = phraseDisplay)
button1.grid(column=0, row=2)

window.mainloop()