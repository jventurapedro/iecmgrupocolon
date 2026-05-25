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

#                 MOSTRAR TABLA FORMATEADA

for i in range(len(datos)):
    linea = ""
    for j in range(numcamp + 1):  # numcamp es el número de campos, pero necesitamos iterar hasta numcamp + 1 para incluir el último campo
        linea = linea + "{:<20}".format(datos[i][j])
    print(linea + "\n")

#      ALUMNOS MENORES DE 18 AÑOS

print("############################################################")
print("      ALUMNOS MENORES DE 18 AÑOS")
print("############################################################")

# PRIMERA PARTE DEL EJERCICIO: Para los menores de 18 años, la fecha de baja será dentro de 30 años a partir de su fecha de nacimiento.

for i in range(len(datos)):
    edad = int(datos[i][2])  # Convertir la edad a entero para compararla

    if edad < 18:
        fecha_nacimiento = datetime.strptime(datos[i][6], "%d/%m/%Y")   # Convertir la fecha de nacimiento a un objeto datetime
        fecha_baja = fecha_nacimiento + relativedelta(years=30)  # Calcular la fecha de baja sumando 30 años a la fecha de nacimiento
        datos [i][7] = fecha_baja.strftime("%d/%m/%Y")  # Actualizar la fecha de baja en el array con el nuevo formato

        print("------------------------------------------------------------")
        print(f"DNI / ID     : {datos[i][0]}")
        print(f"Nombre       : {datos[i][1]}")
        print(f"Edad         : {datos[i][2]}")
        print(f"Fecha Baja   : {datos[i][7]}")
        print("------------------------------------------------------------")


#      ALUMNOS ENTRE 18 Y 65 AÑOS
#

print("############################################################")
print("      ALUMNOS ENTRE 18 Y 65 AÑOS")
print("############################################################")

# SEGUNDA PARTE DEL EJERCICIO: Para los alumnos de entre 18 y 65 años (incluyendo 18 y 65), la fecha de baja será dentro de 10 años a partir de la fecha de hoy.

for i in range(len(datos)):
    edad = int(datos[i][2])  # Convertir la edad a entero para compararla

    if 18 <= edad <= 65:
        fecha_hoy = datetime.now()  # Obtener la fecha actual
        fecha_baja = fecha_hoy + relativedelta(years=10)  # Calcular la fecha de baja sumando 10 años a la fecha actual
        datos [i][7] = fecha_baja.strftime("%d/%m/%Y")

        print("------------------------------------------------------------")
        print(f"DNI / ID     : {datos[i][0]}")
        print(f"Nombre       : {datos[i][1]}")
        print(f"Edad         : {datos[i][2]}")
        print(f"Fecha Baja   : {datos[i][7]}")
        print("------------------------------------------------------------")


#      ALUMNOS MAYORES DE 65 AÑOS

print("############################################################")
print("      ALUMNOS MAYORES DE 65 AÑOS")
print("############################################################")

for i in range(len(datos)):
    edad = int(datos[i][2])  # Convertir la edad a entero para compararla

    if edad > 65:
        fecha_hoy = datetime.now()  # Obtener la fecha actual
        fecha_baja = fecha_hoy + relativedelta(years=5)  # Calcular la fecha de baja sumando 5 años a la fecha actual
        datos [i][7] = fecha_baja.strftime("%d/%m/%Y")

        print("------------------------------------------------------------")
        print(f"DNI / ID     : {datos[i][0]}")
        print(f"Nombre       : {datos[i][1]}")
        print(f"Edad         : {datos[i][2]}")
        print(f"Fecha Baja   : {datos[i][7]}")
        print("------------------------------------------------------------")

# ============================================================
#      GUARDAR LOS RESULTADOS EN resultados15.csv
# ============================================================

fichero_resultado = "resultados15.csv"

ruta_resultado = os.path.join(carpeta, fichero_resultado)
ruta_resultado = os.path.abspath(ruta_resultado)

archivo_resultado = open(ruta_resultado, mode="w")

for i in range(len(datos)):
    linea = ""

    for j in range(numcamp + 1):
        linea = linea + datos[i][j]

        if j < numcamp:
            linea = linea + ";"

    archivo_resultado.write(linea + "\n")

archivo_resultado.close()

print("############################################################")
print("      TABLA GUARDADA EN resultados15.csv")
print("############################################################")