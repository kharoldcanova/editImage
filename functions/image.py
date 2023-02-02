from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk

def select_image():
    filepath = filedialog.askopenfilename()
    return filepath

def photo_image(filepath):
    image = Image.open(filepath)
    image = image.resize(size=[200, 200])
    photo = ImageTk.PhotoImage(image)
    return photo
   
def constraint_label(root, photo):
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
