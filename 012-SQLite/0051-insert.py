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
INSERT INTO Personas
VALUES(
NULL,
'Jose Vicente',
'523453245',
'info@jocarsa.com'
);
''')
#Mediante commit acabamos de ejecutar la consulta preparada
conexion.commit()




