#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

#Dividendo: 14
#Divisor: 5

#La división no es exacta.
#Cociente: 2
#Resto: 4
#dividendo: 100
#Divisor: 10

#La división es exacta.
#Cociente: 10
#Resto: 0

# Solicitar al usuario que ingrese el dividendo y el divisor
div = int(input("Dividends: "))
div2 = int(input("Divider: "))

# Calcular el cociente y el resto
quotient = div // div2
reminder = div % div2

# Verificar si la división es exacta
if reminder == 0:
    print("La división es exacta.")
else:
    print("La división no es exacta.")

# Mostrar el cociente y el resto
print(f"quotient: {quotient}")
print(f"Reminder: {reminder}")

