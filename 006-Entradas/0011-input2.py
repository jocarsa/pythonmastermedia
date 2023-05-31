print("Dime tu edad")
edad = input()
# primero convierto a entero para poder multiplicar
edad = int(edad)
# ahora puedo multiplicar
doble = edad*2
# lo convierto a string para poder concatenar
cadena = str(doble)
#y ahora saco por pantalla
print("El doble de tu edad es de: "+cadena)
