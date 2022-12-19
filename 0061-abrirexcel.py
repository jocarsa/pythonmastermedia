# pip3 install  pandas
# pip3 install openpyxl
import pandas as pan

registros = pan.read_excel('Libro1.xlsx')
print(type(registros))
print(registros)
