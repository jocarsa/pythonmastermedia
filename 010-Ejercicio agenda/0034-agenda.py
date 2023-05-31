# Programa agenda
# (c) 2022 Jose Vicente Carratalá

agenda = []

print('''
Bienvenid@ a tu agenda
Selecciona una opción:
1.-Listar registros
2.-Insertar un registro
''')
opcion = input()
print("Has elegido la opcion: "+opcion)
if opcion == "1":
    print("Vamos a listar los registros")
    print(agenda)
elif opcion == "2":
    print("Vamos a insertar un nuevo registro")
    print("Indica el nombre de la persona:")
    nombre = input()
    print("Indica el teléfono de la persona:")
    telefono = input()
    print("Indica el email de la persona:")
    email = input()
