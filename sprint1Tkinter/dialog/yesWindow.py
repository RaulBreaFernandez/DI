from tkinter import Tk, ttk

def showYes():
    root = Tk()
    root.title("YesWindow")
    label = ttk.Label(root, text = "Has respondido SÍ")
    label.pack()
    root.mainloop()