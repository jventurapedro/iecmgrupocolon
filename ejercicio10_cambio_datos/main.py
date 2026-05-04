import os   
os.system("cls")

# Ejercicio 10 - Cambio de datos

#Aqui haremos WHILE
while True:
    nombre = input("Ingrese su nombre: ").strip()

    # Validamos que el nombre no esté vacío ni contenga solo espacios
    if nombre == "":
        print("Error: el nombre no puede estar vacío")
        continue  # vuelve al inicio del while 
    # Si el nombre es correcto, salimos del bucle
    break

# Ahora pedimos la contraseña

while True:
    clave = input("Ingrese su contraseña: ").strip()

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    if len(clave) < 8:
        print("Error: la contraseña debe tener al menos 8 caracteres")
        continue

    for caracter in clave:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        else: 
            print("Error: la contraseña solo puede contener letras y números")
            continue

    if not tiene_mayuscula:
        print("Error: la contraseña debe tener al menos una letra mayúscula")
        continue

    if not tiene_minuscula:
        print("Error: la contraseña debe tener al menos una letra minúscula")
        continue

    if not tiene_numero:
        print("Error: la contraseña debe tener al menos un número")
        continue

    # Si se cumple con todas las condiciones, salimos del bucle
    break

print("Contraseña válida")

ver = input("¿Desea ver su contraseña? (s/n): ").strip().lower()
if ver == "s":
    print(f"Su contraseña es: {clave}")
        