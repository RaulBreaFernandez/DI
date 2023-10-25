from tkinter import ttk
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

        for i, cell in enumerate(self.cells):

            label = ttk.Label(root, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = i, column = 0)
            label.bind("<Button-1>", lambda event, cell = cell: self.onButtonClicked(cell))

        width = int(180)
        height = int(400)

        root.geometry(str(width)+"x"+str(height))

        x = (root.winfo_screenwidth() - width) / 2
        y = (root.winfo_screenheight() - height) / 2
        root.geometry(f"+{int(x)}+{int(y)}")

        barMenu = tk.Menu()
        fileMenu = tk.Menu(barMenu, tearoff = False)

        fileMenu.add_command(label = "Acerca de", command = self.onButtonClicked2)
        barMenu.add_cascade(menu = fileMenu, label = "Ayuda")
        root.config(menu = barMenu)