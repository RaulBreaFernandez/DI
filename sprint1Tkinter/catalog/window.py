from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk

class MainWindow():

    def onButtonClicked(self):

        #Mensaje que aparece cuando haces click en un libro.
        message = "Has hecho click en el libro: " + Cell.title 

    def __init__(self, root) -> None:
        
        #Título de la ventana
        root.title("5 libros de Brandon Sanderson")

        #Celdas con el título y su ruta definidos
        self.cells = [

            Cell("Elantris", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\edited\\elantris.jpg"),
            Cell("El Camino de los Reyes","C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\edited\\elCaminoDeLosReyes.jpg"),
            Cell("El Imperio Final", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\edited\\elImperioFinal.jpg"),
            Cell("Escuadrón", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\edited\\escuadron.jpg"),
            Cell("Yumi y el Pintor de Pesadillas", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\edited\\yumiYElPintorDePesadillas.jpg")

        ]

        #Bucle para leer la lista
        for i, cell in enumerate(self.cells):

            libro = (Image.open(cell.path)).resize((100, 100), Image.Resampling.LANCZOS)
            cell.imagetk = ImageTk.PhotoImage(libro)
            label = ttk.Label(root, image = cell.imagetk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = 0,column = i)
            label.bind("<Button-1>",lambda event, cell = cell: self.onButtonClicked(cell))

        
            
        