#Ejercicio 08 - Pizzeria

import os
os.system("cls")

#Listas

vegetariana = ["pimiento", "aceitunas", "cebolla", "tofu"]
no_vegetariana = ["pepperoni", "jamon", "bacon", "atun"]

#Solicitar tipo

tipo = input("Quieres pizza vegetariana (si/no): ")
tipo = tipo.lower()

#Calculo

if(tipo == "si"):

    print("Ingredientes: pimiento, aceitunas, cebolla, tofu")

    ing1 = input("Elige primer ingrediente: ")
    ing1 = ing1.lower()

    if(ing1 in vegetariana):

        ing2 = input("Elige segundo ingrediente: ")
        ing2 = ing2.lower()

        if(ing2 in vegetariana and ing2 != ing1):
            print("Pizza vegetariana con mozzarella, tomate, " + ing1 + " y " + ing2)
        else:
            print("Error: ingrediente no valido o repetido")

    else:
        print("Error: ingrediente no valido")

else:

    print("Ingredientes: pepperoni, jamon, bacon, atun")

    ing1 = input("Elige primer ingrediente: ")
    ing1 = ing1.lower()

    if(ing1 in no_vegetariana):

        ing2 = input("Elige segundo ingrediente: ")
        ing2 = ing2.lower()

        if(ing2 in no_vegetariana and ing2 != ing1):
            print("Pizza no vegetariana con mozzarella, tomate, " + ing1 + " y " + ing2)
        else:
            print("Error: ingrediente no valido")

    else:
        print("Error: ingrediente no valido")