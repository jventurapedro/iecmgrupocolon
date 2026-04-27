#Ejercicio 07 - Condicion IF Anidado

import os
os.system("cls")

#Solicitar dados del usuario

momento = input("Ingrese el momento del día (m/t/n): ")
sexo = input("Ingrese el sexo (h/m): ")

#Calculo con IF Anidado

if momento == "m":
    if sexo == "h":
        print("Buenos días, señor")
    else:
        print("Buenos días, señora")
elif momento == "t":
    if sexo == "h":
        print("Buenas tardes, señor")
    else:
        print("Buenas tardes, señora")
elif momento == "n":
    if sexo == "h":
        print("Buenas noches, señor")
    else:
        print("Buenas noches, señora")
else:
    print("Momento del día no válido")      
