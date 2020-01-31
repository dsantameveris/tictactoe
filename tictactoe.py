import tkinter as tk

root = tk.Tk()

for r in range(3):
    for c in range(4):
        tk.Button(root).grid(row = r, column = c)
root.mainloop()
