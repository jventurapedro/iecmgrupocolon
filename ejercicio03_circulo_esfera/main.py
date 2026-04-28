#Ejercicio 03 - Calculo de circunferencia, area y volumen

import os
os.system("cls")

#Solicitar datos al usuario

pi = 3.1416

radio = input("Introduce el radio: ")
radio = float(radio)

#Calculos

perimetro = 2 * pi * radio
area = pi * (radio ** 2)
volumen = (4 * pi * (radio ** 3)) / 3

#Mostrar resultados

print("El perimetro es: " + str(round(perimetro, 2)))
print("El area es: " + str(round(area, 2)))
print("El volumen es: " + str(round(volumen, 2)))