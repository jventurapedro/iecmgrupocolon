import os

os.system("cls")

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", db="")
cursor1=conexion1.cursor()




cursor1.execute("drop database if exists tiempo;")
cursor1.execute("create database tiempo character set latin1 collate latin1_spanish_ci;")
cursor1.execute("use tiempo;")
cursor1.execute("create table verano (`fecha` DATE PRIMARY KEY, `dia` VARCHAR(15), `alcorcon` FLOAT, `mostoles` FLOAT, `leganes` FLOAT, `fuenlabrada` FLOAT, `getafe` FLOAT, `temp_media` FLOAT, `clasificacion` VARCHAR(10));")

cursor1.execute("LOAD DATA INFILE 'C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio18_arrays_usando_numpy/ejercicio18.csv' INTO TABLE verano FIELDS TERMINATED BY  ';' LINES TERMINATED BY '\n'")

conexion1.commit()       # IMPORTANTE ACTUALIZAR SIEMPRE LA BASE DE DATOS

cursor1.execute("SELECT fecha, alcorcon, mostoles, leganes, fuenlabrada, getafe FROM verano ORDER BY fecha")
datos = cursor1.fetchall()

for fila in datos:
    fecha = fila[0]
    alcorcon = fila[1]
    mostoles = fila[2]
    leganes = fila[3]
    fuenlabrada = fila[4]
    getafe = fila[5]
    
    temp_media = (alcorcon + mostoles + leganes + fuenlabrada + getafe) / 5
    
    if temp_media > 25:
        clasificacion = "Cálido"
    elif 20 <= temp_media <= 25:
        clasificacion = "Templado"
    else:
        clasificacion = "Frío"
    
    cursor1.execute("UPDATE verano SET temp_media = %s, clasificacion = %s WHERE fecha = %s", (temp_media, clasificacion, fecha))

conexion1.commit()


#==========================================================
# DIBUJAR TABLA COMPLETA
#==========================================================

cursor1.execute("select * from verano")

tabla = []

for fila in cursor1:
    tabla.append(fila)

filas = len(tabla)

if filas > 0:
    columnas = len(tabla[0])

    #====== Encabezados
    cabecera = ["fecha", "dia", "alcorcon", "mostoles", "leganes", "fuenlabrada", "getafe", "temp_media", "clasificacion"]
    
    linea = ""
    for j in range(columnas):
        linea = linea + ("{0:12s}{1}".format(cabecera[j], " | "))
    print(linea)
    
    print("-" * 140)

    #====== Filas de datos
    for i in range(filas):
        linea = ""
        
        for j in range(columnas):
            linea = linea + ("{0:12s}{1}".format(str(tabla[i][j]), " | "))
            
        print(linea)
        
else:
    print("La tabla no tiene registros")


#==========================================================
# GENERAR CSV CALIDO
#==========================================================

cursor1.execute("SELECT fecha, dia, alcorcon, mostoles, leganes, fuenlabrada, getafe, temp_media FROM verano WHERE clasificacion = 'Cálido' ORDER BY fecha")
datos_calido = cursor1.fetchall()

archivo = open("C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio18_arrays_usando_numpy/calido.csv", "w", encoding="utf-8")
archivo.write("fecha;dia;alcorcon;mostoles;leganes;fuenlabrada;getafe;temp_media\n")

for fila in datos_calido:
    fecha = fila[0]
    dia = fila[1]
    alcorcon = fila[2]
    mostoles = fila[3]
    leganes = fila[4]
    fuenlabrada = fila[5]
    getafe = fila[6]
    temp_media = fila[7]
    
    linea = f"{fecha};{dia};{alcorcon};{mostoles};{leganes};{fuenlabrada};{getafe};{temp_media}\n"
    archivo.write(linea)

archivo.close()

#==========================================================
# GENERAR CSV TEMPLADO
#==========================================================

cursor1.execute("SELECT fecha, dia, alcorcon, mostoles, leganes, fuenlabrada, getafe, temp_media FROM verano WHERE clasificacion = 'Templado' ORDER BY fecha")
datos_templado = cursor1.fetchall()

archivo = open("C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio18_arrays_usando_numpy/templado.csv", "w", encoding="utf-8")
archivo.write("fecha;dia;alcorcon;mostoles;leganes;fuenlabrada;getafe;temp_media\n")

for fila in datos_templado:
    fecha = fila[0]
    dia = fila[1]
    alcorcon = fila[2]
    mostoles = fila[3]
    leganes = fila[4]
    fuenlabrada = fila[5]
    getafe = fila[6]
    temp_media = fila[7]

    linea = f"{fecha};{dia};{alcorcon};{mostoles};{leganes};{fuenlabrada};{getafe};{temp_media}\n"
    archivo.write(linea)

archivo.close()

#==========================================================
# GENERAR CSV FRIO
#==========================================================

cursor1.execute("SELECT fecha, dia, alcorcon, mostoles, leganes, fuenlabrada, getafe, temp_media FROM verano WHERE clasificacion = 'Frío' ORDER BY fecha")
datos_frio = cursor1.fetchall()

archivo = open("C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio18_arrays_usando_numpy/frio.csv", "w", encoding="utf-8")
archivo.write("fecha;dia;alcorcon;mostoles;leganes;fuenlabrada;getafe;temp_media\n")

for fila in datos_frio:
    fecha = fila[0]
    dia = fila[1]
    alcorcon = fila[2]
    mostoles = fila[3]
    leganes = fila[4]
    fuenlabrada = fila[5]
    getafe = fila[6]
    temp_media = fila[7]

    linea = f"{fecha};{dia};{alcorcon};{mostoles};{leganes};{fuenlabrada};{getafe};{temp_media}\n"
    archivo.write(linea)

archivo.close()

#==========================================================
# ANALISIS DE LOS DATOS
# Datos por cada ciudad analizada:
# Media Temperatura Septiembre
# Media Temperatura Octubre
# Nº de Días Con Temperaturas Frías
# Nº de Días Con Temperaturas Templadas
# Nº de Días Con Temperaturas Cálidas
#==========================================================

cursor1.execute("SELECT * FROM verano ORDER BY fecha")
todos_datos = cursor1.fetchall()

archivo = open("C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio18_arrays_usando_numpy/datos.csv", "w", encoding="utf-8")
archivo.write("Ciudad;Media Septiembre;Media Octubre;Dias Frios;Dias Templados;Dias Calidos\n")

# ==========================================================
# Aqui vamos a crear una lista con los nombres de las ciudades y otra lista con los indices de cada ciudad en la tabla
# ==========================================================

ciudades = ["alcorcon", "mostoles", "leganes", "fuenlabrada", "getafe"]
indices_ciudades = [2, 3, 4, 5, 6]

# =========================================================
# Ahora vamos a recorrer cada ciudad y calcular los datos solicitados
# =========================================================

for ciudad, indice in zip(ciudades, indices_ciudades):
    temp_septiembre = []
    temp_octubre = []
    dias_frios = 0
    dias_templados = 0
    dias_calidos = 0
    
    for fila in todos_datos:
        fecha = fila[0]
        dia = fila[1]
        temp = fila[indice]
        clasificacion = fila[8]
        
        if fecha.month == 9:
            temp_septiembre.append(temp)
        elif fecha.month == 10:
            temp_octubre.append(temp)
        
        if clasificacion == "Frío":
            dias_frios += 1
        elif clasificacion == "Templado":
            dias_templados += 1
        elif clasificacion == "Cálido":
            dias_calidos += 1
    
    media_septiembre = sum(temp_septiembre) / len(temp_septiembre) if temp_septiembre else 0
    media_octubre = sum(temp_octubre) / len(temp_octubre) if temp_octubre else 0
    
    linea = f"{ciudad};{media_septiembre:.2f};{media_octubre:.2f};{dias_frios};{dias_templados};{dias_calidos}\n"
    archivo.write(linea) 

archivo.close()

cursor1.close()
conexion1.close()