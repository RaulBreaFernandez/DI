import tkinter as tk
import threading
import requests
from window import MainWindow

class LoadingWindow:

    def __init__(self, root):

        self.finished = False
        self.jsonData = []
        self.root = root
        self.root.title("Cargando...")

        self.root.geometry("170x120")
        x=(self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        y=(self.root.winfo_screenheight() - self.root.winfo_reqheight())/2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        
        self.label = tk.Label(self.root, text = "Cargando datos...", font = ("Arial", 14))
        self.label.pack(side = tk.TOP, pady = 10)
        labelBgColor = self.label.cget("bg")

        self.canvas = tk.Canvas(self.root, width = 60, height = 60, bg = labelBgColor)
        self.canvas.pack()

        self.progress = 0
        self.drawProgressCircle(self.progress)

        self.updateProgressCircle()

        self.thread = threading.Thread(target = self.fetchJsonData)
        self.thread.start()
        self.checkThread()

    def drawProgressCircle(self, progress):

        self.canvas.delete("progress")
        angle = int(360*(progress/100))

        self.canvas.create_arc(10, 10, 35, 35,
        start=0, extent=angle, tags="progress", outline="green", width=4, style=tk.ARC)

    def updateProgressCircle(self):

        if self.progress < 90:

            self.progress += 10

        else:

            if self.progress == 90:

                self.progress += 9
            
            else:

                self.progress = 0

        self.drawProgressCircle(self.progress)
        self.root.after(100, self.updateProgressCircle)

    def fetchJsonData(self):

        response = requests.get("https://raw.githubusercontent.com/RaulBreaFernandez/DI/main/catalog.json")

        if response.status_code == 200:

            self.jsonData = response.json()
            self.finished = True

    def checkThread(self):

        if self.finished:

            self.root.destroy()
            self.launchMainWindow(self.jsonData)
        
        else:

            self.root.after(100, self.checkThread)

    def launchMainWindow(self, jsonData):

        root = tk.Tk()
        app = MainWindow(root, jsonData)
        root.mainloop()

        


    
