# w = write , a = append , r = read
archivo = open("miarchivo.txt",'r')
# i = iterador
for i in range(0,10000):
    linea = archivo.readline()
    if linea == "":
        break
    print(linea)
archivo.close()
