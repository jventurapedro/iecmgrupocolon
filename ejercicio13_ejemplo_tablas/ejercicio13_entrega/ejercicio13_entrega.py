
# 13 Ejercicio Ejemplos Tablas

            # Para indicar el lugar donde se encuentra el fichero

import os  # Libreria para trabajar con metodos del sistema operativo   

carpeta = "C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio13_ejemplo_tablas/ejercicio13_entrega"
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

