import os
os.system("cls")

import random

numero = []

while len(numero) < 10:
    n = random.randint(-100, 100)
    if n != 0 and n not in numero:
        numero.append(n)

mayor = numero[0]
menor = numero[0]

forn n 