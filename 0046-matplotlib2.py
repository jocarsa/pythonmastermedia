#pip install matplotlib
import matplotlib.pyplot as grafica

etiquetas = 'Felipe', 'Daniela', 'Marc', 'Fernando'
tamanos = [5345, 53450, 64345, 34224]
explota = (0, 0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

graf, eje = grafica.subplots()
eje.pie(tamanos, explode=explota, labels=etiquetas, autopct='%1.1f%%',
        shadow=True, startangle=90,colors=["red","blue","green","yellow"])
eje.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

grafica.show()

