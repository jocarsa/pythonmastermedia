# Primero importo la librería de Tkinter
# TK es la antigua librería de Widgets de TK (hasta 2002)
import tkinter as tk
# TTK es la nueva librería de Widgets de TK
from tkinter import ttk
# Importo las librerías de bases de datos
import sqlite3 as lite
import sys

ventana = tk.Tk()
ventana.title("Ejercicio SQLite")
tabla = ttk.Treeview(columns=("nombre", "telefono","email"))
tabla.heading("#0", text="Identificador")
tabla.heading("nombre", text="Nombre")
tabla.heading("telefono", text="Teléfono")
tabla.heading("email", text="Email")
# Primero me conecto a la base de datos
conexion = lite.connect("mibasededatos.sqlite3")
# Establezco un cursor para realizar peticiones
cursor = conexion.cursor()
cursor.execute("SELECT * FROM Personas;")
datos = cursor.fetchall()
for tupla in datos:
    tabla.insert(
        "",
        tk.END,
        text=tupla[0],
        values=(tupla[1], tupla[2],tupla[3])
    )

tabla.pack()
ventana.mainloop()






