
            # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo

os.system("cls")

import random



linea = []

while len(linea) < 10:

    numero = random.randint(-100, 100)

    if (numero !=0) and (numero not in linea):
        
        linea.append(numero)
















