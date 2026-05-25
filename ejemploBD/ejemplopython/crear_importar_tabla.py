
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", db="", allow_local_infile=True)
cursor1=conexion1.cursor()

cursor1.execute("drop database if exists coches;")
cursor1.execute("create database coches character set latin1 collate latin1_spanish_ci;")
cursor1.execute("use coches;")
cursor1.execute("create table datos (marca varchar(10), modelo varchar(10), anyo varchar(4), color varchar(10), matricula varchar(7) PRIMARY KEY);")
cursor1.execute("insert into datos values ('Suzuki','Jimny', 2020, 'Gris','0547NHB');")
cursor1.execute("LOAD DATA INFILE 'C:/Users/jpedr/Desktop/iecmgrupocolon/ejemploBD/ejemplopython/base_coches.csv' INTO TABLE datos FIELDS TERMINATED BY  '\t' LINES TERMINATED BY '\n'")

conexion1.commit()

cursor1.execute("select * from datos;")

tabla = list()

for fila in cursor1:
    tabla.append(fila)


for i in range(len(tabla)):
    linea = ""
    for j in range(len(tabla[i])):
        linea = linea + str(tabla[i][j]) + "\t"
    print(linea)


print("\nEn la tabla datos tienes " + str(len(tabla[0]))+ " campos y " + str(len(tabla)) + " registros \n")

conexion1.close()

