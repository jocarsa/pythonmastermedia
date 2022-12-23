import tkinter as tk

raiz = tk.Tk()

def delante(e):
    print("Movemos hacia delante")
def detras(e):
    print("Movemos hacia atrás")
def izquierda(e):
    print("Movemos hacia la izquierda")
def derecha(e):
    print("Movemos hacia la derecha")
    
raiz.bind("w",delante)
raiz.bind("s",detras)
raiz.bind("a",izquierda)
raiz.bind("d",derecha)
