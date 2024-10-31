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


div = int(input("Dividends: "))
div2 = int(input("Divider: "))

quotient = div // div2
reminder = div % div2


if reminder == 0:
    print("La división es exacta.")
else:
    print("La división no es exacta.")
print(f"quotient: {quotient}")
print(f"Reminder: {reminder}")

