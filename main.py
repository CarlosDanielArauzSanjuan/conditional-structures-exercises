#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

# 	edad < 45	edad ≥ 45
#IMC < 22.0	bajo	medio
#IMC ≥ 22.0	medio	alto
#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

stature  = float(input("Enter stature: "))
Weight   = float(input("Enter weight: "))
age      = float(input("Enter age: "))

corporal  = Weight / (stature**2)

if age < 45:
    if corporal < 22.0:
        risk = "low"
    else:
        risk = "medium"
else:
    if corporal < 22.0:
        risk = "medium"
    else:
        risk = "high"

print(f"Your risk of coronary heart disease is {risk}.")