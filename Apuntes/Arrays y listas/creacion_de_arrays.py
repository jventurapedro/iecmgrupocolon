                
                # Generador automático de numeros enteros

import random
numero = random.randint(1, 20)                   


                    # Uso de Arrays o listas en Python

# Creación de una lista o Array vacío

edades = []         # Opcion 1

edades = list()     # Opcion 2

# Llenado de datos en un Array

edades = [20, 41, 6, 18, 23]            # Opcion 1

edades = list([20, 41, 6, 18, 23])      # Opcion 2

# Recorriendo los elementos directamente con FOR

for indice in edades:
    print(indice)

print("\n")

# Recorriendo los índices con FOR. Ejemplo en horizontal.

lista = ""

for indice in range(len(edades)):
    lista = lista + str(edades[indice]) + " "

print(lista + "\n")

# Recorriendo los índices con WHILE. Ejemplo en vertical

indice = 0

while indice < len(edades):
    print(edades[indice])
    indice = indice + 1 

print("\n")

# Añadir elementos a un Array

edades.append(10)
edades.append(5)
edades.append(18)

# Impresión directa del contenido del Array

print(edades)       # Mostrará 20, 41, 6, 18, 23, 10, 5, 18
print("\n")

# Quitar elementos de un Array. Con REMOVE se elimina la primera
#       coinciencia que encuentre. Para ir eliminando mas de un valor
#       hay que repetir el proceso hasta que no quede ningún número

edades.remove(18)

print(edades)       # Mostrará 20, 41, 6, 23, 10, 5, 18
print("\n")

# Quitar todos las coincidencias de una array. Con REMOVE se elimina la primera
#       coinciencia que encuentre. Para ir eliminando mas de un valor
#       hay que repetir el proceso, por ejemplo con While, hasta que no quede ningún número

control = False
while control == False:

    control = True

    if (18 in edades):
        edades.remove(18)
        control = False
        
print(edades)       # Mostrará 20, 41, 6, 23, 10, 5
print("\n")

# Sustituir elementos de un Array. Se puede hacer por sustitución
#       directa, marcando el indice del valor a modificar y dándole
#       otro valor.


print(edades)       # Mostrará 20, 41, 6, 23, 10, 5, 18

edades[2] = 10

print(edades)       # Mostrará 20, 41, 10, 23, 10, 5, 18
print("\n")


# Otra forma de hacerlo es mediante un FOR, buscando el elemento a sustituir
#       y cambiándolo por el valor nuevo. Este método permite modificar más 
#       de una posición


print(edades)       # Mostrará 20, 41, 10, 23, 10, 5, 18

for index, value in enumerate(edades):
    if (value == 10):           # También if(edades[index == 10]):
        edades[index] = 125

print(edades)       # Mostrará 20, 41, 125, 23, 125, 5, 18
print("\n")

