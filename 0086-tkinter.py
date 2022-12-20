# Primero importo la librería
from tkinter import *
# Creo un marco en el cual voy a crear controles
marco = Frame(width=300,height=300)
# Empaqueto el marco dentro de la ventana
marco.pack(padx=30,pady=30)

# Creo un título, pero ese título está en memoria
titulo = Label(marco,text = "Programa Agenda")
# empaqueto el título en la ventana
titulo.pack(side=TOP)

# Creo un título, pero ese título está en memoria
titulo2 = Label(marco,text = "v0.1 Jose Vicente Carratala")
# empaqueto el título en la ventana
titulo2.pack(side=TOP)

fotografia = PhotoImage(file="josevicente.png")
imagen = Label(marco,image=fotografia,width=100,height=100)
imagen.pack()

boton = Button(text="Pulsame")
boton.pack()


