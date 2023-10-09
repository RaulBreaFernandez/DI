from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk 

class MainWindow():

    def onButtonClicked(self):

        #Mensaje que aparece cuando haces click en un libro.
        message = "Has hecho click en el libro: " + Cell.title 
        messagebox.showinfo("Información", message)

    def __init__(self, root) -> None:
        
        #Título de la ventana
        root.title("5 libros de Brandon Sanderson")
        self.root = root

        #Celdas con el título y su ruta definidos
        self.cells = [

            Cell("Elantris", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\elantris.jpg"),
            Cell("El Camino de los Reyes","C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\elCaminoDeLosReyes.jpg"),
            Cell("El Imperio Final", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\elImperioFinal.jpg"),
            Cell("Escuadrón", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\edited\\escuadron.jpg"),
            Cell("Yumi y el Pintor de Pesadillas", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\yumiYElPintorDePesadillas.jpg")

        ]

        #Bucle para leer la lista
        for i, cell in enumerate(self.cells):

            label = ttk.Label(root, image = cell.imageTk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = 0,column = i)
            label.bind("<Button-1>",lambda event, cell = cell: self.onButtonClicked(cell))

        
            
        