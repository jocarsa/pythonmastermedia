# quiero un loop infinito que se ejecute en una ventana gráfica
import tkinter as tk

class Personaje():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

personajes = []
for i in range(0,10):
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
        print(personajes)
        self.master.after(1000,self.bucle)
# saco una ventana
root = tk.Tk()
# en la ventana gráfica ejecuto la Aplicacion
aplicacion = Aplicacion(root)
