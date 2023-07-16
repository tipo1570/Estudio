#identificar en un texto las letras en mayuscula


import string

texto_usr=input("Introduzca un texto: ")
letra_mayus=0

for letra in texto_usr:
    if letra in string.ascii_uppercase:
        letra_mayus += 1

print("Hay {} letras mayusculas".format(letra_mayus))
