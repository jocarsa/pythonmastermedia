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
UPDATE Personas
SET telefono = 1234
WHERE Identificador = 2
;
''')

#Mediante commit acabamos de ejecutar la consulta preparada
conexion.commit()




