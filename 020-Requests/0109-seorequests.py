# Primero importaremos librerías
# pip install requests

import requests

# Me quiero conectar a una web y sacar su código

with requests.Session() as misesion:
    pagina = misesion.get("https://jocarsa.com")
    print(pagina.content)

# Quiero poder procesar el código de esa web para sacar los textos

# Quiero meter cada una de esas palabras en una base de datos

# Realizaré una petición a la base de datos para obtener un filtrado

# Sacaré el resultado de esa petición en consola en modo texto

# Quiero un resultado en forma de gráfica
