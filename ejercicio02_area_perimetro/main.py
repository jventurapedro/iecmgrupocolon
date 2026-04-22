#Ejercicio 02 - Calculo de area y perimetro

import os
os.system("cls")

#Solicitar datos al usuario

base = input("Introduce la base: ")
altura = input("Introduce la altura: ")

base = float(base)
altura = float(altura)

#Calculos

area = base * altura
perimetro = 2 * (base + altura)

#Mostrar resultados

print("El area es: " + str(round(area, 2)))
print("El perimetro es: " + str(round(perimetro, 2)))