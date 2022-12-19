from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    cadena = ""
    cadena = cadena + """
            <!doctype html>
            <html>
                <head>
                    <style>
                        .dia{
                            width:100px;
                            height:100px;
                            border:1px solid;
                            float:left;
                            }
                    </style>
                </head>
                <body>

            """
    for i in range(1,31):
        cadena = cadena + '<div class="dia">'+str(i)+'</div>'
        if i % 7 == 0:
            cadena = cadena + '<div style="clear:both"></div>'
    return cadena
