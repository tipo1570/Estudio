#lista de compras 


import os


lista_compra= []
entrada_usr=None



while True:
    
    
    entrada_usr=input("OPRIME [Q] para salir\n"
                      "---------------------\n"
                      "Que desea comprar: ")


    if entrada_usr == "q":
        break

    elif entrada_usr == "Q":
        break

    elif entrada_usr in lista_compra:
        print(" EL articulo {} ya esta en la lista".format(entrada_usr))

    
    else: 
        if input("seguro que quieres meter el siguiente articulo en la lista {} \n"
                  "[S|N] : ".format(entrada_usr)) == "S" or "s":

                  lista_compra.append(entrada_usr)
    

    os("cls")
                  
                  


print("la lista de compra es")
print(lista_compra)