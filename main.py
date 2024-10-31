#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.
#La salida del programa debe ser el resultado de la operación.
#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5
#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1
#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20
#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5
#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1

number1 = float(input("Insert number: "))
symbol = (input("Insert operator (+, -, *, /): "))
number2 = float(input("Insert number: "))

if symbol == "+":
    answer1 = number1 + number2
    print (f"{number1} + {number2} = {answer1}")
elif symbol == "-":
    answer2 = number1 - number2
    print (f"{number1} - {number2} = {answer2}")
elif symbol == "*":
    answer3 = number1 * number2
    print (f"{number1} * {number2} = {answer3}")
elif symbol == "/":
    if number2 !=0:
        answer4 = number1 / number2
        print (f"{number1} / {number2} = {answer4}")
else:
        print ("No valid")