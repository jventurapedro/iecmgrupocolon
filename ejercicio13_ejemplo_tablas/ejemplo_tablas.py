
import  os

os.system("cls")


mi_tabla = [['Juan', 'Laura'], [21, 32]]

# Recorriendo los elementos con FOR

print("Recorriendo los elementos con FOR\n")

# Accedemos a cada fila (que es una lista)
for fila in mi_tabla:
    # Accedemos a cada columna dentro de la fila
    for columna in fila:
        print(columna)



# Recorriendo los índices usando WHILE
# i serían las filas
# j serían las columnas

print("\nRecorrienddo con índices con WHILE\n")




for i in range(len(mi_tabla)):
    for j in range(len(mi_tabla[i])):
        print(mi_tabla[i][j])


print(mi_tabla[1][0]) # Imprime el primer elemento de la primera fila

# Con while y los índices

print("\nRecorrienddo con índices con WHILE\n")

fila = 0
while fila < len(mi_tabla):
    columna = 0
    while columna < len(mi_tabla[fila]):
        print(mi_tabla[fila][columna])
        columna += 1        # Equivale a columna = columna + 1
    fila += 1               # Equivale a fila = fila + 1
    
print("\n")

# Dibujando la tabla solamente con los indices


print("Dibujando la tabla con índices con FOR \n")

for fila in range(len(mi_tabla)):
    linea = "|"
    for columna in range(len(mi_tabla[fila])):
        linea = linea + str(mi_tabla[fila][columna]) + "\t"

    print(linea + "|")



print("\n")


print("Dibujo de una tabla en el terminal usando FOR y FORMAT\n")

# Dibujo de una tabla en el terminal usando FOR y FORMAT. Ejemplo:

for x in range(1,11):
    print ('{3}{0:2d}{3} {3}{1:3d}{3} {3}{2:4d}{3}'.format(x, x * x, x * x * x, '|'))

print("\n")

# Dibujo de una tabla en el terminal usando WHILE y FORMAT. Ejemplo:
print("Dibujo de una tabla en el terminal usando WHILE y FORMAT\n")    


x = 1
while (x < 11):
    print ('{3}{0:2d}{3} {3}{1:3d}{3} {3}{2:4d}{3}'.format(x, x * x, x * x * x, '|'))
    x += 1

print("\n")

# Aplicando format a nuestra tabla

print

for fila in range(len(mi_tabla)):
    print ('{3}{0}{3}{1}{3}{2}{3}'.format(mi_tabla[fila][0],'\t',mi_tabla[fila][1], '|'))




