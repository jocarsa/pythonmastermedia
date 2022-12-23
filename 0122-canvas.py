# importo la librería gráfica
from tkinter import *

# creo un marco
marco = Frame(width=300,height=30)
marco.pack(padx=30,pady=30)

# creo un lienzo en el que voy a poder dibujar
lienzo = Canvas()
lienzo.create_oval(10,10,40,40)
lienzo.create_oval(60,10,200,140,fill = "orange")
lienzo.create_rectangle(160,210,240,240,fill = "red")
lienzo.pack(side=TOP)
