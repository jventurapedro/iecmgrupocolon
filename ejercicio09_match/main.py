#Ejercicio 09 - SWITCH (MATCH)

import os
from unittest import case
os.system("cls")

#Solicitar datos
momento = input("Momento del día (m-mañana, t-tarde, n-noche): ").lower()
persona = ""
saludo = "" 

#Evaluar momento
if momento not in ["m", "t", "n"]:
    print("Momento no válido. Escribe 'm' (mañana), 't' (tarde) o 'n' (noche)")

else:
    match momento:
        case "m":
            saludo = "Buenos días"
        case "t":
            saludo = "Buenas tardes"
        case "n":
            saludo = "Buenas noches"
        case _:
            saludo = "momento no valido"

    #Evaluar sexo
    sexo = input("Sexo (m-masculino, f-femenino): ").lower()
    if sexo not in ["m", "f"]:
        print("Sexo no válido. Escribe 'm' (masculino) o 'f' (femenino)")   

    else:
        match sexo:
            case "m":
                persona = "señor"
            case "f":
                persona = "señora"
            case _:
                persona = "sexo no valido"

#Mostrar resultado
print(saludo + " " + persona)