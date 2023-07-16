from random import random
from random import randint
import os
import time

os.system("cls")

print("\n")

titulo = "Guerra pokemon"

print(titulo + "\n" + "-" * len(titulo) + "")


titulo_pikachu = "Turno de pikachu"

titulo_squirtle = "Turno de squirtle"

VIDA_INICIAL_PIKACHU = 80
VIDA_INCIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INCIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    #se desenvuelven los turnos del combate

    #turno de pikachu
    print(titulo_pikachu + "\n" + "-" * len(titulo_pikachu))
    ataque_pikachu = randint(1, 2,)
    if ataque_pikachu == 1:
        print("Pikachu ataca con bola voltio")
        vida_squirtle -= 10
    elif ataque_pikachu == 2:
        print("Pikachu ataca con onda trueno")
        vida_squirtle -= 11

    else:
        print("Pikachu descansa")


    if vida_squirtle < 0:
        vida_squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0


    barra_de_vida_pikachu = int(10 * vida_pikachu / VIDA_INICIAL_PIKACHU)
    barra_de_vida_squirtle = int(10 * vida_squirtle / VIDA_INCIAL_SQUIRTLE)
    print("Pikachu:    [{}]({}/{})".format("*" * barra_de_vida_pikachu, vida_pikachu, VIDA_INICIAL_PIKACHU))
    print("Squirtle:   [{}]({}/{})".format("*" * barra_de_vida_squirtle, vida_squirtle, VIDA_INCIAL_SQUIRTLE))



    print("\n")
    input("Presiona enter para continuar....")


    os.system("cls")


    print(titulo_squirtle + "\n" + "-" * len(titulo_squirtle))
    ataque_squirtle = input(""""Que ataque deseas realizar?
    P - Placaje
    A - Pistola de agua
    B - Burbuja
    D - Descansar
    """"")

    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "D":
        ataque_squirtle = input("""Que ataque deseas realizar?
    P - Placaje
    A - Pistola de agua
    B - Burbuja
    D - Descansar
    """)

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10

    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola de agua")
        vida_pikachu -= 12

    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9

    elif ataque_squirtle == "D":
        print("Squirtle descansa")

    if vida_squirtle < 0:
        vida_squirtle = 0



    os.system("cls")




