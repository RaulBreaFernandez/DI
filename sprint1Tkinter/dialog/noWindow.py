from tkinter import Tk, ttk

def showNo():
    root = Tk()
    root.title("NoWindow")
    label = ttk.Label(root, text = "Has respondido NO")
    label.pack()
    root.mainloop()