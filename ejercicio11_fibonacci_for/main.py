# Ejercicio 11 - Sucesión de Fibonacci usando For

import os
os.system("cls")


#Creamos una lista con los 2 primeros numeros 
lista_fibonacci = [0, 1]

#CREAMOS SIEMPRE LA VARIABLE FUERA Y LUEGO LA SOLICITAMOS!
cantidad = ""

#OJO WHILE TRUE ES UN BUCLE INFINITO, SI NO PONEMOS UN BREAK, EL PROGRAMA SEGUIRA PIDIENDO LA CANTIDAD DE NUMEROS A MOSTRAR
while True:
    cantidad = input("¿Cuántos números desea imprimir? (mínimo 2): ")

    #VALIDAMOS SI ESTA VACIO NO SEGUIREMOS !
    if cantidad == "":
        print("¡Error!: No puede estar vacío. (mínimo 2):")
        continue

    #VALIDAMOS SI ES UN NUMERO, SI NO LO ES, SEGUIREMOS PIDIENDO UN NUMERO VALIDO
    if not cantidad.isdigit():
        print("¡Error! No es un número. (mínimo 2):")
        continue

    if (cantidad.isdigit()):
        cantidad = int(cantidad)
        if cantidad >= 2:
            print("¡Número válido!") 
            break 

        elif cantidad < 2:
            print("¡Error! El número debe ser mayor o igual a 2. (mínimo 2):")
            continue


for i in range(cantidad - 2):
        # Calculamos el siguiente número de Fibonacci sumando los dos últimos números de la lista
        ultimo = lista_fibonacci[len(lista_fibonacci) - 1]  # Último número de la lista
        penultimo = lista_fibonacci[len(lista_fibonacci) - 2]  # Penúltimo número de la lista
        numero = ultimo + penultimo  # Siguiente número de Fibonacci

        #Guardamos en la lista.
        lista_fibonacci.append(numero)

for i in range(cantidad):
     
     print(lista_fibonacci[i], end="\n")  # Imprimimos cada número de la lista hasta la cantidad solicitada