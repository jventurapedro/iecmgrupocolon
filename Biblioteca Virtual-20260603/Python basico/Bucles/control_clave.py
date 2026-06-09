import os
os.system("cls")

usuario = input("Introduce un nombre de usuario: ")
numero = len(usuario)

# Controlamos que el usuario no este vacio

while (usuario == "") or (numero == 0):
    print("\nNo has escrito un nombre valido")
    usuario = input("Introduce un nombre de usuario: ")
    numero = len(usuario)
    

clave = input("Introduce una contraseña (minimo 8 caracteres, con mayusculas, minusculas y numeros): ")
numero = len(clave)

# Controlamos que tenga al minimo 8 caracteres

control = False

while (control == False):

    control = True

    print("\nIntroduce una contraseña: ")
    clave = input("Introduce una contraseña (minimo 8 caracteres, con mayusculas, minusculas y numeros): ")
    numero = len(clave)

    if (numero < 8):
        control = False

    mayusculas = [char for char in clave if char.isupper()]     # pePitoGrillO  -->  mayusculas [P,G,O]
    cuantas = len(mayusculas)

    if (cuantas == 0):
        control = False

    minusculas = [char for char in clave if char.islower()]     # pePitoGrillO  -->  minusculas [p,e,i,t,o,r,i,l,l]
    cuantasmin = len(minusculas)

    if (cuantasmin == 0):
        control = False

    minimo = min(clave)             # pepitogrillo

    if (minimo >= "0") and (minimo <= "9"):
        control = False






# Calculamos el valor mínimo y máximo para determinar si hay números y minúsculas

minimo = min(clave)             # pepitogrillo
maximo = max(clave)

# Método opcional para buscar minúsculas

minusculas = [char for char in clave if char.islower()]     # pePitoGrillO  -->  minusculas [p,e,i,t,o,r,i,l,l]
cuantasmin = len(minusculas)

print("\n")

if (minimo >= "0") and (minimo <= "9"):
    print("Has escrito al menos un numero")
else:
    print("No has escrito ningun un numero")


if (maximo >= "a") and (maximo <= "z"):
    print("Has escrito al menos una letra minúscula")
else:
    print("No has escrito ninguna letra minúscula")


# Buscamos caracter por caracter si hay mayúsculas o no en la cadena

mayusculas = [char for char in clave if char.isupper()]     # pePitoGrillO  -->  mayusculas [P,G,O]
cuantas = len(mayusculas)

print("\nUsuario correcto. Tu usuario es: " + usuario)
print("Contraseña correcta. Tu clave es: " + clave + " y tiene " + str(cuantas) + " mayusculas")