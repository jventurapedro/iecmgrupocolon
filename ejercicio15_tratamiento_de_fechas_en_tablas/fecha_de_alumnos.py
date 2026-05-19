hay que coger los numeros de la base de datos.

utilizar el ejercicio.

Del ejercicio hacer los calculos, y luego mostrar el resultado.

y luego el resultado grabarlo en una tabla.

##15 Tratamiento de fechas en tablas

# EMPEZAMOS POR "os import" para importar la tabla.
import os 
# EL FROM DATETIME IMPORT DATE ES EL CODIDGO PARA TRATAR LAS FECHAS EN PYTHON
from datetime import date                           # Para trabajar con fecha y hora

carpeta = "C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio15_tratamiento_de_fechas_en_tablas/ejercicio15_tratamiento_de_fechas_en_tablas/ejercicio15_tratamiento_de_fechas_en_tablas/"
fichero = "alumnos_fecha.csv"

#AHORA ESCRIBIR LA RUTA
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)    

# PARA LEER EL FICHERO

datos = list()  # Inicializamos el array de destino
archivo = open(ruta, mode="r")
contenido = archivo.readlines()
for linea in contenido:
    numcamp = linea.count(";")
    registro = linea.replace('\n', '')
    registro = registro.replace(",", ".")  # Reemplazar comas por puntos decimales
    datos.append(registro.split(";"))

archivo.close()

for i in range(len(datos)):
    linea = ""
    for j in range(numcamp + 1):  # numcamp es el número de campos, pero necesitamos iterar hasta numcamp + 1 para incluir el último campo
        linea = linea + "{:<15}".format(datos[i][j])
    print(linea + "\n")

    