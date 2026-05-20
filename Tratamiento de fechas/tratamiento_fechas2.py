
# Para trabajar con fechas es necesario importar las librerias necesarias

# Previamente hay que instalar como administrador el siguiente comando:

            # pip install python-dateutil


from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas

# Lista de algunos de los formatos de código más usados en fechas:

#   %d - El día del mes con un número decimal con ceros como  28.
#   %a - El nombre abreviado de un día, por ejemplo, domingo (Sunday) se abrevia a Sun
#   %A - El nombre completo del día Sunday.
#   %m - El mes como un decimal acompañado de cero, cómo es el caso de 01.
#   %b - El nombre abreviado del mes como Jan.
#   %B - El nombre completo del mes January.
#   %y - El año sin siglos 23.
#   %Y - El año con siglos 2023.
#   %H - Las horas del día en un formato de 24 horas, al igual que 08.
#   %I - Las horas del día en un formato de 12 horas.
#   %M - Los minutos en una hora, al igual que 20.
#   %S - Los segundos en un minuto, al igual que 00.


import os

os.system("cls")

# Conversión de una cadena a fecha

fecha = "2016-04-15"

# En esta parte aplicamos la conversion y creación del objeto fecha

fecha_dato = datetime.strptime(fecha, "%Y-%m-%d")

anyo = fecha_dato.year

mes = fecha_dato.month

dia = fecha_dato.day

hora = fecha_dato.hour

minutos = fecha_dato.minute

segundos = fecha_dato.second

print ("La fecha introducida es la siguiente: " + fecha)
print ("\nDia: " + str(dia))
print ("Mes: " + str(mes))
print ("Año: " + str(anyo))
print ("Hora: " + str(hora))
print ("Minutos: " + str(minutos))
print ("Segundos: " + str(segundos))



