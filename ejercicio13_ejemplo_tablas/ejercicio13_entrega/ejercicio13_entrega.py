
# 13 Ejercicio Ejemplos Tablas

            # Para indicar el lugar donde se encuentra el fichero

import os  # Libreria para trabajar con metodos del sistema operativo   

carpeta = "C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio13_ejemplo_tablas/ejercicio13_entrega/"
fichero = "alumnos.txt"


ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)    

datos = list()  # Inicializamos el array de destino

        # Método 1 para abrir archivos      
archivo = open(ruta, mode="r")

contenido = archivo.readlines()
for linea in contenido:
    numcamp = linea.count("\t")
    registro = linea.replace('\n', '')
    datos.append(registro.split("\t"))


archivo.close()

for i in range(len(datos)):       # Podemos dibujar asi el contenido del array
    linea = "\t"
    for j in range(numcamp):
        linea = linea + str(datos[i][j]) + "\t"
    print(linea + "\n")


#Aplicando format a nuestra tabla para dibujarla
for i in range(len(datos)):
    linea = ""
    for j in range(numcamp):
        linea = linea + "{:<15}".format(datos[i][j])
    print(linea + "\n")


            # Ejemplo de búsqueda: quiero saber cuantos Seat hay en el fichero

cantidad = 0

#AHORA VAMOS A CALCULAR LA EDAD MEDIA DE LOS ALUMNOS
suma = 0
cantidad = 0

for i in range(len(datos)):

    edad = int((datos[i][2]).strip())

    if edad >= 18 and edad <= 65:

        suma += edad
        cantidad += 1

    media = suma / cantidad

print ("La edad media de los alumnos es: ", media)


#AHORA VAMOS A INDICAR POR SEPARADO EL NUMERO DE ALUMNOS DE MADRID, GUADALAJARA Y SORIA

madrid = 0
guadalajara = 0
soria = 0

for i in range(len(datos)):
    provincia = datos[i][4].strip()
    if provincia == "Madrid":
        madrid += 1
    elif provincia == "Guadalajara":
        guadalajara += 1
    elif provincia == "Soria":
        soria += 1

print("Número de alumnos de Madrid: ", madrid)
print("Número de alumnos de Guadalajara: ", guadalajara)
print("Número de alumnos de Soria: ", soria)

#Solicitar al operador los siguientes datos:

    #1. Rango de Edad: dos valores numéricos enteros que nos delimiten el rango de edad.
    #2. Provincia: dos provincias en la que buscaremos el rango de edad.

#Solicitar rango de edad:
rango_edad = int(input("Introduce el rango de edad (ejemplo: 18-65): "))
while True:
    if rango_edad == "":
        print("No se ha introducido un rango de edad válido.")
    elif (rango_edad.isdigit() == False):
        print("El rango de edad debe ser un número.")
    else:
        rango_edad = int(rango_edad)
        break

provincia1 = input("Introduce la primera provincia: ")


provincia2 = input("Introduce la segunda provincia: ")
