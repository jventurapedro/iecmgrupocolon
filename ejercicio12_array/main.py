#Ejercicio 12 - Busqueda de datos en un array

import os
os.system("cls")

import random

#Creamos el array con 10 numeros aleatorios entre -100 y 100, sin repetir y sin incluir el 0

numero = []

#Aqui vamos generar 10 numeros distintos entre -100 y 100, sin incluir el 0.

while len(numero) < 10:
    n = random.randint(-100, 100)

    #validamos que el numero no sea 0 y que no se repita en la lista
    if n != 0 and n not in numero:
        numero.append(n)

#Aqui vamos a ordenar el array
numero.sort()

#Mostramos el array ordenado
print("Listado de numeros: ", numero)

#Buscamos el mayor y el menor numero del array
mayor = numero[-1]
menor = numero[0]

#Ahora vamos a sumar las variables con la primera posicion del array.
suma_mayor = mayor + numero[0]
suma_menor = menor + numero[0]

#Mostramos el resultado de la suma
suma_total = 0 
suma_positivos = 0
suma_negativos = 0

#Ahora utilicemos el FOR para recorrer el array y sumar los numeros positivos, negativos y el total de la suma de todos los numeros.

for n in numero:
        mayor = n
if n < menor:
        menor = n
suma_total += n
if n > 0:
        suma_positivos += n
elif n < 0:
        suma_negativos += n

media = suma_total / len(numero)

print("El mayor numero es: ", mayor)
print("El menor numero es: ", menor)
print("La suma total de los numeros es: ", suma_total)
print("La suma de los numeros positivos es: ", suma_positivos)
print("La suma de los numeros negativos es: ", suma_negativos)
print("La media de los numeros es: ", media)

