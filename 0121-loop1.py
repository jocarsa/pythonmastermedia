# quiero un loop infinito que se ejecute en una ventana gráfica
import tkinter as tk

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
        self.master.after(1000,self.bucle)
# saco una ventana
root = tk.Tk()
# en la ventana gráfica ejecuto la Aplicacion
aplicacion = Aplicacion(root)
