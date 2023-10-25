from tkinter import Canvas, Frame, Label, Scrollbar, ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detailWindow import DetailWindow

class MainWindow():

    def onButtonClicked(self, cell):

        DetailWindow(cell)

    def onButtonClicked2(self):

        message = "Al desarrollador le ha costado mucho hacer este sprint, sé bueno por favor"
        messagebox.showinfo("Acerca del desarrollador", message)

    def __init__(self, root, jsonData):
        
        #Título de la ventana
        root.title("5 libros de Brandon Sanderson")
            
        self.cells = []

        for i in jsonData:

            name = i.get("name")
            description = i.get("description")
            url = i.get("image_url")
            self.cells.append(Cell(name, description, url))

        width = int(180)
        height = int(400)

        root.geometry(str(width)+"x"+str(height))

        x = (root.winfo_screenwidth() - width) / 2
        y = (root.winfo_screenheight() - height) / 2
        root.geometry(f"+{int(x)}+{int(y)}")

        self.canvas = Canvas(root)
        self.scrollbar = Scrollbar(root, orient = "vertical", command = self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window = self.scrollable_frame, anchor = "nw")
        self.canvas.configure(yscrollcommand = self.scrollbar.set)

        for i, cell in enumerate(self.cells):

            self.addItem(cell)

        self.canvas.grid(row = 0, column = 0, sticky = "nsew")
        self.scrollbar.grid(row = 0, column = 1, sticky = "ns")
        
    def addItem(self, cell):

        frame = Frame(self.scrollable_frame)
        frame.pack(pady = 10)
        
        label = Label(frame, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
        label.grid(row = 0, column = 0)
        label.bind("<Button-1>", lambda event, clickedCell = cell: self.onButtonClicked(clickedCell))