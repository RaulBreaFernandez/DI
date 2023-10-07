from tkinter import Tk, ttk
from noWindow import showNo
from yesWindow import showYes

class MainWindow():

    def onButtonClicked(self):

        pass

    def __init__(self, root):
        
        root.title("MainWindow")
        self.root = root

        #Marco
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        #Etiqueta
        self.label = ttk.Label(self.frame, text = "¿Crees en la vida extraterrestre?")
        self.label.pack()

        #Botón
        self.button1 = ttk.Button(self.frame, text = "Yes", command = showYes)
        self.button1.pack(side = "left")

        self.button2 = ttk.Button(self.frame, text = "No", command = showNo)
        self.button2.pack(side = "right", padx = 5)