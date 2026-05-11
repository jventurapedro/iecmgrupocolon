
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
        linea = linea + "{:<15}".format(datos[i][j])
    print(linea + "\n")


#Aplicando format a nuestra tabla para dibujarla
for i in range(len(datos)):
    linea = ""
    for j in range(numcamp):
        linea = linea + "{:<15}".format(datos[i][j])
    print(linea + "\n")


            # Ejemplo de búsqueda: quiero saber cuantos Seat hay en el fichero

cantidad = 0

print("\n========== EJERCICIO 1 ==========\n")

#AHORA VAMOS A CALCULAR LA EDAD MEDIA DE LOS ALUMNOS
suma = 0
cantidad = 0

for i in range(len(datos)):

    edad = int((datos[i][2]).strip())

    if edad >= 18 and edad <= 65:

        suma += edad
        cantidad += 1

    media = int(suma / cantidad)

print ("La edad media de los alumnos es: ", media)


#AHORA VAMOS A INDICAR POR SEPARADO EL NUMERO DE ALUMNOS DE MADRID, GUADALAJARA Y SORIA

madrid = 0
guadalajara = 0
soria = 0

for i in range(len(datos)):
    provincia = datos[i][4].strip().lower()
    if provincia == "madrid":
        madrid += 1
    elif provincia == "guadalajara":
        guadalajara += 1
    elif provincia == "soria":
        soria += 1

print("Número de alumnos de Madrid: ", madrid)
print("Número de alumnos de Guadalajara: ", guadalajara)
print("Número de alumnos de Soria: ", soria)


print("\n========== EJERCICIO 2 ==========\n")


#Solicitar al operador los siguientes datos:

    #1. Rango de Edad: dos valores numéricos enteros que nos delimiten el rango de edad.
    #2. Provincia: dos provincias en la que buscaremos el rango de edad.

#Solicitar rango de edad:

while True:

    rango_edad = input("Introduce el rango de edad (ejemplo: 18-65 ): ")

    if rango_edad == "":
        print("No se ha introducido un rango de edad válido.")
    elif (rango_edad.count("-") != 1):
        print("El formato del rango de edad no es correcto. Debe contener un guion entre los dos números.")
    else:

        numeros = rango_edad.split("-")

        edad_min = int(numeros[0])

        edad_max = int(numeros[1])

        break


# Solicitar provincias

provincia1 = input("Introduce la primera provincia: ").strip().lower()

provincia2 = input("Introduce la segunda provincia: ").strip().lower()

# Creamos una nueva variable resultado para crear el fichero resultado.csv

resultado = open(carpeta + "resultado.csv", mode="w")


# Utilizamos cantidad para contar los registros encontrados

cantidad = 0

for i in range(len(datos)):
    edad = int((datos[i][2]).strip())
    provincia = datos[i][4].strip().lower()

    if edad >= edad_min and edad <= edad_max:
        if provincia == provincia1 or provincia == provincia2:
            linea = ""

            for j in range(numcamp):
                linea = linea + "{:<15}".format(datos[i][j])
                
            resultado.write(linea + "\n")

            cantidad += 1

resultado.close()

if cantidad == 0:
    print("No hay registro con ese filtro")
else:
    print('Fichero resultado.csv creado correctamente')

print("\nREGISTROS GENERADOS:", cantidad)

archivo = open(carpeta + "resultado.csv", mode="r")

contenido = archivo.readlines()

for linea in contenido:

    print(linea)

archivo.close()