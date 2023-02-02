import tkinter as tk
from PIL import ImageTk, Image
#importaciones
import functions.image as image
import components.buttons as btn
import functions.filters as flt

#main window
root = tk.Tk()
root.geometry("300x100")
root.title("Filtros de imagen")

def convert(filepath):
    image_filter = Image.open(filepath).convert('LA')
    image_filter = ImageTk.PhotoImage(image_filter)
    image.constraint_label(root, image_filter)

def main():
    filepath = image.select_image()
    photo = image.photo_image(filepath)
    image.constraint_label(root, photo)
    btn.make_button(root, convert(filepath))

btn.button_select(root, main)


root.mainloop()