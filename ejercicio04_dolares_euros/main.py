#Ejercicio 04 - Cambio de dolares a euros

import os
os.system("cls")

#Solicitar datos al usuario

cambio = 1.33250

dolares = input("Introduce cantidad en dolares: ")
dolares = float(dolares)

euros = input("Introduce cantidad en euros: ")
euros = float(euros)

#Calculos

euros_resultado = dolares / cambio
dolares_resultado = euros * cambio

#Mostrar resultados

print("En euros es: " + str(round(euros_resultado, 2)))
print("En dolares es: " + str(round(dolares_resultado, 2)))