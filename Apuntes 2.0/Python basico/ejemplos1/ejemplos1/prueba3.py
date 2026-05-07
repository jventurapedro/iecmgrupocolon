


import os                                   # Libreria para trabajar con metodos del sistema operativo

os.system("cls")                            # Mediante el comando CLS borramos la pantalla del terminal


num1 = input("Introduce un numero: ")       # Pedimos al usuario el primer numero
num1 = float(num1)                          # Como lo que se introduce se lee como texto, lo pasamos a decimal

num2 = input("Introduce otro numero: ")         
num2 = float(num2)                             

suma = num1 + num2                          # Calculamos la suma
suma = round(suma, 2)                       # Redondeamos a dos decimales

resta = num1 - num2
resta = round(resta, 2)

producto = num1 * num2
producto = round(producto, 2)

division = num1 / num2
division = round(division, 2)

resto = num1 % num2
resto = round(resto)

print("La suma de los numeros es: " + str(suma))            # La funcion STR pasa un numero a formato texto
print("La resta de los numeros es: " + str(resta))
print("El producto de los numeros es: " + str(producto))
print("La division de los numeros es: " + str(division))
print("El resto de los numeros es: " + str(resto))
