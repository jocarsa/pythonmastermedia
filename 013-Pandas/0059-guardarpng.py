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
# PIDO LOS USUARIOS DE WINDOWS #############################
# Ahora seleccionamos las conexiones por cada hora del día
cursor.execute('''
SELECT
COUNT(navegador) AS numero,
'Windows'
FROM logs
WHERE navegador LIKE '%Windows%'
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
# PIDO LOS USUARIOS DE MAC #############################
cursor.execute('''
SELECT
COUNT(navegador) AS numero,
'macOS'
FROM logs
WHERE navegador LIKE '%Macintosh%'
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
# PIDO LOS USUARIOS DE LINUX #############################
cursor.execute('''
SELECT
COUNT(navegador) AS numero,
'Linux'
FROM logs
WHERE navegador LIKE '%Linux%'
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

# Ahora saco la grafica de tarta
# Preparo las variables que requiere la gráfica
graf, eje = grafica.subplots()
# Llamo a una gráfica de tarta
eje.pie(lista,  labels=valores, autopct='%1.1f%%',
        shadow=True, startangle=90,colors=["red","blue","green","yellow"])
# Los ejes de la gráfica se representan como iguales
eje.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# Muestro la gráfica

grafica.savefig('paramarlon.png')
grafica.show()

