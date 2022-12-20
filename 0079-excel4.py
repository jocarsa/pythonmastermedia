# pip3 install  pandas
# Pandas para tratamiento masivo de información
# pip3 install openpyxl
# Tratamiento concreto de archivos de Excel
import pandas as pan

registros1 = pan.read_excel('Meses.xlsx')
valores1 = registros1.values

registros2 = pan.read_excel('Mesesmultiplicador.xlsx')
valores2 = registros2.values

resultado1 = []
resultado2 = []

print(valores1)
print(valores2)
# primer índice es la fila, segundo índice es la columna
for celdas in valores1[0]:
    resultado1.append(celdas)

for celdas in valores2[0]:
    resultado2.append(celdas)

print(resultado1)
print(resultado2)

final = []

for i in range(0,len(resultado1)):
    multiplicacion = resultado1[i]*resultado2[i]
    print(multiplicacion)
    final.append(multiplicacion)

print(final)
















