#El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.

#Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

#si A ganó el set, o
#si B ganó el set, o
#si el set todavía no termina, o
#si el resultado es inválido (por ejemplo, 8-6 o 7-3).
#Desarrolle un programa que solucione el problema de Solarrabietas:

#Juegos ganados por A: 4
#Juegos ganados por B: 5
#Aun no termina
#Juegos ganados por A: 5
#Juegos ganados por B: 7
#Gano B
#Juegos ganados por A: 5
#Juegos ganados por B: 6
#Aun no termina
#Juegos ganados por A: 3
#Juegos ganados por B: 7
#Invalido
#Juegos ganados por A: 6
#Juegos ganados por B: 4
#Gano A
p1 = int(input("games won by A: "))
p2 = int(input("games won by B: "))

#IF ITS INVALID
if p1 > 7 or p2 > 7 or ( p1==7 and p2 < 5) or (p2==7 and p1 < 5) or abs(p1-p2) > 2:
    print ("Invalid")
#IF ITS NOT FINISHED
elif (p1 <= 6 and p2 <= 6 ) or (p1==6 and p2==6):
    print ("It's not over yet")
#IF P1 WON
elif (p1 == 6 and p2 <= 4) or (p1 == 7 and p2 == 5) or (p1 == 7 and p2 == 6):
    print ("Won A")

elif (p2 == 6 and p1 <= 4) or (p2 == 7 and p1 == 5) or (p2 == 7 and p1 == 6):
    print ("Won B")