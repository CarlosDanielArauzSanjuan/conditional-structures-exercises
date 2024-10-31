#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.

#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.
#Ingrese a: 3.9
#Ingrese b: 6.0
#Ingrese c: 1.2
#No es un triangulo valido.
#Ingrese a: 1.9
#Ingrese b: 2
#Ingrese c: 2
#El triangulo es isoceles.
#Ingrese a: 3.0
#Ingrese b: 5.0
#Ingrese c: 4.0
#El triangulo es escaleno.


t1 = float(input("Enter side A: "))
t2 = float(input("Enter side B: "))
t3 = float(input("Enter side C: "))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    if  t1 == t2 == t3:
        print ("triangle is equilateral")
    elif t1 == t2 or t1 == t3 or t2 == t3:
        print ("triangle is isosceles")
    else:
        print ("triangle is scalene")
else:
    print ("its no a valid triangle ")