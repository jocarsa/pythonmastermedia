# De la librería Flask, importo todo lo que tiene flask
from flask import Flask
# Creamod una aplicación web vacía
app = Flask(__name__)

@app.route('/')

def run():
    return "<h1>Hola desde Flask</h1>"
