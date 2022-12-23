# quiero un loop infinito que se ejecute en una ventana gráfica
import tkinter as tk
import random

class Personaje():
    def __init__(self,x,y,z):
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 300)
        self.z = z

personajes = []
for i in range(0,100):
    personajes.append(Personaje(10,10,0))

print(personajes)

# creo una clase que se va a ejecutar en bucle
class Aplicacion(object):
    # método constructor, que se tiene que ejecutar una vez
    def __init__(self,master):
        # esto es obligatorio
        self.master = master
        # Dentro de un segundo, entra en el bucle
        self.master.after(1000,self.bucle)
    # el método bucle se ejecuta una vez cada X milisegundos
    def bucle(self):
        #Este método se va a ejecutar de forma continua
        print("el programa ha arrancando y empezará a dar vueltas")
        # print(personajes)
        for personaje in personajes:
            # en cada iteracion quiero que el personaje se mueva un poco
            personaje.x = personaje.x + random.randint(-2,2)
            personaje.y = personaje.y + random.randint(-2,2)
            lienzo.create_oval(personaje.x,personaje.y,personaje.x+10,personaje.y+10)
        self.master.after(1000,self.bucle)
# saco una ventana
root = tk.Tk()
# Dentro de la ventana, he creado un canvas para pintar a los personajes
lienzo = tk.Canvas()
# añado el lienzo a la ventana de TKInter
lienzo.pack()
# en la ventana gráfica ejecuto la Aplicacion
aplicacion = Aplicacion(root)
