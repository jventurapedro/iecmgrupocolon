import os 
os.system("cls")

nombre = input("Introduce tu nombre: ")
clave = input("Introduce una contraseña de 8 caracteres (con al menos una mayúscula, una minúscula y un número)")

control = False
while control == False:
    
    control = True

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    if nombre == "":
        print("El nombre no puede estar vacío")
        control = False
        

    if len(clave) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        control = False

        for c in clave:
            if c.isupper():
                tiene_mayuscula = True
            elif c.islower():
                tiene_minuscula = True
            elif c.isdigit():
                tiene_numero = True

        if not tiene_mayuscula:
            print("La contraseña debe contener al menos una letra mayúscula")
            control = False
        if not tiene_minuscula:
            print("La contraseña debe contener al menos una letra minúscula")
            control = False
        if not tiene_numero:
            print("La contraseña debe contener al menos un número")
            control = False

        if control == False:
            clave = input("\nIntroduce una contraseña de 8 caracteres (con al menos una mayúscula, una minúscula y un número)")

print("\n¡Registro exitoso! Bienvenido, " + nombre + ".")
