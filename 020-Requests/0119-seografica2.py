# Primero importaremos librerías
# pip install requests
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
# pip install lxml
# pip install db-sqlite3
import sqlite3 as lite
import sys
# Preparo la base de datos
# Importo la librería de gráficas
import matplotlib.pyplot as grafica

# Primero me conecto a la base de datos
conexion = lite.connect("palabras.sqlite3")
# Establezco un cursor para realizar peticiones
cursor = conexion.cursor()
# Ejecuto una consulta SQL
cursor.execute('''
CREATE TABLE IF NOT EXISTS "palabras" (
	"Identificador"	INTEGER,
	"palabra"	TEXT,
	"url"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
''')
# por si la base de datos tiene resultados, los borro
cursor.execute('''
DELETE FROM palabras;
''')

# Me quiero conectar a una web y sacar su código

with requests.Session() as misesion:
    pagina = misesion.get("https://jocarsa.com")
    #print(pagina.content)

# Quiero poder procesar el código de esa web para sacar los textos
# Para cada una de las direcciones en la lista
for direccion in ['https://jocarsa.com']:
    # en primer lugar intenta
    try:
        respuesta = requests.get(direccion)
        respuesta.raise_for_status()
    # en el caso de que de error http (conexión a internet) sácamelo por pantalla
    except HTTPError as mierror:
        print(mierror)
    # en el caso de que de un error de Python
    except Exception as errorpython:
        print(errorpython)
    # en el caso de que todo vaya bien, sacamos la informacion
    else:
        # le indico el juego de caracteres que se va a encontrar
        respuesta.encoding ='utf-8'
        # proceso el contenido de la web como un arbol xml
        sopa = BeautifulSoup(respuesta.text,'lxml')
        # localizo una etiqueta concreta
        textos = sopa.find_all("p")
        # la imprimo en pantalla
        #print(textos)
        # para cada uno de los textos que me encuentro
        for lineas in textos:
            # convierto la linea a cadena
            cadena = str(lineas)
            # separo las palabras en base al espacio
            partido = cadena.split(" ")
            # imprimo los resultados en pantalla
            #print(partido)
            for palabra in partido:
                # Quiero meter cada una de esas palabras en una base de datos
                cursor.execute("INSERT INTO palabras VALUES (NULL,'"+str(palabra)+"','https://jocarsa.com')")
                #Mediante commit acabamos de ejecutar la consulta preparada
                conexion.commit()

# Realizaré una petición a la base de datos para obtener un filtrado
cursor.execute('''
SELECT COUNT(palabra),palabra
FROM palabras
WHERE 
palabra NOT IN ('y','la','con','de','en','a','el','las')
GROUP BY palabra
ORDER BY COUNT(palabra) DESC
LIMIT 4
''')


    
# Sacaré el resultado de esa petición en consola en modo texto
# Primero creo una lista vacía para introducir los datos de los valores
lista = []
# Creo otra lista vacía para introducir los valores de la columna
valores = []
datos = cursor.fetchall()

for i in datos:
    print(str(i[0])+" - "+str(i[1]))
    # añadimos el valor ala lista llamada "lista"
    lista.append(i[0])
    # Añadimos el valor de la columna a su lista correspondiente
    valores.append(i[1])

# Quiero un resultado en forma de gráfica
#etiquetas = ['red', 'blue', '_red', 'orange']
#colores = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
grafica.bar(valores,lista)
#Le pongo un título
grafica.ylabel("Palabras más frecuentes")
# Y lo saco por pantalla
grafica.show()











