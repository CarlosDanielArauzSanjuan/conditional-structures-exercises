#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

#Palabra 1: edificio
#Palabra 2: tren
#La palabra edificio tiene 4 letras mas que tren.
#Palabra 1: sol
#Palabra 2: paralelepipedo
#La palabra paralelepipedo tiene 11 letras mas que sol
#Palabra 1: plancha
#alabra 2: lapices
#Las dos palabras tienen el mismo largo


word1 = input("word 1: ")
word2 = input("word2: ")

long1 = len(word1)
long2 = len(word2)

if long1 > long2:
    diference = long1 - long2
    print(f"the word {word1} have {diference} more letters than {word2}.")
elif long2 > long1:
    diference = long2 - long1
    print(f"the word {word2} have {diference} more letters than  {word1}.")
else:
    print("both words are same number of letters.")