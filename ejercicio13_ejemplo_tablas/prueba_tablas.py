
            # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo

carpeta = "C:/proyectos/ficheros/"
fichero = "base_coches.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)



                # Para pasar cada línea de un fichero a un array

datos = list()  # Inicializamos el array de destino


        # Método 1 para abrir archivos
        
# archivo = open(carpeta + fichero, mode="r")
               
archivo = open("C:/proyectos/ficheros/base_coches.csv", mode="r")
    
contenido=archivo.readlines()

# Linea 0   = VW\tPolo\t2007\tVerde\t2542HGT\n

 
for linea in contenido:    

    numcamp = linea.count("\t")
    
        # Cuenta cuantos campos hay en cada linea
    
    registro = linea.replace('\n', '')
    
        # Linea 0   = VW\tPolo\t2007\tVerde\t2542HGT
    
    datos.append(registro.split("\t"))
    
        # Linea 0   = VW, Polo, 2007, Verde, 2542HGT
        
archivo.close()






        # Método 2 para abrir archivos
        
datos.clear()      
      

with open(carpeta + "base_coches.csv", mode="r") as archivo:   

    contenido=archivo.readlines()
 
    for linea in contenido:
        numcamp = linea.count("\t")
        registro = linea.replace('\n', '')
        datos.append(registro.split("\t"))



longitud = len(datos)           # Numero de filas
numcamp += 1                    # Numero de columnas con ajuste



for i in range(longitud):       # Podemos dibujar asi el contenido del array
    linea = "\t"
    for j in range(numcamp):
        linea = linea + str(datos[i][j]) + "\t"
    print(linea)


            # Ejemplo de búsqueda: quiero saber cuantos Seat hay en el fichero

cantidad = 0

for i in range(longitud):
    if (datos[i][0]=="Seat"):
        cantidad += 1

print("Hay " + str(cantidad) + " coches Seat en la tabla")

            # Ejemplo de búsqueda: quiero saber cuantos coches hay del 2007

cantidad = 0

for i in range(longitud):
    if (datos[i][2]=="2007"):
        cantidad += 1

print("Hay " + str(cantidad) + " coches matriculados en 2007")
