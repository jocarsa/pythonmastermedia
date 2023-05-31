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
        verde = pixeles[x,y][1]
        azul = pixeles[x,y][2]
        rojo = rojo*2
        verde = verde*2
        azul = azul*2
        if rojo > 255:
            rojo = 255
        if verde > 255:
            verde = 255
        if azul > 255:
            azul = 255
        # reemplazo el valor anterior en la tupla
        pixeles[x,y] = (rojo,verde,azul,255)


mifoto.save("resultado.png")
        
