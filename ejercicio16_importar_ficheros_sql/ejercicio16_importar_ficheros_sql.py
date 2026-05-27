# ============================================================================
# LO PRIMERO ES IMPORTAR LA LIBRERÍA NECESARIA PARA LEER LOS FICHEROS SQL
# ============================================================================

import mysql.connector
import os   
import csv
from datetime import datetime

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

    while True:

        dni = input("Introduce el DNI/NIE del alumno: ")

        dni = dni.upper()
    # ============================================================
    # AQUI VAMOS A VALIDAR EL DNI/NIE
    #=============================================================
        if len(dni) != 9:

            print("Documento Incorrecto!")
            continue

    #============================================================
    # COMPROBAR SI ES NIE Y SI LOS 7 DIGITOS DEL MEDIO SON NUMEROS
    #============================================================
        elif dni[0] == "X" or dni[0] == "Y" or dni[0] == "Z":

            if dni[1:8].isdigit() == False:

                print("NIE Incorrecto")
                continue

    #============================================================
    # COMPROBAR DNI Y SI LOS 8 PRIMEROS DIGITOS SON NUMEROS
    #============================================================
        elif dni[0:8].isdigit() == False:

            print("DNI Incorrecto")
            continue

    #============================================================
    # COMPROBAR SI EL DNI/NIE YA EXISTE EN LA BASE DE DATOS
    #============================================================
        sql = "select * from alumnos where dni = %s"

        cursor.execute(sql, (dni,))

        resultado = cursor.fetchone()

        if resultado:

            print("DNI/NIE ya existe. Introduce otro.")
            continue

        else:

            print("Documento correcto")
            break

# ============================================================
# AQUI VAMOS A SOLICITAR LOS DATOS (SECUNDARIOS) DEL ALUMNO
# ============================================================
    while True:
        nombre = input("Introduce el nombre del alumno: ")
# ============================================================
# COMPROBAR SI EL NOMBRE TIENE NUMEROS
# ============================================================
        numero_encontrado = False
        for caracter in nombre:
            if caracter.isdigit() or caracter in ".,;:'@#$%&()!?/":
                numero_encontrado = True
        if numero_encontrado:
            print("El nombre contiene caracteres no permitidos.")
        elif len(nombre) >30:
            print("El nombre no puede tener más de 30 caracteres.")
        else:
            print("Nombre correcto")
            break

# ============================================================
# AQUI VAMOS A SOLICITAR LA EDAD
# ============================================================
    while True:
        edad = input("Introduce la edad: ")

#=============================================================
# COMPROBAR SI LA EDAD CONTIENE SOLO NUMEROS
# ============================================================
        if edad.isdigit() == False:
            print ("La edad solo puede contener números.")

        elif int(edad) < 1 or int(edad) > 121:
            print ("La edad debe estar entre 1 y 121 años.")

        else: 
            print ("Edad correcta")
            break

# ============================================================
# AQUI VAMOS A SOLICITAR EL NOMBRE DE LA CALLE
# ============================================================
    while True:
        nombre_calle = input("Introduce el nombre de la calle: ")
        caracter_incorrecto = False

# ============================================================
# COMPROBAR SI EL NOMBRE DE LA CALLE CONTIENE NUMEROS
# O CARACTERES ESPECIALES
# ============================================================
        for caracter in nombre_calle:
            if caracter.isdigit() or caracter in ".,;:'@#$%&()!?/":
                caracter_incorrecto = True

        if caracter_incorrecto:
            print("La calle contine caracteres no permitidos.")

        else:
            print("Nombre de la calle correcto")
            break

# ============================================================
# AQUI VAMOS A SOLICITAR EL NUMERO DE LA CALLE
# ============================================================
    while True:
        numero_calle = input("Introduce el número de la calle: ")

#=============================================================
# COMPROBAR SI EL NUMERO DE LA CALLE CONTIENE SOLO NUMEROS
# ============================================================
        if " " in numero_calle:
            print("El número de la calle no puede contener espacios.")
    
        elif numero_calle.isdigit() == False:
            print("El número de la calle solo puede contener números.")

        elif len(numero_calle) > 6:
            print("El número de la calle no puede superar 6 números.")

        else:
            print("Número de la calle correcto")
            break

#=============================================================
# AQUI VAMOS A SOLICITAR LA PROVINCIA
#=============================================================
    while True:
        provincia = input("Introduce la provincia: ")
        caracter_incorrecto = False
        for caracter in provincia:
            if caracter.isdigit() or caracter in ".,;:'@#$%&()!?/":
                caracter_incorrecto = True

        if caracter_incorrecto:
            print("La provincia contine caracteres no permitidos.")
        elif len(provincia) > 30:
            print("La provincia no puede superar 30 caracteres.")
        else:
            print("Provincia correcta")
            break

#=============================================================
# AQUI VAMOS A SOLICITAR EL TELEFONO
#=============================================================
    while True:
        telefono = input("Introduce el teléfono: ")

#=============================================================
# COMPROBAR SI EL TELEFONO CONTIENE SOLO NUMEROS
# ============================================================
        if telefono.isdigit() == False:
            print("El teléfono solo puede contener números.")
        elif len(telefono) != 9:
            print("El teléfono debe contener exactamente 9 dígitos.")
        else:
            print("Teléfono correcto")
            break


#=============================================================
# AQUI VAMOS A SOLICITAR FECHA DE NACIMIENTO
#=============================================================
    while True:
        fecha_nacimiento = input("Introduce la fecha de nacimiento (dd-mm-yyyy): ")
        if len(fecha_nacimiento) != 10:
            print("La fecha de nacimiento debe tener el formato dd-mm-yyyy.")
        else:
            dia = fecha_nacimiento[0:2]
            mes = fecha_nacimiento[3:5]
            año = fecha_nacimiento[6:10]


            if dia.isdigit() == False or mes.isdigit() == False or año.isdigit() == False:

                print("La fecha solo puede contener números y guiones(-).")

            elif int(año) < 1900 or int(año) > datetime.now().year:

                print("El año debe estar entre 1900 y la fecha actual.")

            else:

                print("Fecha de nacimiento correcta")
                break

#=============================================================
# GENERAR FECHA DE ALTA
#=============================================================
    fecha_alta = datetime.now().strftime("%d-%m-%Y")

#=============================================================
# MOSTRAR RESUMEN DE LOS DATOS INTRODUCIDOS
#=============================================================
    print()
    print("CONFIRME LOS DATOS INTRODUCIDOS")
    print()

    print("DNI/NIE:", dni)
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Calle:", nombre_calle)
    print("Número:", numero_calle)
    print("Provincia:", provincia)
    print("Teléfono:", telefono)
    print("Fecha nacimiento:", fecha_nacimiento)
    print("Fecha alta:", fecha_alta)

    print()

    confirmacion = input("¿Desea completar el alta? (S/N): ")

#=============================================================
# COMPROBAR LA CONFIRMACION
#=============================================================
    if confirmacion.upper() == "S":

        sql = """INSERT INTO alumnos (dni, nombre, edad, direccion, provincia, telefono, fecha_nacimiento, fecha_alta)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        valores = (
            dni,
            nombre,
            edad,
            nombre_calle + " " + numero_calle,
            provincia,
            telefono,
            fecha_nacimiento,
            fecha_alta
            )

        cursor.execute(sql, valores)

        conexion.commit()

        print("Alumno insertado correctamente")

        break

# ============================================================
# SOLICITAR RANGO DE EDAD Y PROVINCIAS
# ============================================================

    edad_minima = int(input("Introduce la edad mínima: "))
    edad_maxima = int(input("Introduce la edad máxima: "))

    provincia1 = input("Introduce la primera provincia: ")
    provincia2 = input("Introduce la segunda provincia: ")

    else:  
    print("Reiniciando introducción de datos...")

    continue