import os

os.system("cls")

edades=[5, 3, 2, 5, 7, 1, 9, 5, 5, 3, 2, 5, 7, 1, 9, 5]

borrar = 8

valores = len(edades) - borrar                       # Le restamos la cantidad de valores a borrar

nuevo=list()

for indice, value in enumerate(edades):

    if indice < valores:
        nuevo.append(value)

print(edades)
print("\n")

edades = nuevo

print(edades)