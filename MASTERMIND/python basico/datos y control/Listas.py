#lista de compras 

import os
print("Programa para la lista de compra\n")



lista_de_compra = []
input_usuario=None


while True:
    
    input_usuario = input("Que desea comprar?\n"
                          "[Q] oprime para salir\n"
                          "|:")
    os.system("cls")
    
    if input_usuario=="Q":
        break

    elif input_usuario in lista_de_compra:
        print("{} ya esta en la lista".format(input_usuario))
    
    else:
        if input("seguro que quieres meter el siguiente articulo en la lista {} \n"
                  "[S|N] : ".format(input_usuario)) == "S":

                  lista_de_compra.append(input_usuario)
                  os.system("cls")

print("la lista de compra es")
print(lista_de_compra) 


