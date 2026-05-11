
            # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo

carpeta = "C:/Users/jpedr/Desktop/iecmgrupocolon/Apuntes 2.0/Python basico/Tablas y ficheros/ficheros/ficheros/"
fichero = "base_coches.csv"


ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)



                # Para pasar cada línea de un fichero a un array

datos = list()  # Inicializamos el array de destino


        # Método 1 para abrir archivos
               
archivo = open("ruta", mode="r")
    
contenido=archivo.readlines()
 
for linea in contenido:    
    numcamp = linea.count("\t")
    registro = linea.replace('\n', '')
    datos.append(registro.split("\t"))

archivo.close()

datos.clear()





        # Método 2 para abrir archivos

with open(carpeta + "base_coches.csv", mode="r") as archivo:   

    contenido=archivo.readlines()
 
    for linea in contenido:
        numcamp = linea.count("\t")
        registro = linea.replace('\n', '')
        datos.append(registro.split("\t"))



longitud = len(contenido)       # Numero de filas
numcamp += 1                    # Numero de columnas con ajuste



for i in range(longitud):       # Podemos dibujar asi el contenido del array
    linea = "\t"
    for j in range(numcamp):
        linea = linea + str(datos[i][j]) + "\t"
    print(linea + "\n")


            # Ejemplo de búsqueda: quiero saber cuantos Seat hay en el fichero

cantidad = 0

for i in range(longitud):
    if (datos[i][0]=="Seat"):
        cantidad += 1

salida1 = ("Hay " + str(cantidad) + " coches Seat en la tabla")

cantidad = 0

for i in range(longitud):
    if (datos[i][2]=="2007"):
        cantidad += 1

salida2 = ("Hay " + str(cantidad) + " coches matriculados en 2007")


        # Modos de apertura de ficheros:
        # 
        #   read        mode="r"    Fichero de solo lectura
        #   create      mode="x"    Creación de nuevo fichero
        #   escritura   mode="w"    Creación y escritura en un fichero
        #   añadir      mode="a"    Añade a un fichero creado

with open(carpeta + "mensajes.txt", mode="w") as mensaje:   

    mensaje.write(salida1)



with open(carpeta + "mensajes.txt", mode="a") as mensaje:   

    mensaje.write("\n" + salida2)



with open(carpeta + "mensajes.txt", mode="a") as mensaje:   

    mensaje.write("\n\n")

    for i in range(longitud):       # Podemos dibujar asi el contenido del array
        
        linea = ""
        
        for j in range(numcamp):
            linea = linea + str(datos[i][j])
            if (j < numcamp):
                linea = linea + "\t"
    
        mensaje.write(linea + "\n")

# Buscar cuantos coches de color azul hay

cantidad = 0 

filas = len(datos)
columnas = len(datos[0])

for i in range(filas):
    if (datos[i][0]=="BMW") and (datos[i][3]=="Azul"):
        cantidad = 1



        if (datos[i][2]=="2007"):
            cantidad += 1