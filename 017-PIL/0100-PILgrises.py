# pip install pillow
from PIL import Image

mifoto = Image.open("josevicente.png")

anchura = mifoto.size[0]
altura = mifoto.size[1]
print(mifoto.size)

pixeles = mifoto.load()
# Ahora quiero barrer TODOS los pixeles de la imagen
# Primero barro en X
for x in range(0,anchura):
    # Luego barro en Y
    for y in range(0,altura):
        # Atrapo las coordenadas de color del pixel
        rojo = pixeles[x,y][0]
        # reemplazo el valor anterior en la tupla
        pixeles[x,y] = (rojo,rojo,rojo,255)


mifoto.save("resultado.png")
        
