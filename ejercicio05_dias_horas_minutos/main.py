#Ejercicio 05 - Dias, horas y minutos a segundos

import os
os.system("cls")

#Solicitar datos al usuario

dias = input("Introduce numero de dias: ")
dias = int(dias)

horas = input("Introduce numero de horas: ")
horas = int(horas)

minutos = input("Introduce numero de minutos: ")
minutos = int(minutos)

#Calculos

segundos = (dias * 86400) + (horas * 3600) + (minutos * 60)

#Mostrar resultados

print("El numero total de segundos es: " + str(segundos))