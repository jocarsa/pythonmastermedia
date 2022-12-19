# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# pip install pysqlite3

import sqlite3 as lite
import sys
# Primero me conecto a la base de datos
conexion = lite.connect("mibasededatos.sqlite3")
# Establezco un cursor para realizar peticiones
cursor = conexion.cursor()
# Ahora insertamos
cursor.execute('''
SELECT * FROM Personas;
''')

datos = cursor.fetchall()

for i in datos:
    print("El identificador es:"+str(i[0]))
    print("El nombre es:"+i[1])
    print("El telefono es:"+i[2])
    print("El email es:"+i[3])
    print("/////////////////////////////////////")

#Mediante commit acabamos de ejecutar la consulta preparada
conexion.commit()




