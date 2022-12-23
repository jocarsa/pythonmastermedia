# quiero un loop infinito que se ejecute en una ventana gráfica
import tkinter as tk
import random
import math



class Personaje():
    def __init__(self,x,y,z):
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 300)
        self.z = z
        
class Jugador():
    def __init__(self,x,y,z,vida):
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 300)
        self.z = z
        self.vida = vida

personajes = []
for i in range(0,10):
    personajes.append(Personaje(10,10,0))

jugador = Jugador(10,10,0,100)

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
        # borro todo lo que hubiera
        lienzo.delete("all")
        #Este método se va a ejecutar de forma continua
        ##print("el programa ha arrancando y empezará a dar vueltas")
        # print(personajes)
        for personaje in personajes:
            # en cada iteracion quiero que el personaje se mueva un poco
            personaje.x = personaje.x + random.randint(-2,2)
            personaje.y = personaje.y + random.randint(-2,2)
            #lienzo.create_oval(personaje.x,personaje.y,personaje.x+10,personaje.y+10)
            lienzo.create_image(personaje.x, personaje.y, image=impersonaje)
            # calculo la distancia
            p = [personaje.x, personaje.y]
            q = [jugador.x, jugador.y]
            distancia = math.dist(p, q)
            if distancia < 20:
                jugador.vida= jugador.vida - 1
                print(jugador.vida)
        #lienzo.create_oval(jugador.x,jugador.y,jugador.x+10,jugador.y+10,fill="black")
        if jugador.vida < 0:
            lienzo.create_image(jugador.x, jugador.y, image=immuerto)
        else:
            lienzo.create_image(jugador.x, jugador.y, image=imjugador)
        self.master.after(33,self.bucle)
# saco una ventana
raiz = tk.Tk()
impersonaje = tk.PhotoImage(file='josevicentesprite.png')
imjugador = tk.PhotoImage(file='anasprite.png')
immuerto = tk.PhotoImage(file='calavera.png')

def delante(e):
    #print("Movemos hacia delante")
    jugador.y = jugador.y-5
def detras(e):
    #print("Movemos hacia atrás")
    jugador.y = jugador.y+5
def izquierda(e):
    #print("Movemos hacia la izquierda")
    jugador.x = jugador.x-5
def derecha(e):
    #print("Movemos hacia la derecha")
    jugador.x = jugador.x+5
    
raiz.bind("w",delante)
raiz.bind("s",detras)
raiz.bind("a",izquierda)
raiz.bind("d",derecha)

# Dentro de la ventana, he creado un canvas para pintar a los personajes
lienzo = tk.Canvas()
# añado el lienzo a la ventana de TKInter
lienzo.pack()
# en la ventana gráfica ejecuto la Aplicacion
aplicacion = Aplicacion(raiz)

raiz.mainloop()
