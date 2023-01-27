from random import randint



vida_pikachu_in= 130

vida_magikart_in= 140


vida_pikachu= vida_pikachu_in

vida_magikart= vida_magikart_in


tamanio_barra=20

while vida_pikachu >0 and vida_magikart >0:
    
    
    
    #empieza la batalla pokemon 



    #turno de pikachu
    print("turno de pikachu")
    ataque_pikachu= randint(1,2)
    if ataque_pikachu== 1:
        #bola voltio
        print("pikachu uso bola voltio")
        vida_magikart -= 10
    

    elif ataque_pikachu==2:
        #impactrueno
        print("pikachu uso impactrueno")
        vida_magikart -= 13


    barra_vida_pica=int(vida_pikachu*tamanio_barra/vida_pikachu_in)
    barra_vida_magi=int(vida_magikart*tamanio_barra/vida_magikart_in)

 
    print("la vida de la pikachu es:\n" 
            "[{}]\n" 
            "la vida de magikart es:\n" 
            "[{}]\n"
            .format(barra_vida_pica*"#",barra_vida_magi*"#"))
    

    input("Oprime enter para continuar...... \n")


    #turno de magikart
    print("turno de magikart")


    ataque_magikart=None

    while ataque_magikart != "p" and ataque_magikart != "b" and ataque_magikart != "a":


        ataque_magikart=input("Que ataque deseas realizar?\n"
                              "(p)lacaje\n"
                              "(b)urbuja de agua\n"
                              "pistola (a)gua\n")

    if ataque_magikart=="p":

        print("magikart ataca con placaje")
        vida_pikachu =- 15
    
    
    
    elif ataque_magikart=="b":

        print("magikart ataca con burbuja de agua")
        vida_pikachu =-13
    

    
    elif ataque_magikart =="a":

        print("magikart ataca con pistola de agua")
        vida_pikachu =- 14

    barra_vida_pica=int(vida_pikachu*100/vida_pikachu_in)
    barra_vida_magi=int(vida_magikart*100/vida_magikart_in)


    
    print(titulo,len(titulo)*'-')
    input("Oprime enter para continuar...... \n")
    input("Enter para continuar...... \n")

if vida_pikachu>vida_magikart:
    print("pikachu gana!")

else:
    print("magikart gana!")







    


        

    












