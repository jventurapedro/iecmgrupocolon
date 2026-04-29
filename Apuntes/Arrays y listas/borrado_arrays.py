
edades=[5, 3, 2, 5, 7, 1, 9, 5, 5, 3, 2, 5, 7, 1, 9, 5]

valores = 5                       # Cantidad de valores a borrar

nuevo=list()

contador = 0

for indice, value in enumerate(edades):
    
    if (value != valores):
        nuevo.append(value)
    else:
        contador+=1             # Equivale a contador = contador + 1
        if (contador < 3):
            nuevo.append(value)


print(edades)
print("\n")

edades = nuevo

print(edades)