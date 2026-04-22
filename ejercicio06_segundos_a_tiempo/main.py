#Ejercicio 06 - Segundos a dias, horas, minutos

import os
os.system("cls")

#Solicitar datos al usuario

segundosentrada = input("Introduce un numero de segundos: ")
segundosentrada = int(segundosentrada)

segundosinicio = segundosentrada

#Calculos

dias = segundosentrada // 86400
segundosentrada = segundosentrada % 86400

horas = segundosentrada // 3600
segundosentrada = segundosentrada % 3600

minutos = segundosentrada // 60
segundos = segundosentrada % 60

#Mostrar resultados

print("Has introducido: " + str(segundosinicio))
print("Son " + str(dias) + " dias, " + str(horas) + " horas, " + str(minutos) + " minutos y " + str(segundos) + " segundos")