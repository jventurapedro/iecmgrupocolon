
import os

os.system("cls")


# Creacion de una tabla


mi_tabla = [['Juan', 'Laura'], [21, 32]]

# Recorriendo los elementos

print("Recorriendo los elementos usando FOR\n")

# Accedemos a cada fila (que es una lista)
for fila in mi_tabla:
    print(fila)

print("\n")

# Accedemos a cada fila (que es una lista)
for fila in mi_tabla:
    # Accedemos a cada columna dentro de la fila
    for columna in fila:
        print(columna)
        


# Recorriendo los índices usando FOR
# i serían las filas
# j serían las columnas

print("\nRecorriendo los indices con FOR\n")

filas = len(mi_tabla)
columnas = len(mi_tabla[0])

for i in range(filas):
    for j in range(columnas):
        print(mi_tabla[i][j])



# Con while y los índices

print("\nRecorriendo los indices con WHILE\n")

fila = 0
while fila < filas:
    columna = 0
    while columna < columnas:
        print(mi_tabla[fila][columna])
        columna += 1        # Equivale a columna = columna + 1
    fila += 1               # Equivale a fila = fila + 1
    


# Dibujando la tabla solamente con los indices

print("\nDibujando la tabla usando los indices con FOR\n")

for fila in range(len(mi_tabla)):
    linea = "|"
    for columna in range(len(mi_tabla[fila])):
        linea = linea + str(mi_tabla[fila][columna]) + "\t"

    print(linea + "|")


print("\n")

print("\nEjemplo de dibujo de nuestra tabla usando FOR y FORMAT\n")

# Aplicando format a nuestra tabla

for fila in range(len(mi_tabla)):
    print ('{3}{0}{3}{1}{3}{2}{3}'.format(mi_tabla[fila][0],'\t',mi_tabla[fila][1], '|'))

print("\n")


print("\nEjemplo de dibujo de una tabla en el terminal usando FOR y FORMAT\n")

# Dibujo de una tabla en el terminal usando FOR y FORMAT. Ejemplo:

for x in range(1,11):
    print ('{3}{0:2d}{3} {3}{1:3d}{3} {3}{2:4d}{3}'.format(x, x * x, x * x * x, '|'))

print("\n")


print("\nEjemplo de dibujo de una tabla en el terminal usando WHILE y FORMAT\n")

# Dibujo de una tabla en el terminal usando WHILE y FORMAT. Ejemplo:

x = 1
while (x < 11):
    print ('{3}{0:2d}{3} {3}{1:3d}{3} {3}{2:4d}{3}'.format(x, x * x, x * x * x, '|'))
    x += 1

print("\n")






