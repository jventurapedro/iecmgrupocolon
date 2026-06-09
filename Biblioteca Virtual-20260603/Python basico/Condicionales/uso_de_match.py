
import os
os.system("cls")

numero = input("Introduce 0 o 1: ")
numero = int(numero)

if(numero == 0):

    print("Has introducido un 0")

elif(numero == 1):


    print("Has introducido un 1")

else:

    print("No has introducido ni 0 ni 1")



match(numero):

    case 0:
        print("Has introducido un 0")

    case 1:
        print("Has introducido un 1")

    case _:
        print("No has introducido ni 0 ni 1")


