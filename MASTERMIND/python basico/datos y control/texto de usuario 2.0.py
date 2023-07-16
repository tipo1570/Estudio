#contar las comas los puntos y los espacios



texto_usuario=input("Introducir un texto: ")


espacio = 0 
coma = 0
punto = 0


for letra in texto_usuario:
    if letra == " ":
        espacio += 1

    elif letra == ",":
        coma += 1
    
    elif letra == ".":
        punto += 1



print("Espacios: {}|\nComa: {}|\nPunto: {}|".format(espacio,coma,punto))

