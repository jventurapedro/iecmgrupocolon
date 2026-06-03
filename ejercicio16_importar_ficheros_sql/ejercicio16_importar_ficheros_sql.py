# ============================================================================
# LO PRIMERO ES IMPORTAR LA LIBRERÍA NECESARIA PARA LEER LOS FICHEROS SQL
# ============================================================================

import mysql.connector
import os   
import csv
import subprocess
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
# RUTA PARA BACKUPS
# ============================================================

ruta_backup = r"C:\Users\jpedr\Desktop\iecmgrupocolon\ejercicio16_importar_ficheros_sql"

# ============================================================
# MENU PRINCIPAL
# ============================================================

while True:

    print()
    print("====================================")
    print("MENU PRINCIPAL")
    print("====================================")
    print()
    print("1. Dar de alta alumno")
    print("2. Buscar alumnos por edad y provincia")
    print("3. Salir")
    print()

    opcion = input("Seleccione una opción: ")
# ============================================================
## OPCION 1 - DAR DE ALTA ALUMNO
# ============================================================

    if opcion == "1":
    
# ============================================================
# AQUI VAMOS A SOLICITAR EL DNI
# ============================================================

        
        while True:

            dni = input("Introduce el DNI/NIE del alumno: ")

            dni = dni.upper()
        # ============================================================
        # AQUIA VAMOS A VALIDAR EL DNI/NIE
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
                break

    # ============================================================
    # AQUI VAMOS A SOLICITAR LA EDAD (OPCIONAL)
    # ============================================================
        while True:
            edad = input("Introduce la edad (opcional, presiona Enter para omitir): ")

            if edad == "":
                edad = None
                break

            elif edad.isdigit() == False:
                print ("La edad solo puede contener números.")

            elif int(edad) < 1 or int(edad) > 121:
                print ("La edad debe estar entre 1 y 121 años.")

            else: 
                break

    # ============================================================
    # AQUI VAMOS A SOLICITAR EL NOMBRE DE LA CALLE (OPCIONAL)
    # ============================================================
        while True:
            nombre_calle = input("Introduce el nombre de la calle (opcional, presiona Enter para omitir): ")
            caracter_incorrecto = False

            if nombre_calle == "":
                nombre_calle = None
                break

    # ============================================================
    # COMPROBAR SI EL NOMBRE DE LA CALLE CONTIENE NUMEROS
    # O CARACTERES ESPECIALES
    # ============================================================
            for caracter in nombre_calle:
                if caracter.isdigit() or caracter in ".,;:'@#$%&()!?/":
                    caracter_incorrecto = True

            if caracter_incorrecto:
                print("La calle contiene caracteres no permitidos.")

            else:
                break

    # ============================================================
    # AQUI VAMOS A SOLICITAR EL NUMERO DE LA CALLE (OPCIONAL)
    # ============================================================
        while True:
            numero_calle = input("Introduce el número de la calle (opcional, presiona Enter para omitir): ")

            if numero_calle == "":
                numero_calle = None
                break

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
                break

    #=============================================================
    # AQUI VAMOS A SOLICITAR LA PROVINCIA (OPCIONAL)
    #=============================================================
        while True:
            provincia = input("Introduce la provincia (opcional, presiona Enter para omitir): ")
            caracter_incorrecto = False
            
            if provincia == "":
                provincia = None
                break
            
            for caracter in provincia:
                if caracter.isdigit() or caracter in ".,;:'@#$%&()!?/":
                    caracter_incorrecto = True

            if caracter_incorrecto:
                print("La provincia contiene caracteres no permitidos.")
            elif len(provincia) > 30:
                print("La provincia no puede superar 30 caracteres.")
            else:
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
                break


    #=============================================================
    # AQUI VAMOS A SOLICITAR FECHA DE NACIMIENTO (OPCIONAL)
    #=============================================================
        while True:
            fecha_nacimiento = input("Introduce la fecha de nacimiento (opcional, dd-mm-yyyy, presiona Enter para omitir): ")
            
            if fecha_nacimiento == "":
                fecha_nacimiento = None
                break
            
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

                    break

    #=============================================================
    # GENERAR FECHA DE ALTA
    #=============================================================
        fecha_alta = datetime.now().strftime("%d-%m-%Y")

    #=============================================================
    # CONSTRUIR DIRECCION
    #=============================================================
        if nombre_calle and numero_calle:
            direccion = nombre_calle + " " + numero_calle
        elif nombre_calle:
            direccion = nombre_calle
        elif numero_calle:
            direccion = numero_calle
        else:
            direccion = None

    #=============================================================
    # MOSTRAR RESUMEN DE LOS DATOS INTRODUCIDOS
    #=============================================================
        print()
        print("CONFIRME LOS DATOS INTRODUCIDOS")
        print()

        print("DNI/NIE:", dni)
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("Dirección:", direccion)
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
                direccion,
                provincia,
                telefono,
                fecha_nacimiento,
                fecha_alta
                )

            cursor.execute(sql, valores)

            conexion.commit()

            print()
            print("Alumno insertado correctamente")

    #=============================================================
    # REALIZAR COPIA DE SEGURIDAD AUTOMATICA
    #=============================================================
            fecha_backup = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            nombre_archivo = "backup_" + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".sql"
            
            comando = "mysqldump -u root alumnosdb > \"" + ruta_backup + "\\" + nombre_archivo + "\""
            
            resultado = os.system(comando)
            
            if resultado == 0:
                
    #=============================================================
    # GUARDAR FECHA DE LA ULTIMA COPIA
    #=============================================================
                archivo_fecha = open(ruta_backup + "\\ultima_copia.txt", "w")
                archivo_fecha.write(fecha_backup)
                archivo_fecha.close()
                
                print("Copia de seguridad actualizada")
            
            print()

            while True:
                opcion_despues = input("¿Desea volver al menú principal (M) o salir (S)? ")
                
                if opcion_despues.upper() == "M":
                    break
                elif opcion_despues.upper() == "S":
                    cursor.close()
                    conexion.close()
                    exit()
                else:
                    print("Opción no válida.")

# ============================================================
# OPCION 2 - BUSCAR ALUMNOS
# ============================================================

    elif opcion == "2":

        while True:

    #=============================================================
    # AQUI VAMOS A SOLICITAR LA EDAD MINIMA
    #=============================================================
            while True:
                edad_minima = input("Introduce la edad mínima: ")

                if edad_minima.isdigit() == False:
                    print("La edad solo puede contener números.")

                elif int(edad_minima) < 1 or int(edad_minima) > 121:
                    print("La edad debe estar entre 1 y 121 años.")

                else:
                    edad_minima = int(edad_minima)
                    break

    #=============================================================
    # AQUI VAMOS A SOLICITAR LA EDAD MAXIMA
    #=============================================================
            while True:
                edad_maxima = input("Introduce la edad máxima: ")

                if edad_maxima.isdigit() == False:
                    print("La edad solo puede contener números.")

                elif int(edad_maxima) < 1 or int(edad_maxima) > 121:
                    print("La edad debe estar entre 1 y 121 años.")

                else:
                    edad_maxima = int(edad_maxima)
                    break

    #=============================================================
    # AQUI VAMOS A SOLICITAR LA PRIMERA PROVINCIA
    #=============================================================
            while True:
                provincia1 = input("Introduce la primera provincia: ")
                caracter_incorrecto = False
                for caracter in provincia1:
                    if caracter.isdigit() or caracter in ".,;:'@#$%&()!?/":
                        caracter_incorrecto = True

                if caracter_incorrecto:
                    print("La provincia contiene caracteres no permitidos.")
                elif len(provincia1) > 30:
                    print("La provincia no puede superar 30 caracteres.")
                else:
                    break

    #=============================================================
    # AQUI VAMOS A SOLICITAR LA SEGUNDA PROVINCIA
    #=============================================================
            while True:
                provincia2 = input("Introduce la segunda provincia: ")
                caracter_incorrecto = False
                for caracter in provincia2:
                    if caracter.isdigit() or caracter in ".,;:'@#$%&()!?/":
                        caracter_incorrecto = True

                if caracter_incorrecto:
                    print("La provincia contiene caracteres no permitidos.")
                elif len(provincia2) > 30:
                    print("La provincia no puede superar 30 caracteres.")
                else:
                    break

            sql = """SELECT * FROM alumnos
            WHERE edad BETWEEN %s AND %s
            AND (provincia = %s OR provincia = %s)"""

            valores = (edad_minima, edad_maxima, provincia1, provincia2)

            cursor.execute(sql, valores)

            resultado = cursor.fetchall()

            if resultado:

                fichero = open(
                    ruta_backup + "\\resultado16.csv",
                    "w",
                    newline=""
                )

                escribir = csv.writer(fichero, delimiter=";")

                for fila in resultado:

                    escribir.writerow(fila)

                fichero.close()

                print()
                print("HEMOS ENCONTRADO ESTOS USUARIOS:")
                print()

                for fila in resultado:

                    print("DNI:", fila[0], "- Nombre:", fila[1], "- Edad:", fila[2])

            else:

                print()
                print("====================================")
                print("NO SE HAN ENCONTRADO REGISTROS CON ESE FILTRO")
                print("====================================")
                print()

            nueva_busqueda = input("¿Desea realizar una nueva búsqueda? (S/N): ")

            if nueva_busqueda.upper() == "S":

                continue

            else:

                break

# ============================================================
# OPCION 3 - SALIR
# ============================================================

    elif opcion == "3":

        print()
        print("====================================")

    #=============================================================
    # LEER FECHA DE LA ULTIMA COPIA
    #=============================================================
        try:
            archivo_fecha = open(ruta_backup + "\\ultima_copia.txt", "r")
            fecha_ultima_copia = archivo_fecha.read()
            archivo_fecha.close()
            print("Última copia de seguridad: " + fecha_ultima_copia)
        except:
            print("No hay copia de seguridad realizada")

        print("====================================")
        print()

        break

cursor.close()
conexion.close()