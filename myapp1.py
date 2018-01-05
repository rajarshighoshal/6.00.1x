# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:36:44 2017

@author: RAJARSHI GHOSHAL
"""

import tkinter as tk

window = tk.Tk()
window.title("My APP")
window.geometry("400x400")

# LABEL
title = tk.Label(text="Hello world, welcome to cs50 and welcome to my app")
title.grid(column = 0, row = 0)

# button
button1 = tk.Button(text="Click ME!", bg="red", font=("Times New Roman", 25))
button1.grid(column = 0, row = 1)

# entry field
entryField1 = tk.Entry()
entryField1.grid(column = 0, row = 2)

window.mainloop()