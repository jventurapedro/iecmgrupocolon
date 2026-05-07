
import os

os.system("cls")

# Inicio del programa

valor = "hOlA mUnDo"

mayus = valor.upper()     # Convierte todos los caracteres de una cadena en mayúsculas

minus = valor.lower()     # Convierte todos los caracteres de una cadena en minúsculas

capital = valor.capitalize()  # Convierte todos los caracteres de una cadena en minúsculas salvo el primero, que lo pone en mayúsculas

todas = valor.title() # Convierte todos los caracteres de una cadena en minúsculas salvo los primeros, que los pone en mayúsculas

print (valor + " " + mayus + " " + minus + " " + capital + " " + todas)

letra = input("Introduce una letra minuscula: ")

letra = letra.lower()

if(letra < "p"): 
    print("La letra es anterior a p")

elif(letra > "p"):
    print("La letra es posterior a p")

else: print("La letra es " + letra)






