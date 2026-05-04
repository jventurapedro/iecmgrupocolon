# Ejercicio 07 - Condicion IF Anidado

import os
os.system("cls")

while True:
# Utilizamos while a principio para que el Bucle exista hasta que el usuario introduzca datos correctos

    #VALIDACION 1 - Momento del día (m/t/n)

    # OJO! SEPARAMOS MOMENTO Y SEXO PARA PODER VALIDARLOS POR SEPARADO, ASÍ EVITAMOS PROBLEMAS DE VALIDACIÓN

    # --- PEDIR MOMENTO ---
    momento = input("Ingrese el momento del día (m/t/n): ").strip().lower()

    # Validar momento (evita vacío, espacios y letras incorrectas)
    if momento not in ["m", "t", "n"]:
        print("Error: momento no válido")
        continue  # vuelve al inicio del while

    # --- PEDIR SEXO ---
    sexo = input("Ingrese el sexo (h/m): ").strip().lower()

    # Validar sexo
    if sexo not in ["h", "m"]:
        print("Error: sexo no válido")
        continue  # vuelve al inicio del while

    # --- IF ANIDADO (AQUI HACEMOS EL SALUDO SEGÚN LOS DATOS) ---
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

    # Si todo es correcto, salir del bucle
    break