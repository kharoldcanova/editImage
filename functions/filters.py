#Importacion de la libreria pillow
from PIL import Image, ImageFilter

# DirectorioImagen = r'./índice.jpeg'


# #Convirtiendo la imagen a blanco y negro
# img = Image.open(DirectorioImagen).convert('LA')
# img.show()

# #Aplica a la imagen un filtro borroso.
# img = Image.open(DirectorioImagen).filter(ImageFilter.BoxBlur(30))
# img.show()

# #Aplica a la imagen un filtro negativo.
# img = Image.open(DirectorioImagen).filter(ImageFilter.FIND_EDGES)
# img.show()

# #Aplica a la imagen un filtro e dibujo.
# img = Image.open(DirectorioImagen).filter(ImageFilter.CONTOUR)
# img.show()

def convert_LA(filepath):
    img = Image.open(filepath).convert('LA')
    return img

def choise(filepath, filter):
    if (filter == " B/N"):
        img = Image.open(filepath).convert('LA')
        return img
    if (filter == "BLUER"):
        img = Image.open(filepath).filter(ImageFilter.BoxBlur(30))
        return img
    if (filter == "NEGATIVO"):
        img = Image.open(filepath).filter(ImageFilter.FIND_EDGES)
        return img
    if(filter == "CONTORNO"):
        img = Image.open(filepath).filter(ImageFilter.CONTOUR)
        return img