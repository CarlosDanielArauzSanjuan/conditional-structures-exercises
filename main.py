#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

#Ingrese su fecha de nacimiento.
#Dia: 14
#Mes: 6
#Anno: 1948
#Usted tiene 62 annos
#Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.

#Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2011):

#3>>> from time import localtime
#>>> t = localtime()
#>>> t.tm_mday
#11
#>>> t.tm_mon
#3
#>>> t.tm_year
#2011
from time import localtime

day = int(input("Please, enter your day of birth: "))
month = int(input("Please, enter your nonth of birth: "))
year = int(input("Please, enter your year of birth: "))

t = localtime()
actual_day = t.tm_mday
actual_month = t.tm_mon
actual_year = t.tm_year

age = actual_year - year

if (actual_month < month) or (actual_month == month and actual_day < day):
    age -=1 

print (f"you have {age} years old")

# !!!! watchouts !!!
#from time import localtime
#t = localtime()
#actual_day = t.tm_mday
#actual_month = t.tm_mon
#actual_year = t.tm_year
