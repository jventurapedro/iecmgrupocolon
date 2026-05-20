#    hay que coger los numeros de la base de datos.
#    utilizar el ejercicio.
#    Del ejercicio hacer los calculos, y luego mostrar el resultado.
#     y luego el resultado grabarlo en una tabla.

##15 Tratamiento de fechas en tablas

# EMPEZAMOS POR "os import" para importar la tabla.
import os 

# EL FROM DATETIME IMPORT DATE ES EL CODIDGO PARA TRATAR LAS FECHAS EN PYTHON
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas 
                                                    #   tipo años, meses, minutos y segundos

# DEFINIMOS LA CARPETA Y EL FICHERO
carpeta = "C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio15_tratamiento_de_fechas_en_tablas/"
fichero = "alumnos_fechas.csv"

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

# PRIMERA PARTE DEL EJERCICIO: Para los menores de 18 años, la fecha de baja será dentro de 30 años a partir de su fecha de nacimiento.

for i in range(len(datos)):
    edad = int(datos[i][2])  # Convertir la edad a entero para compararla
    if edad < 18:
        fecha_nacimiento = datetime.strptime(datos[i][6], "%d/%m/%Y")   # Convertir la fecha de nacimiento a un objeto datetime
        fecha_baja = fecha_nacimiento + relativedelta(years=30)  # Calcular la fecha de baja sumando 30 años a la fecha de nacimiento
        datos [i][7] = fecha_baja.strftime("%d/%m/%Y")  # Actualizar la fecha de baja en el array con el nuevo formato
        print(f"El alumno {datos[i][0]} {datos[i][1]} es menor de 18 años, su fecha de baja será: {datos[i][7]}")
        