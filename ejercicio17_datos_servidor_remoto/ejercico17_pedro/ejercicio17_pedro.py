#====================================================
# ejercicio17_datos_servidor_remoto
#====================================================
# IMPORTAR LIBRERIA
#====================================================

import mysql.connector
import os
os.system("cls")

#====================================================
# CONECTAR A LA BASE DE DATOS
#====================================================

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ejercicio17"
)

cursor = conexion.cursor()

#====================================================
# CONSULTAR LOS DATOS DE LA TABLA 
# UTILIZANDO SELECT * FROM 
#====================================================

sql = "SELECT * FROM datos"
cursor.execute(sql)
datos = cursor.fetchall()

#====================================================
# IMPRIMIR LOS DATOS DE LA TABLA + TITULO
#====================================================

print()
print("====================================================")
print("==============TABLA DE DATOS EMPRESA ===============")
print("====================================================")

print()

for fila in datos:

    print("| {:<5} | {:<25} | {:<22} | {:<12} | {:<8} | {:>15} |".format(

        fila[0],
        fila[1],
        fila[2],
        fila[3],
        fila[4],
        fila[5]

    ))

#====================================================
# VAMOS A CREAR LAS VARIABLES PARA GUARDAR LOS DATOS DE LA TABLA
# Porque vamos a necesitar estas variables para hacer los calculos que nos piden en el ejercicio
# entonces por eso vamos a crear estas variables para guardar los datos de la tabla y luego hacer los calculos que nos piden en el ejercicio
# #====================================================

total_facturacion_clientes = 0
total_pagos_proveedores = 0

total_clientes = 0
total_proveedores = 0

clientes_morosos = 0
proveedores_morosos = 0

clientes_madrid = 0

#====================================================
# RECORRER LOS DATOS DE LA TABLA
#====================================================

for fila in datos:
    codigo = fila[0]
    empresa = fila[1]
    direccion = fila[2]
    poblacion = fila[3]
    estatus = fila[4]
    facturacion = float(fila[5])

#====================================================
# CLIENTES
#====================================================

    if estatus == "Cliente":
        total_clientes += 1
        total_facturacion_clientes += facturacion
        if facturacion < 0:
            clientes_morosos += 1
        if poblacion == "Madrid":
            clientes_madrid += 1

#====================================================
# PROVEEDORES
#====================================================

    elif estatus == "Proveedor":
        total_proveedores += 1
        total_pagos_proveedores += facturacion
        if facturacion < 0:
            proveedores_morosos += 1

#====================================================
# CALCULOS
#====================================================

beneficio_total = total_facturacion_clientes - total_pagos_proveedores

media_facturacion_clientes = total_facturacion_clientes / total_clientes

media_pagos_proveedores = total_pagos_proveedores / total_proveedores

#====================================================
# IMPRIMIR LOS RESULTADOS
#====================================================

print()
print("====================================================")
print("=================== RESULTADOS =====================")
print("====================================================")

print()

print("| {:<20} | {:>8.2f} |".format("Facturacion clientes", total_facturacion_clientes))

print("| {:<20} | {:>8.2f} |".format("Pagos proveedores", total_pagos_proveedores))

print("| {:<20} | {:>8.2f} |".format("Beneficio total", beneficio_total))

print("| {:<20} | {:>8.2f} |".format("Media clientes", media_facturacion_clientes))

print("| {:<20} | {:>8.2f} |".format("Media proveedores", media_pagos_proveedores))

print("| {:<20} | {:>8} |".format("Total clientes", total_clientes))

print("| {:<20} | {:>8} |".format("Total proveedores", total_proveedores))

print("| {:<20} | {:>8} |".format("Clientes morosos", clientes_morosos))

print("| {:<20} | {:>8} |".format("Proveedores morosos", proveedores_morosos))

print("| {:<20} | {:>8} |".format("Clientes Madrid", clientes_madrid))

print()

#====================================================
# GENERAR Y GUARDAR CSV
#====================================================
#====================================================
# GUARDAR RESULTADOS EN CSV
#====================================================

archivo = open("resultados.csv", mode="w")

archivo.write("Facturacion total clientes;" + str(round(total_facturacion_clientes, 2)) + "\n")

archivo.write("Total pagos proveedores;" + str(round(total_pagos_proveedores, 2)) + "\n")

archivo.write("Beneficio total;" + str(round(beneficio_total, 2)) + "\n")

archivo.write("Media facturacion clientes;" + str(round(media_facturacion_clientes, 2)) + "\n")

archivo.write("Media pagos proveedores;" + str(round(media_pagos_proveedores, 2)) + "\n")

archivo.write("Total clientes;" + str(round(total_clientes, 2)) + "\n")

archivo.write("Total proveedores;" + str(round(total_proveedores, 2)) + "\n")

archivo.write("Clientes morosos;" + str(round(clientes_morosos, 2)) + "\n")

archivo.write("Proveedores morosos;" + str(round(proveedores_morosos, 2)) + "\n")

archivo.write("Clientes Madrid;" + str(round(clientes_madrid, 2)) + "\n")

archivo.close()

#====================================================
# CERRAR LA CONEXION A LA BASE DE DATOS
#====================================================
cursor.close()
conexion.close()

