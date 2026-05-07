import os

os.system("cls")

# Programa que explica como calcular potencias en Python

base = input("Introduce la base: ")     # 3
exponente = input("Introduce el exponente: ")

base = float(base)  # 3.000000000
exponente = int(exponente)

valor1 = base**exponente        #Esta es una opcion de potencia

valor2 = pow(base, exponente)   #Esta es la funcion de potencia

valor2 = round(pow(base, exponente), 2)     #Esta es la funcion de potencia redeondeando a 2 decimales

print("El resultado es: " + str(valor1) + " " + str(valor2))

