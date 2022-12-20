'''
Problema: Entre el rayo y el trueno,
introduciendo el usuario los segundos que han pasado
desde el rayo hasta el trueno,
calcular la distancia hasta la tormenta
'''

# PRIMERO TOMO LOS DATOS DE ENTRADA
# En primer lugar, necesito saber la velocidad del sonido
# (parece un constante)
VELOCIDAD_SONIDO = 343
# A continuación le pregunto al usuario los segundos que han pasado
# Parece una entrada de usuario
print("Indica el tiempo que ha pasado:")
tiempo = input()

# SEGUNDO, REALIZO CÁLCULOS CON LOS DATOS QUE ME HAN DADO
# la distancia es igual al tiempo multiplicado por la velocidad del sonido
# multiplico lal entrada del usuario por la constante
distancia = int(tiempo)*VELOCIDAD_SONIDO

# TERCERO, SACO RESULTADOS POR PANTALLA
# hago un print de lo que quiero mostrar al usuario
print("La distancia a la tormenta es de : "+str(distancia)+" metros")


