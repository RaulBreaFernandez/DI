from tkinter import ttk, messagebox
import tkinter as tk
from cell import Cell
from PIL import Image, ImageTk 
from detailWindow import DetailWindow

class MainWindow():

    def onButtonClicked(self, cell):

        #Mensaje que aparece cuando haces click en un libro.
        detail_window = DetailWindow(self.root, cell.title, cell.imageTk, cell.description)

    def __init__(self, root):
        
        #Título de la ventana
        root.title("5 libros de Brandon Sanderson")
        self.root = root

        #Celdas con el título y su ruta definidos
        self.cells = [

            Cell("Elantris", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\elantris.jpg","'Elantris' es una novela de fantasía escrita por Brandon Sanderson que se desarrolla en la ciudad de Elantris, una vez gloriosa y mágica, pero ahora en ruinas."),
            Cell("El Camino de los Reyes","C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\elCaminoDeLosReyes.jpg", "'El Camino de los Reyes' es el primer libro de la serie 'El Archivo de las Tormentas' escrita por Brandon Sanderson. La historia se desarrolla en un mundo ficticio llamado Roshar."),
            Cell("El Imperio Final", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\elImperioFinal.jpg", "'El Imperio Final' es el primer libro de la trilogía 'Nacidos de la Bruma' escrita por Brandon Sanderson. La historia se desarrolla en un mundo asolado por cenizas y brumas."),
            Cell("Escuadrón", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\edited\\escuadron.jpg","'Escuadrón' es una novela escrita por Brandon Sanderson que se sitúa en un futuro distópico. La historia sigue a Spensa, una joven con el sueño de convertirse en una piloto de combate y defender su planeta."),
            Cell("Yumi y el Pintor de Pesadillas", "C:\\Users\\rauli\\Documents\\Proyectos\\Clase\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\yumiYElPintorDePesadillas.jpg","Yumi viene de una tierra de jardines, meditación y espíritus, mientras que Pintor vive en un mundo de oscuridad, tecnología y pesadillas. De pronto sus vidas se ven extrañamente entrelazadas.")

        ]

        #Bucle para leer la lista
        for i, cell in enumerate(self.cells):

            label = ttk.Label(root, image = cell.imageTk, text = cell.title, compound = tk.BOTTOM)
            label.grid(row = 0,column = i)
            label.bind("<Button-1>",lambda event, cell = cell: self.onButtonClicked(cell))

        
            
        