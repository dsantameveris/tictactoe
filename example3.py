import tkinter

class exa3:
    def __init__ (self, windowroot):
        self.lbl = tkinter.Label(windowroot, text = "Press button to quit")
        self.lbl.pack()
        self.btn = tkinter.Button(windowroot, text = "Quit", command = self.quit)
        self.btn.pack()

    def quit(self):
        import sys; sys.exit()
    
root = tkinter.Tk()

ex3 = exa3(root)
root.mainloop()
