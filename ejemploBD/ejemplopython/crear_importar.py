# Paquete de Python necesario para conectarnos a MySQL.

# Utilizaremos el programa 'pip' que vimos anteriormente para instalar el paquete necesario 
# para interconectar 'Python' y 'MySQL'. Desde la línea de comandos ejecutamos el programa pip con el siguiente paquete a instalar:

# pip install mysql-connector

# Luego de ejecutar el programa pip podemos ver que nos informa de la instalación del paquete 'mysql-connector': 

# python.exe  -m install  --upgrade pip


import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", db="", allow_local_infile=True)
cursor1=conexion1.cursor()

cursor1.execute("drop database if exists coches;")
cursor1.execute("create database coches character set latin1 collate latin1_spanish_ci;")
cursor1.execute("use coches;")
cursor1.execute("create table datos (marca varchar(10), modelo varchar(10), anyo varchar(4), color varchar(10), matricula varchar(7) PRIMARY KEY);")
cursor1.execute("insert into datos values ('Suzuki','Jimny', '2020', 'Gris','0547NHB');")
cursor1.execute("LOAD DATA INFILE 'C:/Users/jpedr/Desktop/iecmgrupocolon/ejemploBD/ejemplopython/base_coches.csv' INTO TABLE datos FIELDS TERMINATED BY  '\t' LINES TERMINATED BY '\n'")

conexion1.commit()

opcion = input("Quieres introducir algun registro mas? (S/N): ")

opcion = opcion.upper()

if (opcion == "S"):
    marca = input("Escribe la marca del vehiculo: ")
    modelo = input("Escribe el modelo del vehiculo: ")
    anyo = input("Escribe el año de matriculación: ")
    color = input("Escribe la color del vehiculo: ")
    matricula = input("Escribe la matricula del vehiculo: ")

    cursor1.execute("insert into datos values ('" + marca + "','" + modelo + "', '" + anyo + "', '" + color + "','" + matricula +"');")
    conexion1.commit()

cursor1.execute("show tables")

longitud = 0
for tabla in cursor1:
    print(tabla)
    longitud += 1

print("En la base de datos tienes " + str(longitud) + " tablas\n")

opcion = input("Escribe el nombre de la tabla que quieres ver: ")



cursor1.execute("select * from " + opcion + ";")

longitud = 0
for fila in cursor1:
    ancho = len(fila)
    print(fila)
    longitud += 1


print("\nEn la tabla " + opcion + " tienes " + str(ancho)+ " campos y " + str(longitud) + " registros \n")



conexion1.close()

