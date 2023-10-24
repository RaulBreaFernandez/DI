from PIL import Image, ImageTk
import requests
from io import BytesIO

class Cell:

    def __init__(self, title, description, url):

        self.title = title
        self.description = description
        self.image = self.loadImageFromUrl(url).resize((100, 100), resample = Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(self.image)

    def loadImageFromUrl(self, url):

        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        return img
        