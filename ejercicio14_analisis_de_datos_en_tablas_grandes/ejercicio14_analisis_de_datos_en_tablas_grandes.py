#14 Analisis de datos en tablas grandes

# El codigo empezamos por IMPORT OS y luego definimos la carpeta y el fichero, despues juntamos la carpeta y el fichero con os.path.join y luego con os.path.abspath obtenemos la ruta absoluta del fichero.
import os 

carpeta = "C:/Users/jpedr/Desktop/iecmgrupocolon/ejercicio14_analisis_de_datos_en_tablas_grandes/"
fichero = "poblacion.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

#Ahora vamos a leer el fichero y a cargarlo en un array (array es una lista en python
datos = list()  # Inicializamos el array de destino
archivo = open(ruta, mode="r")
contenido = archivo.readlines()
for linea in contenido:
    numcamp = linea.count(";")
    registro = linea.replace('\n', '')
    registro = registro.replace(",", ".")  # Reemplazar comas por puntos decimales
    datos.append(registro.split(";"))

archivo.close()

#Ahora vamos a dibujar la tabla con format para que se vea bien
for i in range(len(datos)):
    linea = ""
    for j in range(numcamp + 1):  # numcamp es el número de campos, pero necesitamos iterar hasta numcamp + 1 para incluir el último campo
        linea = linea + "{:<20}".format(datos[i][j])
    print(linea + "\n")

#REVISION! (LA ESTRUCTURA DEL LOS EJERCICIOS)
#1* IMPORTAR OS.
#2* DEFINIMOS LA CARPETA Y EL FICHERO.
#3* JUNTAMOS LA CARPETA Y EL FICHERO CON OS.PATH.JOIN Y LUEGO CON OS.PATH.ABSOLUT OBTENEMOS LA RUTA ABSOLUTA DEL FICHERO.
#4* LEEMOS EL FICHERO Y LO CARGAMOS EN UN ARRAY (ARRAY ES UNA LISTA EN PYTHON).
#5* DIBUJAMOS LA TABLA CON FORMAT PARA QUE SE VEA BIEN.


#AHORA VAMOS A QUITAR EL ENCABEZADO PORQUE EL ENCABEZADO ES LETRA Y NO NUMERO.

del datos[0]  # Elimina el primer elemento del array, que es el encabezado

#AHORA VAMOS A CALCULAR

municipios_mar = 0
#aqui vamos a cachear/buscar los municipios de la provinciac con mar.
for i in range(len(datos)):
    km_costa = float(datos[i][2])  # Convertir el valor a float para compararlo
    if km_costa > 0: 
        municipios_mar += 1

print("\n========== EJERCICIO 1 ==========\n")
print(f"El número de municipios en Mar es: {municipios_mar}")

#2. Número de municipios con más de 15.000 habitantes

municipios_15000 = 0
#1* CREAMOS LA VARIABLE MUNICIPIOS_15000 PARA CONTAR LOS MUNICIPIOS CON MÁS DE 15.000 HABITANTES.

#Y hacemos lo mismo con FOR y IN RANGE PARA RECORRER EL ARRAY DE DATOS Y BUSCAR LOS MUNICIPIOS CON MÁS DE 15.000 HABITANTES.

for i in range(len(datos)):
    habitantes = int(datos[i][7])  # Convertir el valor a entero para compararlo
    if habitantes > 15000: 
        municipios_15000 += 1

print(f"El número de municipios con más de 15.000 habitantes es: {municipios_15000}")

#3. Suma total de playas de la provincia

suma_playas = 0

for i in range(len(datos)):
    playas = int(datos[i][3])  # Convertir el valor a entero para sumarlo
    suma_playas += playas  

print(f"La suma total de playas de la provincia es: {suma_playas}") 

#4. Suma total de habitantes que viven en municipios costeros

suma_municipios_costeros = 0

for i in range(len(datos)):
    km_costa = float(datos[i][2])  # Convertir el valor a float para compararlo
    habitantes = int(datos[i][7])  # Convertir el valor a entero para sumarlo
    if km_costa > 0: 
        suma_municipios_costeros += habitantes

print(f"La suma total de habitantes que viven en municipios costeros es: {suma_municipios_costeros}")   

#5. Suma total de los habitantes que viven en municipios de menos de 5.000 habitantes

suma_municipios_menores_5000 = 0

for i in range(len(datos)):
    habitantes = int(datos[i][7])  # Convertir el valor a entero para compararlo
    if habitantes < 5000:
        suma_municipios_menores_5000 += habitantes

print(f"La suma total de los habitantes que viven en municipios de menos de 5.000 habitantes es: {suma_municipios_menores_5000}")

#6. Suma total de kilómetros de costa de la provincia

suma_km_costa = 0.0
for i in range(len(datos)):
    km_costa = float(datos[i][2])  # Convertir el valor a float para sumarlo
    suma_km_costa += km_costa

print(f"La suma total de kilómetros de costa de la provincia es: {suma_km_costa}")


#7 Suma total de viviendas en pueblos costeros.

suma_vivendas_costeras = 0
for i in range(len(datos)):
    km_costa = float(datos[i][2])  # Convertir el valor a float para compararlo
    viviendas = int(datos[i][4])  # Convertir el valor a entero para sumarlo
    if km_costa > 0: 
        suma_vivendas_costeras += viviendas

print(f"La suma total de viviendas en pueblos costeros es: {suma_vivendas_costeras}")   

#8.Densidad de población en costa (Viviendas en costa / habitantes en costa)

densidad_poblacion_costa = suma_vivendas_costeras / suma_municipios_costeros


print(f"La densidad de población en costa es: {round(densidad_poblacion_costa, 2)}")



#9. Densidad de población en no costeros (Viviendas en no costeros / habitantes en no costeros)
suma_vivendas_no_costeras = 0
suma_habitantes_no_costeros = 0

for i in range(len(datos)):
    km_costa = float(datos[i][2])  # Convertir el valor a float para compararlo
    viviendas = int(datos[i][4])  # Convertir el valor a entero para sumarlo
    habitantes = int(datos[i][7])  # Convertir el valor a entero para sumarlo
    if km_costa == 0: 
        suma_vivendas_no_costeras += viviendas
        suma_habitantes_no_costeros += habitantes


densidad_no_costeros = suma_vivendas_no_costeras / suma_habitantes_no_costeros

print(f"La densidad de población en no costeros es: {round(densidad_no_costeros, 2)}")


#Ahora vamos a guardar los resultados en un fichero de texto llamado resultados.txt, para eso abrimos el fichero en modo escritura y escribimos los resultados con formato.
resultado = open(carpeta + "resultados.txt", mode="w")

linea = "Número de municipios en Mar: " + str(municipios_mar) + "\n"
linea += "Número de municipios con más de 15.000 habitantes: " + str(municipios_15000) + "\n"
linea += "Suma total de playas de la provincia: " + str(suma_playas) + "\n"
linea += "Suma total de habitantes que viven en municipios costeros: " + str(suma_municipios_costeros) + "\n"
linea += "Suma total de los habitantes que viven en municipios de menos de 5.000 habitantes: " + str(suma_municipios_menores_5000) + "\n"
linea += "Suma total de kilómetros de costa de la provincia: " + str(round(suma_km_costa, 2)) + "\n"
linea += "Suma total de viviendas en pueblos costeros: " + str(suma_vivendas_costeras) + "\n"
linea += "Densidad de población en costa: " + str(round(densidad_poblacion_costa, 2)) + "\n"
linea += "Densidad de población en no costeros: " + str(round(densidad_no_costeros, 2)) + "\n"

resultado.write(linea)

resultado.close()