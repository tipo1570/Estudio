print(" adivina el numero ")

import random

numeroganador= random.randint (1,10)


print(" debes adivinar un nuemero entre el 1 y el 10 ")
num_selecionado =int(input(" escoje el numero "))
if (num_selecionado == numeroganador ):
    print(" felicidades eres el ganador ")
if (num_selecionado != numeroganador ):
    print(" noooooo sos un pelotudo ")
if (num_selecionado > numeroganador):
    print (" un poco mas abajo")
if (num_selecionado < numeroganador):
    print(" mas arriba weon")
if (num_selecionado == 666 ):
    print (" el numero del diablo")

print(" el numero ganador era {}" .format(numeroganador))