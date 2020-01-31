import tkinter as tk
import sys

#This is the root
root = tk.Tk()

def quit():
    sys.exit()

label = tk.Label(root, text = "Press to quit")
label.pack()

button = tk.Button(root, text = "Quit", command = quit)
button.pack()

root.mainloop()