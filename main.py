#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
#
#Ingrese numero: 51
#Ingrese numero: 24
#24 51
#A continuación, escriba otro programa que haga lo mismo con tres números:

#Ingrese numero: 8
#Ingrese numero: 1
#Ingrese numero: 4
#1 4 8
#Finalmente, escriba un tercer programa que ordene cuatro números:

#Ingrese numero: 7
#Ingrese numero: 0
#Ingrese numero: 6
#Ingrese numero: 1
# 1 6 7
#Recuerde que su programa debe entregar la solución correcta para cualquier combinación de números, no sólo para los ejemplos mostrados aquí.

#Hay más de una manera de resolver cada ejercici#o.

#Programa para ordenar dos números:

number1 = int(input("insert number: "))
number2 = int(input("insert number: "))

if number1 > number2:
    print(number2, number1)
else:
    print(number1, number2)

#print("Exercise 5 sort numbers")

number1 = int(input("insert number: "))
number2 = int(input("insert number: "))
number3 = int(input("insert number: "))

numbers = [number1 ,number2, number3]
numbers.sort()

print(numbers)

#print("Exercise 5 sort numbers")

n1 = int(input("insert number: "))
n2 = int(input("insert number: "))
n3 = int(input("insert number: "))
n4 = int(input("insert number: "))

numbers = [n1 ,n2, n3, n4]
numbers.sort()

print(numbers)