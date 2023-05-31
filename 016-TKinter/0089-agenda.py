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

etiquetanombre = Label(marco,text = "Introduce el nombre:")
etiquetanombre.pack(side=TOP)
nombre = Entry(marco)
nombre.pack()

etiquetatelefono = Label(marco,text = "Introduce el teléfono:")
etiquetatelefono.pack(side=TOP)
telefono = Entry(marco)
telefono.pack()

etiquetaemail = Label(marco,text = "Introduce el email:")
etiquetaemail.pack(side=TOP)
email = Entry(marco)
email.pack()

botonenvia = Button(marco,text="Guardar información")
botonenvia.pack()

etiquetatemporal = Label(marco,text = "Aquí te voy a decir cosas")
etiquetatemporal.pack(side=TOP)



