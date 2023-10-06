from tkinter import Tk, ttk

class MainWindow():

    def onButtonClicked(self):

        pass

    def __init__(self, root) -> None:
        
        self.root = root

        #Marco
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        #Etiqueta
        self.label = ttk.Label(self.frame, text = "Este es el ejercicio 2 del sprint 1")
        self.label.pack()

        #Botón
        self.button = ttk.Button(self.frame, text = "Realizar la acción", command = self.onButtonClicked)
        self.button.pack()