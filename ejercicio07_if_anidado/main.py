#    hay que coger los numeros de la base de datos.
#    utilizar el ejercicio.
#    Del ejercicio hacer los calculos, y luego mostrar el resultado.
#    y luego el resultado grabarlo en una tabla.

##15 Tratamiento de fechas en tablas

# EMPEZAMOS POR "os import" para importar la tabla.
import os 

# EL FROM DATETIME IMPORT DATE ES EL CODIGO PARA TRATAR LAS FECHAS EN PYTHON
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

# DEFINIMOS LA CARPETA Y EL FICHERO
carpeta = "C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio15_tratamiento_de_fechas_en_tablas/"
fichero = "alumnos_fechas.csv"

# AHORA ESCRIBIR LA RUTA
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

# VARIABLE PARA SEPARAR LOS CAMPOS
separador = " | "

# MOSTRAR LA TABLA FORMATEADA
print("\n" + "-" * 180)

for i in range(len(datos)):

    linea = ""

    for j in range(numcamp + 1):

        linea = linea + "{:<20}".format(datos[i][j]) + separador

    print(linea)

print("-" * 180)

# PRIMERA PARTE DEL EJERCICIO:
# Para los menores de 18 años,
# la fecha de baja será dentro de 30 años
# a partir de su fecha de nacimiento.

for i in range(len(datos)):

    edad = int(datos[i][2])

    if edad < 18:

        # Convertir la fecha de nacimiento a datetime
        fecha_nacimiento = datetime.strptime(datos[i][6], "%d/%m/%Y")

        # Sumar 30 años
        fecha_baja = fecha_nacimiento + relativedelta(years=30)

        # Guardar fecha de baja
        datos[i][7] = fecha_baja.strftime("%d/%m/%Y")

        print(
            f"El alumno {datos[i][0]} {datos[i][1]} "
            f"es menor de 18 años, "
            f"su fecha de baja será: {datos[i][7]}"
        )

# SEGUNDA PARTE DEL EJERCICIO:
# Para alumnos entre 18 y 65 años

for i in range(len(datos)):

    edad = int(datos[i][2])

    if 18 <= edad <= 65:

        # Obtener fecha actual
        fecha_hoy = datetime.now()

        # Sumar 10 años
        fecha_baja = fecha_hoy + relativedelta(years=10)

        # Guardar fecha
        datos[i][7] = fecha_baja.strftime("%d/%m/%Y")

        print(
            f"El alumno {datos[i][0]} {datos[i][1]} "
            f"tiene entre 18 y 65 años, "
            f"su fecha de baja será: {datos[i][7]}"
        )

# TERCERA PARTE DEL EJERCICIO:
# Para mayores de 65 años

for i in range(len(datos)):

    edad = int(datos[i][2])

    if edad > 65:

        # Obtener fecha actual
        fecha_hoy = datetime.now()

        # Sumar 5 años
        fecha_baja = fecha_hoy + relativedelta(years=5)

        # Guardar fecha
        datos[i][7] = fecha_baja.strftime("%d/%m/%Y")

        print(
            f"El alumno {datos[i][0]} {datos[i][1]} "
            f"es mayor de 65 años, "
            f"su fecha de baja será: {datos[i][7]}"
        )

# MOSTRAR TABLA FINAL CON FECHAS ACTUALIZADAS

print("\n")
print("=" * 180)
print("TABLA FINAL ACTUALIZADA")
print("=" * 180)

for i in range(len(datos)):

    linea = ""

    for j in range(numcamp + 1):

        linea = linea + "{:<20}".format(datos[i][j]) + separador

    print(linea)

print("=" * 180)