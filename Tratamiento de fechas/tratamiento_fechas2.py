
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


# Día actual
today = date.today()

# Fecha actual
now = datetime.now()

print(today)
print(now)


# Una vez obtengamos la fecha actual podremos obtener el día, mes, año, hora, minutos y segundos

# Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))


# Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))


# Conversión de una cadena a fecha

fecha = "31/12/2023"

# En esta parte aplicamos la conversion y creación del objeto fecha

date_time_object = datetime.strptime(fecha, "%d/%m/%Y")

print(date_time_object.day)
print(date_time_object.month)
print(date_time_object.year)
