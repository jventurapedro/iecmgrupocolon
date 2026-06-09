import os

os.system("cls")


# Bucles son parte del código que se repite N veces

# Indeterminados: son aquellos que se ejecutan un numero variable de veces. 
# Se crean con While.

# Determinados: son aquellos que se ejecutan un numero fijo de veces. 
# Se crean con For.


# Estructura básica FOR:    for (i=0; i<=5; i++)
#                               {
#                                  alert(i);
#                                }

mensaje = ""

for i in range(11):
    mensaje = mensaje + str(i) + " "

print(mensaje)


mensaje = ""

numeros = int(input("\n\nCuantos números pares quieres sacar: "))

for i in range(numeros):
    mensaje = mensaje + str((i+1)*2) + " "

print(mensaje)