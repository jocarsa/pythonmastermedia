# pip3 install  pandas
# Pandas para tratamiento masivo de información
# pip3 install openpyxl
# Tratamiento concreto de archivos de Excel
import pandas as pan

registros = pan.read_excel('Meses.xlsx')
print(type(registros))
print(registros)
print(registros.values)
