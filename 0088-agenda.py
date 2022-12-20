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

etiquetenombre = Label(marco,text = "Introduce el nombre:")
etiquetenombre.pack(side=TOP)
nombre = Entry(marco)
nombre.pack()



