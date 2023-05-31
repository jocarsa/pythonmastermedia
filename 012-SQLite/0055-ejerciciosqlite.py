# https://jocarsa.com/registros.db

import sqlite3 as lite
import sys
# Primero me conecto a la base de datos
conexion = lite.connect("registros.db")
# Establezco un cursor para realizar peticiones
cursor = conexion.cursor()
# Ahora seleccionamos
cursor.execute('''
SELECT
COUNT(hora) AS numero,
hora
FROM logs
GROUP BY hora
;
''')

datos = cursor.fetchall()

for i in datos:
    print(i)

#Mediante commit acabamos de ejecutar la consulta preparada
conexion.commit()
