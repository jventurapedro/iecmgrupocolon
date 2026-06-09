
import os
import mysql.connector

os.system("cls")

fichero_tabla = "tabla.csv"
fichero_salida = "resultado17.csv"

conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ejercicio17")

cursor = conexion.cursor()

cursor.execute("select * from datos")

# Generamos la tabla en Python y luego la guardamos en un fichero

tabla = list()

for fila in cursor:
    tabla.append(fila)
    
    # Metodo para pasar la tabla a un fichero y mostrarla en el terminal
    
filas = len(tabla)

if filas > 0:
    columnas = len(tabla[0])

    with open("c:/ejemplos/ejercicio_17/tabla.csv", mode="w") as archivo:   

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
                    linea = linea + ("{0:15s}{1}".format(str(tabla[i][j])," | "))
                    
            archivo.write(texto)     # Guardamos la linea en el fichero
                    
            print(linea)             # Imprimimos la linea en el terminal
            
       
            
else:
    
    print("La tabla no tiene registros")
 

cursor.close()                  # Cerramos el canal de conexion con la Base de Datos
conexion.close()                # Cerramos la conexion con la Base de Datos


