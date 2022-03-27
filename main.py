#Importacion de la libreria pillow
from PIL import Image, ImageFilter

DirectorioImagen = r'./índice.jpeg'

#Convirtiendo la imagen a blanco y negro
img = Image.open(DirectorioImagen).convert('LA')
img.show()

#Aplica a la imagen un filtro borroso.
img = Image.open(DirectorioImagen).filter(ImageFilter.BoxBlur(30))
img.show()

#Aplica a la imagen un filtro negativo.
img = Image.open(DirectorioImagen).filter(ImageFilter.FIND_EDGES)
img.show()

#Aplica a la imagen un filtro e dibujo.
img = Image.open(DirectorioImagen).filter(ImageFilter.CONTOUR)
img.show()



