
# Para trabajar con fechas es necesario importar las librerias necesarias

# Previamente hay que instalar como administrador el siguiente comando:

            # pip install datetime

            # pip install python-dateutil

from datetime import date, datetime, timedelta


from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas 
                                                    #   tipo años, meses, minutos y segundos

# Lista de algunos de los formatos de código más usados en fechas:

#   %d - El día del mes con un número sin ceros, formato 8.
#   %a - El nombre abreviado del día de la semana, por ejemplo, domingo (Sunday) se abrevia a Sun
#   %A - El nombre completo del día de la semana, Sunday.
#   %m - El mes como un número acompañado de cero, cómo es el caso de 01.
#   %b - El nombre abreviado del mes, como Jan.
#   %B - El nombre completo del mes, January.
#   %y - El año sin siglos, 23.
#   %Y - El año con siglos, 2023.
#   %H - Las horas del día en un formato de 24 horas, como 18.
#   %I - Las horas del día en un formato de 12 horas, como 6 (PM).
#   %M - Los minutos en una hora, en formato 20.
#   %S - Los segundos en un minuto, en formato 00.


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

fecha = "31/12/2023 23:59:59"

# En esta parte aplicamos la conversion y creación del objeto fecha

date_time_object = datetime.strptime(fecha, "%d/%m/%Y %H:%M:%S")

print(date_time_object)






# Para trabajar solamente con la fecha

date_object = datetime.strptime(fecha, "%d/%m/%Y %H:%M:%S").date()

print(date_object)

# Para trabajar solamente con la hora

time_object = datetime.strptime(fecha,"%d/%m/%Y %H:%M:%S").time()

print(time_object)




# Conversión de una cadena a fecha solamente

fecha = "31/12/2023"

# En esta parte aplicamos la conversion y creación del objeto fecha

date_time_object = datetime.strptime(fecha, "%d/%m/%Y")

print(date_time_object.day)     # Aqui obtenemos el dia
print(date_time_object.month)   # Aqui obtenemos el mes
print(date_time_object.year)    # Aqui obtenemos el año






# Sumar días u horas a la fecha actual. Para restar usar números negativos

new_date = now + timedelta(days=2)

new_date = now + timedelta(hours=2)

# Sumar años, meses, minutos o segundos a la fecha actual. Para restar usar números negativos

new_date = now + relativedelta(years=2)

new_date = now + relativedelta(months=2)

new_date = now + relativedelta(minutes=2)

new_date = now + relativedelta(seconds=2)

print(new_date)





#Comparación

if now < new_date:
    print("La fecha actual es menor que la nueva fecha")
    
# Pregunta: ¿Cuántos dias quedan para Fin de Año?

dias = (date_object - today).days

print ("Faltan " + str(dias) + " dias para Fin de Año")

