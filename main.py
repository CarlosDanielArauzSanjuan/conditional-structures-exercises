#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. 
# En caso que sea letra, determine si es mayúscula o minúscula.

#Ingrese caracter: 9
#Es numero.
#Ingrese caracter: A
#Es letra mayúscula.
#Ingrese caracter: f
#Es letra minúscula.
#Ingrese caracter: #
#No es letra ni número.#


character = input ("insert a single character: ")

if character.isdigit():
    print ("Is a number")

elif character.isalpha(): 
    if character.isupper():
        print ("the letter is odded")
    else:
        print ("the letter is lowercase")
else:
    print ("It is neither a letter nor a number")