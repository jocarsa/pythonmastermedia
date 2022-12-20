# Primero importo la librería
from tkinter import *

def guardaInformacion():
    nombrelocal = str(tknombre.get())
    telefonolocal = str(tktelefono.get())
    emaillocal = str(tkemail.get())
    cadena = "Nombre:"+nombrelocal+" Telefono:"+telefonolocal+" Email:"+emaillocal
    etiquetatemporal.config(text=cadena) 

# Creo un marco en el cual voy a crear controles
marco = Frame(width=300,height=300)
# Empaqueto el marco dentro de la ventana
marco.pack(padx=30,pady=30)

tknombre = StringVar()
tktelefono = StringVar()
tkemail = StringVar()

# Creo un título, pero ese título está en memoria
titulo = Label(marco,text = "Programa Agenda")
# empaqueto el título en la ventana
titulo.pack()

etiquetanombre = Label(marco,text = "Introduce el nombre:")
etiquetanombre.pack(side=TOP)
nombre = Entry(marco,textvariable=tknombre)
nombre.pack()

etiquetatelefono = Label(marco,text = "Introduce el teléfono:")
etiquetatelefono.pack(side=TOP)
telefono = Entry(marco,textvariable=tktelefono)
telefono.pack()

etiquetaemail = Label(marco,text = "Introduce el email:")
etiquetaemail.pack(side=TOP)
email = Entry(marco,textvariable=tkemail)
email.pack()

botonenvia = Button(marco,text="Guardar información",command=guardaInformacion)
botonenvia.pack()

etiquetatemporal = Label(marco,text = "Aquí te voy a decir cosas")
etiquetatemporal.pack(side=TOP)



