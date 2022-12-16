def calculadora:
    # primero le pido al usuario la entrada

    print("Dime el operando 1:")
    operando1 = input()
    print("Dime el operando 2:")
    operando2 = input()
    print("Dime el operando que quieres usar (+,-,*,/)")
    operador = input()

    # convierto los datos a enteros para poder calcular
    operando1 = int(operando1)
    operando2 = int(operando2)

    # ahora realizo la operación que el usuario haya pedido
    if operador == "+":
        resultado = operando1 + operando2
    elif operador == "-":
        resultado = operando1 - operando2
    elif operador == "*":
        resultado = operando1 * operando2
    elif operador == "/":
        resultado = operando1 / operando2
    else:
        print("Lo que has introducido no es un operador válido")

    # convierto la suma en una cadena para sacarla por pantalla

    try:
        #escribo en pantalla
        resultado = str(resultado)
        print("El resultado de la operacion es:"+resultado)
    except:
        print("ha habido algún error")

    










