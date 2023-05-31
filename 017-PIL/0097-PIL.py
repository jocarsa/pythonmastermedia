# pip install pillow
from PIL import Image

mifoto = Image.open("josevicente.png")

anchura = mifoto.size[0]
altura = mifoto.size[1]
print(mifoto.size)
