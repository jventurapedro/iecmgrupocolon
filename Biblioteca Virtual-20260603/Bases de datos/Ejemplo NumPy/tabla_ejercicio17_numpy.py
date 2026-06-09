
import os
import mysql.connector

import numpy as np

os.system("cls")

fichero_tabla = "ejercicio17.csv"
fichero_salida = "ejercicio17.csv"

ruta_base = "C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio17_datos_servidor_remoto/ENCLASE/soluciones_professor/"

conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ejercicio17")

cursor = conexion.cursor()

cursor.execute("select * from datos")

# Generamos la tabla en Python guardada en la memoria RAM y luego la guardamos en un fichero



tabla = list()                  # Ejemplo de Dataframe de Python

nueva_tabla = np.array(tabla)   # Ejemplo de Array de NumPy

tabla_fichero = np.loadtxt(ruta_base + fichero_tabla, skiprows=1, dtype=str, delimiter=";")


for fila in cursor:
    tabla.append(fila)
    
    # Metodo para pasar la tabla a un fichero y mostrarla en el terminal
    
filas = len(tabla)

if filas > 0:
    columnas = len(tabla[0])

    with open(ruta_base + fichero_tabla, mode="w") as archivo:   

        for i in range(filas):
            linea = ""
            texto = ""
            for j in range(columnas):
                
                
                if (j == 5):
                    texto = texto + str(tabla[i][j]) + "\n"
                else:
                    texto = texto + str(tabla[i][j]) + ";"
    
                
                if (j == 1) or (j == 2):
                    linea = linea + ("{0:25s}{1}".format(str(tabla[i][j])," | "))    
                else:
                    linea = linea + ("{0:12s}{1}".format(str(tabla[i][j])," | "))
                    
                   
                    
            archivo.write(texto)     # Guardamos la linea en el fichero
                    
            print(linea)             # Imprimimos la linea en el terminal
            
       
            
else:
    
    print("La tabla no tiene registros")
 

cursor.close()                  # Cerramos el canal de comunicacion con la Base de Datos
conexion.close()                # Cerramos la conexion con la Base de Datos


