from os import system
system("cls")

import numpy as np


antiguo = list([1, 3, 5, 7, 9, 2, 4, 6, 8])       # Dataframe, no se puede modificar

# antiguo[0] = 20   Esto no se puede hacer, da error de ejecucion

# Creacion de un Array con NumPy



nuevo2 =np.array(antiguo)








nuevo = np.array([1, 3, 5, 7, 9, 2, 4, 6, 8])   # Array, si se puede modificar

nuevo[0] = 20

print(nuevo)

# Creacion de una tabla con NumPy

tabla = np.array([[1, 3, 5], [7, 9, 2], [4, 6, 8], [10, 12, 9]])

print (tabla)

# Para obtener el numero de columnas de una tabla

columnas = len(tabla[0])

# Para obtener el numero de filas de una tabla

filas = len(tabla)

# Para imprimir los valores de la tabla usando tabulaciones

for i in range(filas):
    linea=""
    for j in range(columnas):
        linea = linea + str(tabla[i][j]) + "\t"
    print (linea + "\n")

