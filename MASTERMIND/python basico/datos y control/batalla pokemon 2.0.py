import os
import random


#batalla pokemon 

#turno de mewtwo


size_life=20


ini_vida_mewtwo=250
ini_vida_dito=240


vida_mewtwo=ini_vida_mewtwo
vida_dito=ini_vida_dito


ataque_dito=None

while vida_mewtwo > 0 and vida_dito > 0:

    #batalla pokemon 



    #turno de mewtwo

    print("turno de mewtwo")
    ataque_mewtwo = random.randint(1,4)
    
    
    
    life_mewtwo=int((vida_mewtwo*20/ini_vida_mewtwo))
    life_dito=int((vida_dito*20/ini_vida_dito))



    if ataque_mewtwo == 1:
        #psiconda
        mensaje=("\nmewtwo uso psiconda")
        print(mensaje,"\n",len (mensaje)*"_" )
        vida_dito -= 15
        
        print("la vida de mewtwo es:"
              "\n[{}{}] {}/{}".format(life_mewtwo*"#"," "*(size_life-life_mewtwo),vida_mewtwo,ini_vida_mewtwo))
        
        print("\n",len (mensaje)*"_" )

        print("la vida de dito es:"
              "\n[{}{}] {}/{}".format(life_dito*"#"," "*(size_life-life_dito),vida_dito,ini_vida_dito))

        
        input("oprime enter....")
        os.system("cls")








    elif ataque_mewtwo == 2:
        #velo sagrado
        mensaje=("\nmewtwo uso velo sagrado")
        
        print(mensaje,"\n",len (mensaje)*"_" )
        
        vida_dito -= 10
        


        print("la vida de mewtwo es:"
              "\n[{}{}] {}/{}".format(life_mewtwo*"#"," "*(size_life-life_mewtwo),vida_mewtwo,ini_vida_mewtwo))
        
        print("\n",len (mensaje)*"_" )

        print("la vida de dito es:"
              "\n[{}{}] {}/{}".format(life_dito*"#"," "*(size_life-life_dito),vida_dito,ini_vida_dito))

        input("oprime enter....")
        os.system("cls")







    elif ataque_mewtwo == 3:
        #aguzar 
        mensaje=("\nmewtwo uso aguzar")

        print(mensaje,"\n",len (mensaje)*"_" )

        vida_dito -= 12
        
        
        
        
        print("la vida de mewtwo es:"
              "\n[{}{}] {}/{}".format(life_mewtwo*"#"," "*(size_life-life_mewtwo),vida_mewtwo,ini_vida_mewtwo))
        
        print("\n",len (mensaje)*"_" )

        print("la vida de dito es:"
              "\n[{}{}] {}/{}".format(life_dito*"#"," "*(size_life-life_dito),vida_dito,ini_vida_dito))

        input("oprime enter....")
        os.system("cls")







    elif ataque_mewtwo == 4:
        #onda mental 
        mensaje=("\nmewtwo uso onda mental")
        
        print(mensaje,"\n",len (mensaje)*"_" )
        
        vida_dito -= 17
        
        print("la vida de mewtwo es:"
              "\n[{}{}]  {}/{}".format(life_mewtwo*"#"," "*(size_life-life_mewtwo),vida_mewtwo,ini_vida_mewtwo))
        
        print("\n",len (mensaje)*"_" )

        print("la vida de dito es:"
              "\n[{}{}] {}/{}".format(life_dito*"#"," "*(size_life-life_dito),vida_dito,ini_vida_dito))
  

        input("oprime enter....")
        os.system("cls")





    
      
    while ataque_dito != "t" and ataque_dito != "p" and ataque_dito != "b" and ataque_dito != "d":

            advertencia=("\nturno de dito")
            
            print(advertencia,"\n",len(advertencia)*"_")



            ataque_dito=input("\nQue ataque deseas realizar:\n"
                              "t. Tranformacion\n"
                              "p. Placaje\n"
                              "b. Bofetada\n"
                              "d. Denscaso\n"
                              "ELIGE: ")
            os.system("cls")
            


            if ataque_dito == "t":
                  mensaje="dito uso transformacion"
                  
                  print(mensaje,"\n",len(mensaje)*"_")
                  
                  vida_mewtwo -= 15

                  print("la vida de mewtwo es:"
                        "\n[{}{}]  {}/{}".format(life_mewtwo*"#"," "*(size_life-life_mewtwo),vida_mewtwo,ini_vida_mewtwo))
        
                  print("\n",len (mensaje)*"_" )

                  print("la vida de dito es:"
                        "\n[{}{}] {}/{}".format(life_dito*"#"," "*(size_life-life_dito),vida_dito,ini_vida_dito))
  

                  input("oprime enter....")
                  os.system("cls")

            
            elif ataque_dito == "p":
                  mensaje="dito uso placaje"
                  
                  print(mensaje,"\n",len(mensaje)*"_")
                  
                  vida_mewtwo -= 18

                  print("la vida de mewtwo es:"
                        "\n[{}{}]  {}/{}".format(life_mewtwo*"#"," "*(size_life-life_mewtwo),vida_mewtwo,ini_vida_mewtwo))
        
                  print("\n",len (mensaje)*"_" )

                  print("la vida de dito es:"
                        "\n[{}{}] {}/{}".format(life_dito*"#"," "*(size_life-life_dito),vida_dito,ini_vida_dito))
  

                  input("oprime enter....")
                  os.system("cls")

            elif ataque_dito == "b":
                  mensaje="dito uso bofetada"
                  
                  print(mensaje,"\n",len(mensaje)*"_")
                  
                  vida_mewtwo -= 12

                  print("la vida de mewtwo es:"
                        "\n[{}{}]  {}/{}".format(life_mewtwo*"#"," "*(size_life-life_mewtwo),vida_mewtwo,ini_vida_mewtwo))
        
                  print("\n",len (mensaje)*"_" )

                  print("la vida de dito es:"
                        "\n[{}{}] {}/{}".format(life_dito*"#"," "*(size_life-life_dito),vida_dito,ini_vida_dito))
  

                  input("oprime enter....")
                  os.system("cls")

            elif ataque_dito == "d":
                  mensaje="dito uso descansar"
                  
                  print(mensaje,"\n",len(mensaje)*"_")
                  

                  print("la vida de mewtwo es:"
                        "\n[{}{}]  {}/{}".format(life_mewtwo*"#"," "*(size_life-life_mewtwo),vida_mewtwo,ini_vida_mewtwo))
        
                  print("\n",len (mensaje)*"_" )

                  print("la vida de dito es:"
                        "\n[{}{}] {}/{}".format(life_dito*"#"," "*(size_life-life_dito),vida_dito,ini_vida_dito))
  

                  input("oprime enter....")
                  os.system("cls")

            ataque_dito=None



print("\n")

      
if life_mewtwo < 0:
      life_mewtwo = 0
    
if life_dito < 0:
      life_dito = 0

if life_mewtwo < 0 or life_mewtwo == 0:
    print("dito gano la guerra!!!!")
    exit()

elif vida_dito < 0 or vida_dito == 0:
    print("Mewtwo gano la pelea!!!")
    exit()