# ============================================================================
# LO PRIMERO ES IMPORTAR LA LIBRERÍA NECESARIA PARA LEER LOS FICHEROS SQL
# ============================================================================

import mysql.connector
import os   
import csv

os.system('cls')  # LIMPIA LA PANTALLA

# ============================================================
# AQUI VAMOS CONECTAR CON EL XAMP Y CREAR LA BASE DE DATOS
# ============================================================

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alumnosdb"
)

cursor = conexion.cursor()

# ============================================================
# AQUI VAMOS A SOLICITAR EL DNI
# ============================================================
while True:
    dni = input("Introduce el DNI del alumno: ")

# ============================================================
# AQUI VAMOS A VALIDAR SI EL DNI YA EXISTE
# ============================================================

    sql = "select * from alumnos where dni = %s"

    cursor.execute(sql, (dni,))

    resultado = cursor.fetchone()

    if resultado:

        print("ERROR - DNI repetido")

# ============================================================
# AQUI VAMOS A SOLICITAR LOS DATOS
# ============================================================

    else:

        nombre = input("Introduce el nombre del alumno: ")

        telefono = input("Introduce el teléfono del alumno: ")

# ============================================================
# AQUI VAMOS A VALIDAR EL TAMAÑO DEL NOMBRE
# ============================================================

        if len(nombre) > 30:

            print("El nombre no puede tener más de 30 caracteres.")

# ============================================================
# AQUI VAMOS A VALIDAR EL FORMATO DEL TELEFONO 
# ============================================================

        elif len(telefono) != 9:

            print("El teléfono debe tener 9 dígitos.")

# ============================================================
# AQUI VAMOS INSERTAR ALUMNO EN LA BASE DE DATOS
# ============================================================

        else:

            sql = "INSERT INTO alumnos (dni, nombre, telefono) VALUES (%s, %s, %s)"

            valores = (dni, nombre, telefono)

            cursor.execute(sql, valores)

            conexion.commit()

            print("Alumno insertado correctamente")

            break

# ============================================================
# EN ESTE BLOQUE:
# Rango de Edad: dos valores numéricos enteros que nos delimiten el rango de edad.
# Provincia: dos provincias en la que buscaremos el rango de edad.
# ============================================================

# SOLICITAMOS LOS DATOS PARA EL RANGO DE EDAD Y LAS PROVINCIAS

edad_minima = int(input("Introduce la edad mínima: "))
edad_maxima = int(input("Introduce la edad máxima: "))
provincia1 = input("Introduce la primera provincia: ")
provincia2 = input("Introduce la segunda provincia: ")

# AQUI VAMOS HACER EL SELECT

sql = """ select * from alumnos where edad between %s and %s and (provincia = %s or provincia = %s) """

valor = (edad_minima, edad_maxima, provincia1, provincia2)
cursor.execute(sql, valor)
resultado = cursor.fetchall()

# AQUI VAMOS A MOSTRAR LOS RESULTADOS

if resultado: 
    fichero = open(r"C:\Users\jpedr\Desktop\iecmgrupocolon\ejercicio16_importar_ficheros_sql\resultado16.csv", "w", newline="")
    escribir = csv.writer(fichero, delimiter=";")
    for fila in resultado:
        escribir.writerow(fila)
    fichero.close()

    print()

    print("HEMOS ENCONTRADO ESTOS USUARIOS:")

    print()

    for fila in resultado:

        print("DNI:", fila[0], "- Nombre:", fila[1], "- Edad:", fila[2])

    print()

    print("Consulte el archivo resultado16.csv para ver todos los resultados")

else:

    print("No hay registro con ese filtro")
   
#============================================================
# COPIA DE SEGURIDAD
#============================================================

os.chdir(r"C:\Users\jpedr\Desktop\iecmgrupocolon\ejercicio16_importar_ficheros_sql")

os.system(
    r'"C:\xampp\mysql\bin\mysqldump.exe" -u root alumnosdb > alumnosdb.sql'
)

print("Copia de seguridad realizada")


cursor.close()
conexion.close()