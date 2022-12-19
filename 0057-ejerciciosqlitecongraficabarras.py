# https://jocarsa.com/registros.db
# Primero importo la librería de conexión a base de datos
# IMPORTACIONES ###########################
import sqlite3 as lite
# Importo la librería de sistema por si acaso
import sys
# Importo la librería de gráficas
import matplotlib.pyplot as grafica

# DECLARACIONES ###########################
# Primero creo una lista vacía para introducir los datos de los valores
lista = []
# Creo otra lista vacía para introducir los valores de la columna
valores = []

# Primero me conecto a la base de datos
conexion = lite.connect("registros.db")
# Establezco un cursor para realizar peticiones
cursor = conexion.cursor()
# Ahora seleccionamos las conexiones por cada hora del día
cursor.execute('''
SELECT
COUNT(hora) AS numero,
hora
FROM logs
GROUP BY hora
;
''')
# Metemos el resultado de la petición en una lista
datos = cursor.fetchall()
# Recorremos la lista con un bucle for
for i in datos:
    print(i)
    # añadimos el valor ala lista llamada "lista"
    lista.append(i[0])
    # Añadimos el valor de la columna a su lista correspondiente
    valores.append(i[1])

#Mediante commit acabamos de ejecutar la consulta preparada
conexion.commit()
# Preparo una gráfica de barras
grafica.bar(valores,lista)
#Le pongo un título
grafica.ylabel("Visitantes por hora del día")
# Y lo saco por pantalla
grafica.show()
