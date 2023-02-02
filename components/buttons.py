import tkinter as tk
import functions.filters as flt

#button selected
def button_select(root, function):
    #create a button
    button = tk.Button(root, text="Seleccione el archivo", command=function)
    button.pack()

#buttons of filters
def make_button(root, function):
    button = tk.Button(root, text="name", command=function)
    button.pack()



# def buttons_filters(root):
#     names = ["Blanco y Negro", "Borroso", "Negativo", "Contorno"]
#     functions = [flt.comvert_LA()]
#     for i in names:
#         make_button(root, i, function=i)
    