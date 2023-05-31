# Primero importo la librería de Tkinter
# TK es la antigua librería de Widgets de TK (hasta 2002)
import tkinter as tk
# TTK es la nueva librería de Widgets de TK
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejercicio SQLite")
tabla = ttk.Treeview(columns=("nombre", "telefono","email"))
tabla.heading("#0", text="Identificador")
tabla.heading("nombre", text="Nombre")
tabla.heading("telefono", text="Teléfono")
tabla.heading("email", text="Email")
tabla.insert(
    "",
    tk.END,
    text="1",
    values=("Nombre", "Telefono","Email")
)

tabla.pack()
ventana.mainloop()






