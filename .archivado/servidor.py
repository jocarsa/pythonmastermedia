# flask --app servidor run
# De la librería Flask, importo todo lo que tiene flask
from flask import Flask
# Creamod una aplicación web vacía
app = Flask(__name__)

@app.route('/')

def corre():
    cadena = "<h1>La web de Jose Vicente</h1>"
    cadena = cadena + "<style>h1{color:red;}</style>"
    cadena = cadena + "<p>Esto es un párrafo en html</p>"
    return cadena
