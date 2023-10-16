import tkinter as tk
from PIL import Image, ImageTk

class Cell:

    #Constructor
    def __init__(self, title, path, description):

        self.title = title
        self.path = path
        self.description = description
        
        #Abrimos la imagen, la redimensionamos y la guardamos en la variable "resizedImage"
        resizedImage = (Image.open(self.path)).resize((100, 100), Image.Resampling.LANCZOS)
        
        #Convertimos la imagen a objeto "PhotoImage" para poder usarla en widgets de tkinter
        self.imageTk = ImageTk.PhotoImage(resizedImage)