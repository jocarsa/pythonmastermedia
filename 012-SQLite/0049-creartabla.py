# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# pip install pysqlite3

import sqlite3 as lite
import sys
# Primero me conecto a la base de datos
conexion = lite.connect("mibasededatos.sqlite3")
# Establezco un cursor para realizar peticiones
cursor = conexion.cursor()
# Ejecuto una consulta SQL
cursor.execute('''
CREATE TABLE "Personas" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"telefono"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
''')




