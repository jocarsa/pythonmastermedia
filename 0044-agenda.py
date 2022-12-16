# Programa agenda
# (c) 2022 Jose Vicente Carratalá

agenda = []
def muestraAgenda():
    # Nada más empezar el programa quiero cargar los registros existentes
    archivo = open("agenda.csv",'r')
    for i in range(0,10000):
        linea = archivo.readline()
        partido = linea.split(",")
        agenda.append(partido)
        if linea == "":
            break
    archivo.close()
    print('''
    Bienvenid@ a tu agenda
    Selecciona una opción:
    1.-Listar registros
    2.-Insertar un registro
    3.-Guardar los registros en el disco
    ''')
    opcion = input()
    print("Has elegido la opcion: "+opcion)
    if opcion == "1":
        print("Vamos a listar los registros")
        contador = 1
        for registro in agenda:
            try:
                print("REGISTRO NUMERO "+str(contador)+"////////////////")
                print("nombre:"+registro[0])
                print("teléfono:"+registro[1])
                print("email:"+registro[2])
                contador = contador + 1
            except:
                pass
    elif opcion == "2":
        print("Vamos a insertar un nuevo registro")
        print("Indica el nombre de la persona:")
        nombre = input()
        print("Indica el teléfono de la persona:")
        telefono = input()
        print("Indica el email de la persona:")
        email = input()
        print("Gracias por introducir los datos")
        agenda.append((nombre,telefono,email))
    elif opcion == "3":
        archivo = open("agenda.csv",'w')
        for registro in agenda:
            archivo.write(registro[0]+","+registro[1]+","+registro[2]+"\n")
        archivo.close()
    muestraAgenda()

muestraAgenda()


    
