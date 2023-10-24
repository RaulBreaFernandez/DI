from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class DetailWindow():

    def onButtonClicked(self, cell):

        message = "Has hecho click en la celda: "+cell.title
        messagebox.showinfo("Información", message)

        def __init__(self, cell):

            root = tk.Toplevel()
            root.title("DetailWindow")
            label1 = ttk.Label(root, text=cell.title)
            label2 = ttk.Label(root, image=cell.image_tk)
            label3 = ttk.Label(root, text=cell.description, wraplength= 160)
            label1.pack(side="top")
            label2.pack()
            label3.pack()
            width=int(160)
            height=int(300)

