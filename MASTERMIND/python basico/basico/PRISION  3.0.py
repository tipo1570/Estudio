#"prison break el juego"
#trabajo realizado por nicolas chiquiza rippe

import random

titulo="-Bienvenido al juego prison break, cada decision que tomes sera crucial para\n" \
       "escapar y continuar con la aventura, Mira todas las opciones y tal vez sobrevivas-\n"

print("\n",titulo+"\n",len(titulo)*"=",
      "\n\nRECUERDE QUE PARA SELECCIONAR UNA RESPUESTA DEBE HACERLO EN LETRA MINISCULA"
      " EJEMPLO: a","\n\n",len(titulo)*"=")
print("AQUI ES DONDE COMIENZA LA AVENTURA" "\n", len(titulo) * "=")

opc1=input(
           "\nTe hayas en la prision despues de haber sido culpado de crimenes que jamas cometiste\n"
      "decidido a escapar para buscar a tu familia inicias una revuelta en la prision con el\n"
      "fin de escapar de la prision. Estas encerrado en tu celda cuando ves a varios reclusos\n"
      "luchando contra un guardia de seguridad, El guardia de seguridad cae y los reclusos se \n"
      "abalanzan contra el.\n"
      "A. No hacer nada.\n"
      "B. Ayudar al guardia y meterlo a tu celda.\n"
      "C. Atacar al guardia como el resto.\n"
      "ELIGE: ")

if (opc1=="a"):
    print("\n", len(titulo) * "=")
    opc2=input("\nLos reclusos acaban con el pobre guardia, este muere suplicando que le ayudes\n"
          "El alboroto llama la atencion de mas guardias que van a acabar con los reclusos,\n"
          "para tu fortuna el guardia caido tiene las llaves de tu celda....\n"
               "A. No hacer nada.\n"
               "B. Intentar arrastrar el cuerpo para obtener las llaves.\n"
               "C. Tomar el arma del guardia y volar la cerradura.\n"
               "ELIGE: ")
    if(opc2=="a"):
        print("\n",len(titulo)*"=")
        opc3=input("\nLos guardias que entraron fuertemente armados, inmovilizaron a todos los presos\n"
                   "que encontraron fuera de su celda, y este grupo de guardias al ver a su compañero\n"
                   "muerto empezaron a interregar a todos los presos....\n"
                   "A. No hacer nada.\n"
                   "B. Delatar a los culpables.\n"
                   "C. Incubrir a los culpables.\n"
                   "ELIGE: ")
        if(opc3=="a"):
            print("\n", len(titulo) * "=")
            print("\nLos guardias acaban con la revuelta y meten a todos los presos a las celdas y se abre una\n"
                       "una investigacion con el fin de buscar a los responsables de la revuelta, Como no intentaste\n"
                       "escapar no te acusan de nada y antes te dan una reduccion de tu condena. despues de varios\n"
                       "meses de investigacion se dan cuenta que no realizaste ningun crimen y te dejan libre."
                       "que suerte tienes. ")
            exit()

        elif(opc3=="b"):
            print("\n", len(titulo) * "=")
            print("\nGracias a tu informacion los policias encontraron a los culpables,Los policias acaban con la\n"
                  "revuelta.\n"
                  "gracias a tus buenas aciones se busca revisar tu caso, en este proceso se dan cuenta que no has\n"
                  "hecho nada malo,sales de la prision de la mejor manerena posible de la prision\n ")
            exit()

        elif(opc3=="c"):
            print("\n", len(titulo) * "=")
            opc4=input("\nLes relatas una historia a los policias donde los responsables huyeron del lugar,"
                       " cuando estos\n""estaban al lado tuyo, los policias se van a investigar a otro lado y devuelven"
                       " a los presos a sus\nceldas, estos se vuelven a escapar facilmente y te ayudan a escapar....\n"
                       "A. huir con los reclusos\n"
                       "B. Escapar solo\n"
                       "C. quedarte en tu celda\n"
                       "ELIGE: ")
            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("\nLa policia militar entra a la carcel con el fin de acabar con todos los reclusos que esten fuera\n"
                      "de sus celdas, Estos te encuentran con el grupo de reclusos y disparan a discresion, tu caes"
                      "muerto\n en el patio de la carcel, meses despues se te haya responsable de las revueltas\n"
                      "mueres siendo un sucio criminal.  ese es tu destino ")

            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                opcion_5=input("\nEscoges no huir con los demas, en este momento la policia militar se habia hecho"
                               "cargo de la \n"
                      "situacion y como controlaron la situacion? matando a todos los que estuvieran fuera de sus celdas\n"
                      "Estos acabaron con el grupo de presos que te ayudo a escapar que haras sabiendo que quedan pocos\n"
                      "presos por fuera y los estan masacrando....\n"
                      "A. Re ingresar en mi celda\n"
                      "B. Coger el uniforme de algun oficial muerto\n"
                      "ELIGE: ")
                if(opcion_5=="a"):
                    print("\n", len(titulo) * "="
                          "\nTe quedas en la celda esperando a los guardias de seguridad para que te interrogen \n"
                          "Estos se percatan que la cerradura de la celda habia sido dañada ya que para poder abrir\n"
                          "la cerradura se tiene que insertar la llave de manera especial. Este hecho se anota y se \n"
                          "abre una investigacion en la se te haya culpable de intentar escapar. Gracias a esto se te\n"
                          "añaden 5 años de condena")

                elif(opcion_5=="b"):
                    print("\n", len(titulo) * "=")
                    print("\nle quitas el uniforme a un oficial y huyes facilmente de la prision,con tu uniforme\n"
                          "vas en busca de tu familia y logras encontrala aunque este encuentro no dura demasiado\n"
                          "ya que eres buscado por todo el pais, tu nueva vida sera huir de tus problemas\n"
                          "sin familia, sin tiempo y sin vida. es tu destino ")
                else:
                    print("escoge una opcion valida")
                    exit()
            elif(opc4=="c"):
                print("\n", len(titulo) * "=")
                print("\nLa policia militar llega a la escena y acaban con todos los criminales que encontraron por\n"
                      "fuera de sus celdas despues de la limpieza estos empiezan a interrogar a los demas reclusos\n"
                      "se te a haya culpable de incubrir a los reclusos en el asesinato del guardia por esto se te\n"
                      "añaden 5 años a la condena que ya tenias y como si no fuera suficiente te cambian a una "
                      "prision\nde maxima seguridad ")
            else:
                print("escoge una opcion valida")
                exit()
        else:
            print("escoge una opcion valida")
            exit()



    elif(opc2=="b"):
        print("\n", len(titulo) * "=")
        opc3=input("\nTienes exito arrastrando el cuerpo del policia a tu celda logras encontrar las llaves de todas las\n"
              "celdas pero en este momento entra un gran grupo de guardias que te ven con el cadaver en tus manos\n"
              "que haras? ....\n"
              "A. Escapar rapidamente con las llaves\n"
              "B. Disparar con el arma de dotacion del policia muerto\n"
              "C. Mentir, decir que le prestas primeros auxilios\n"
              "ELIGE: ")
        if(opc3=="a"):
            print("\n", len(titulo) * "=")
            opc4=input("\nLogras salir de tu celda rapidamente y te reunes con los presos que tambien lograron escapar de\n"
                  "sus celdas en este momento los guardias que entraron al pabeyon empiezan a atacar a los presos\n"
                  "con bolillos y escudos antidisturbios la gran mayoria de presos va a atacar a los policicas....\n"
                  "A. Atacar a los policias como los demas presos\n"
                  "B. Huir del lugar\n"
                  "C. Entregarse a los policias\n"
                  "ELIGE: ")
            if(opc4=="a"):
                print("\n", len(titulo) * "=","\n"
                 "\nlos policicas acaban facilmente con la revueta con sus gases lacrimogenos y sus pistolas traumaticas\n"
                 "Todos los presos que resultan involucrados en las protestas reciben una extension de su condena.\n"
                 "se abre una investigacion con el fin de hallar a los culpables de la muerte del oficial como\n"
                 "manipulaste el cadaver del oficial tambien se te hay culpable de colaborar en el asesinato del\n"
                 "oficial y se te imputan varios cargos asi alargando tu condena")
            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                opc5=input("\ncon todo el revuelo alcanzas a huir a los depachos, ya estas cerca de la salida.\n"
                      "pero en este momento ves como entra la policia militar fuertemente armada para hacerse\n"
                      "cargo de la situcion, alcanzas a escoderte dentro de los casilleros...\n"
                           "A. seguir escondido\n"
                           "B. huir del lugar cuando pase la polica militar\n"
                           "C. entregarse a los policias\n"
                           "ELIGE: ")
                if(opc5=="a"):
                    print("\n", len(titulo) * "=")
                    opc6=input("Logras esconderte por varias horas en donde los policias estan ocupados con los presos\n"
                          "re organizandolos en diferentes celdas y otros desaciendose de evidencia de la brutalidad\n"
                          "policiaca...\n"
                               "A. huir con un uniforme de policia\n"
                               "B. Escapar en el clasico camion\n"
                               "ELIGE: ")
                    if(opc6=="a"):
                        print("\n", len(titulo) * "="
                              "\nConsigues facilmente un uniforme de policia ya que estas en sus despacho, logras\n"
                              "escapar de la prision por la puerta principal y sin ninguna sospecha, despues de\n"
                              "varios dias se te empieza a buscar por todo lado y se inculpa de varios cargos\n"
                              "como el asesinato de oficiales y haber orquestado las protestas, tu vida ahora\n"
                                                  "sera escapar de la policia")
                    elif(opc6=="b"):
                        print("\n", len(titulo) * "=",
                              "\nsales de la prision con el tipico camion de basura, terminas en el vertedero\n"
                              "y con todo el revuelo se te da por muerto ya que en la prision hay mas muertos\n"
                              "que personas logras huir depues de una larga travesia y ahora eres invisible para\n"
                              "el estado")
                    else:
                        print("esoge una opcion valida")
                        exit(':)')
            elif(opc4=="c"):
                print("\n", len(titulo) * "=",
                      "Te entregas a la policia militar y estos te dan una paliza por estar fuera de la celda\n"
                      "luego de varios dias buscas denunciar a estos por maltrato pero esto no prospera ya que\n"
                      "estabas fuera de tu celda, se hacen varias investigaciones en tu caso y no te hayan culpable\n"
                      "de nada por esto sales dela carcel sin mayor esfuerzo (tal vez no hacer nada hubiera sido "
                      "mejor)")
            else:
                print("esoge una opcion valida")
                exit()


        elif(opc3=="b"):
            print("\n", len(titulo) * "=")
            opc4=input("\ndisparas el arma del oficial muerto, los policias que entraron a dispersar los disturbios\n"
                       "solo traian armas traumaticas y escudos antidisturbios. estos salen huyendo del lugar, los\n"
                       "presos cebran esto y salen al patio para luego llegar a los despachos y salir de la prision\n"
                       "por la puerta principal...."
                       "\A. ir con el resto de presos\n"
                       "\B. ir solo\n"
                       "\ELIGE: ")
            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("\nVas con el resto de los presos, apenas entran al patio ven como entra un grupo de polica\n"
                      "militar el cual contiene a todos los presos y restablecen el orden en la prision, a los presos\n"
                      "que participaron en las revueltas se les imputan varios cargos y se les extiende la condena\n"
                      "incluyendote a ti pasas 13 años en prision, por algunos crimenes que no cometiste y otros\n"
                      "tantos que si cometiste")
            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                print("logras salir de la prision llendo por la direccion opuesta en la cual todos los demas van\n"
                      "sales de la prision en un camion de basura, depues de varios dias se te empieza a buscar,"
                      "tu vida ahora sera huir de la policia")
            else:
                print("escoge una opcion valida")
                exit()



        elif(opc3=="c"):
            print("\n", len(titulo) * "=")
            opc4=input("\nLos policias ven supuestamente le das primeros auxilios y estos se concentran en los\n"
                       "presos que estan por fuera de las celdas.Los policias acaban con la revuelta y se te da\n"
                       "una reduccion de tu condena por supuestamente prestar primeros auxilios al oficial\n"
                       "que suertudo eres amigo")
        else:
            print("Escoge una opcion valida")
            exit(":)")




    elif(opc2=="c"):
        print("\n", len(titulo) * "=")
        opcion_3=input("\nAl destruir la cerradura esta se abre despues de forcejear, pero el sonido del disparo llama\n"
              "la atencion de todos los guardias de la zona, estos van a investigar\n"
              "A. Huir del lugar con los demas presos\n"
              "B. Tomar el uniforme del guardia muerto\n"
              "C. Esconderse\n"
              "ELIGE: ")
        if(opcion_3=="a"):
            print("\n", len(titulo) * "=")
            print("huyes del lugar con los demas presos pero en este momento ves como entra la policia militar\n"
                  "y acaba con las revueltas del lugar, a los presos que participan de estas se les imputa\n"
                  "varios cargos y extensiones de sus diferentes condenas pasas varios años en la prision\n"
                  "sales y te reencuentras con tu familia")
        elif(opcion_3=="b"):
            print("\n", len(titulo) * "=")
            opc4=input("\ntomas el uniforme del guardia pero un oficial nota algo extraño en ti este te pide\n"
                       "tu carnet de identificacion....\n"
                       "A. Seguir como si nada\n"
                       "B. decir que lo perdiste\n"
                       "ELIGE: ")
            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("te das cuenta que el guardia le hablaba a alguien mas y logras salir de la prision por la\n"
                      "puerta principal, ahora eres buscado por todo el estado eres un profugo pero por lo menos ves\n"
                      "a tu familia")
            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                print("El policia se extraña ya que este no te hablaba a ti, luego acto seguido te interrogan y\n"
                      "rapidamente se dan cuenta que no eres un oficial,como tomaste el arma y el uniforme del oficial\n"
                      "muerto estos suponen que eres el responsable de todo esto y se te imputan varios cargos\n"
                      "asi pasando el resto de tu vida en la carcel")
            else:
                print("escoge una opcion valida")
                exit()
    else:
        print("escoge una opcion valida")
        exit()

#trabajo realizado por nicolas chiquiza rippe
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


elif (opc1=="b"):
    print("\n", len(titulo) * "=")
    gun=input ("te encierras en la celda con el guardia de seguridad,\n"
               "pero esto causa que todos los presos te quieran matar\n"
               "puedes recoger la pistola del policia que esta en tu celda\n"
               "¿que haces?\n"
               "A. recoger el arma\n"
               "B. dejar el arma en el suelo\n"
               "ELIGE: ")


    if (gun=="a"):
        inv_gun = True

    elif(gun=="b"):
        inv_gun = False


    print("\n", len(titulo) * "=")
    opc2=input("Los presos estan enfurecidos contigo y piensan entrar a tu celda\n"
               "a como de lugar, estos estan cada vez mas cerca de la puerta por\n"
               "A. Amenazar a los presos con la pistola del policia\n"
               "B. Llamar a guardias de refuerzo con el radio del policia\n"
               "C. Detener la puerta con tu cuerpo\n"
               "ELIGE: ")



    if(opc2=="a"):



        if (gun=="a" and inv_gun == True):
            print("\n", len(titulo) * "=")
            print("logras disuadir a los presos con exito, mientras llegan los refuerzos\n"
                  "el policia sirve como testigo de tu buena fe, por esto mismo se busca\n" 
                  "mirar tu caso lograste salir de la carcel de una de las mejores maneras,\n" 
                  "pero la mafia no olvidara lo que has hecho\n")
        

        elif(gun=="b" and inv_gun == False):
            print("\n", len(titulo) * "=")
            print("al dejar el arma tirada en el suelo uno de los presos logra recoger el arma\n"
                  "del suelo y te acribilla a ti y al oficial no lograste salir de la carcel, \n"
                  "meses despues se investigo y si dio la conclusion  de que eras inocente de lo\n"
                  "que se te acusaba quedaras en la memoria como un martir\n")

        
        else:
           print("escoge una opcion valida")
           exit()




    elif(opc2=="b"):
            print("\n", len(titulo) * "=")
            opc3=input("los presos estan cada vez mas cerca de la puerta y estos\n"
                       "empiezan a forzar la cerradura y esta cede cada vez mas.\n"
                       "A. amenazar a los presos con la pistola del policia\n"
                       "B. no hacer nada\n"
                       "ELIGE: ")


            if(opc3=="a"):
               if (gun=="a" and inv_gun == True):
                print("logras disuadir a los presos con exito, mientras llegan los\n" 
                      "refuerzos el policia sirve como testigo de tu buena fe, por\n"
                      "esto mismo se busca mirar tu caso lograste salir de la carcel\n"
                      "de una de las mejores maneras, pero la mafia\n"
                      "no olvidara lo que has hecho\n")



               elif(gun=="b" and inv_gun == False):
                print("al dejar el arma tirada en el suelo uno de los presos logra recoger\n"
                      "el arma del suelo y te acribilla a ti y al oficial no lograste salir\n" 
                      "de la carcel, meses despues se investigo y si dio la conclusion  de\n"
                      "que eras inocente de lo que se te acusabaquedaras en la memoria como un martir\n")


               else:
                    print("escoge una opcion valida")
                    exit()
            
           
            elif(opc3=="b"):
                print("los presos intentan forzar la cerradura, en el momento en que estos la logran\n"
                      "abrir, entran los policias de refuerzo que pediste, el policia que ayudaste aboga\n"
                      "por ti y se busca mirar tu caso, se halla que no eres culpable de nada y\n"
                      "a las semanas sales de prision de la mejor manera")
            
            
            else:
               print("escoge una opcion valida")
               exit()


    elif(opc2=="c"):

            if (gun=="a" and inv_gun == True):
                print("\n", len(titulo) * "=")
                opc3=input("los presos no pueden forzar la cerradura gracias a ti ya\n" 
                           "que tu cuerpo la bloquea, pero estos empiezan a pegarte\n"
                           "con patadas e incluso alguno intenta agredir con armas blancas\n"
                           "A. Disparar a los presos\n"
                           "B. Amenzar con disparar\n"
                           "ELIGE: ")
                
                
                if(opc3=="a"):
                    print("\n", len(titulo) * "=")
                    print("los presos se asustan y huyen de la celda, el alboroto trajo a los policias de refuerzo\n"
                          "el policia que salvaste da cuenta de tu buena fe y te ayuda para que puedas salir de la carcel\n" 
                          "pero unos dias antes de tu salida los presos a los que les disparaste cobran venganza.  mueres en\n"
                          "la carcel, tan cerca pero tan lejos....\n")
                
                
                elif(opc3=="b"):
                    print("\n", len(titulo) * "=")
                    print("los presos se asustan y huyen de la celda, el alboroto trajo a los policias de refuerzo\n" 
                          "el policia que salvaste da cuenta de tu buena fe y te ayuda para que puedas salir de la carcel\n"
                          "sales de la carcel intacto y en busca de tu familia pero la mafia no olvida lo que hiciste\n")
                
                
                else:
                    print("escoge una opcion valida")
                    exit()

           
            
            
            elif(gun=="b" and inv_gun == False):
                print("\n", len(titulo) * "=")
                opc3=input("los presos no pueden forzar la cerradura gracias a ti ya\n" 
                           "que tu cuerpo la bloquea, pero estos empiezan a pegarte\n"
                           "con patadas e incluso alguno intenta agredir con armas blancas\n"
                           "A. mantenerte en la puerta apesar de todo\n"
                           "B. quitarte de la puerta\n "
                           "ELIGE: ")
                

                if(opc3=="a"):
                    print("\n", len(titulo) * "=")
                    print("los presos no pueden entrar en la celda gracias a ti, lograste darle tiempo suficiente a los refuerzos\n"
                          "pero estas mal herido el policia nunca olvidara lo que hiciste por el, el es testigo en la investigacion\n" 
                          "que se hace y por esto mismo se te reduce tu condena y eres condenado a casa por carcel\n")



                elif(opc3=="b"):
                    print("\n", len(titulo) * "=")
                    print("los presos logran entrar en la celda, ellos te empiezan a agredir y quedas muy mal herido pero\n"
                          "en ese momento entran los policias de refuerzo y te sacan de alli junto con el policia caido\n"
                          "el policia nunca olvidara lo que hiciste por el, el es testigo en la investigacion\n"
                          "que se hace y por esto mismo se te reduce tu condena y eres condenado a casa por carcel\n")
    
                else:
                    print("escoge una opcion valida")
                    exit()
            

            else:
               print("escoge una opcion valida")
               exit()

    
    else:
        print("escoge una opcion valida")
        exit()
#trabajo realizado por nicolas chiquiza rippe
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                       
elif(opc1=="c"):
    print("\n", len(titulo) * "=")
    opc2=input("procedes a atacar al guardia con el resto de los presos el guardia queda\n"
          "muy mal herido y te pide que le perdones la vida, los demas presos se retiran\n"
          "y dejan esta decicion en tus manos\n"
          "A. Dejar vivir al guardia\n"
          "B. Asesinar al guardia\n"
          "C. No hacer nada\n"
          "ELIGE: ")
    
    
    if(opc2=="a"):
        print("\n", len(titulo) * "=")
        opc3=input("uno de los presos te empieza a regañar por no asesinar al policia\n"
                   "en ese momento el toma la decision que no fuiste capaz de tomar tu\n"
                   "y el asesina al policia, en este momento entran mas policias\n"
                   "A. Robar la tarjeta de seguridad\n"
                   "B. Robar la pistola\n"
                   "C. Robar el juego de llaves del agente\n"
                   "ELIGE: ")
            
        if(opc3=="a"):
            print("\n", len(titulo) * "=")
            opc4=input("Robas la tarjeta con exito, los agentes empiezan a reducir a los presos\n"
                       "y te encuentras en el medio de la batalla campal....\n"
                       "A. Enfrentar a los guardias\n"
                       "B. Huir mientras el resto se enfrenta contra ellos\n"
                       "ELIGE: ")


            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("los guardias logran reducir a todos los reos con sus armas de dotacion\n"
                      "incluyendote a ti, todos los reos son investigados y en la mayoria de los\n"
                      "casos se envian a diferentes prisiones y se les aumenta la condena y tu no eres\n"
                      "la exepcion.\n")
             


            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                opc5=input("huyes a una sala continua y luego te encuentras con un corredor bastante\n" 
                           "extenso pero ves que hay dos puertas en este, una de estas puertas de la\n"
                           "sala de descanso de los oficiales y la ultima puerta es la armeria\n"
                           "A. seguir por el pasillo\n" 
                           "B. entrar en la sala de descanso de los oficiales\n"
                           "C. entrar en la armeria\n"
                           "ELIGE: ")
                
                if(opc5=="a"):
                    print("\n", len(titulo) * "=")
                    opc6=input("sigues el pasillo hasta una sala, te das cuenta que esta es la\n"
                               "recepcion de la prision, ves que hay personas civiles y varios agentes\n"
                               "evacuandolas, cerca de esta recepcion hay una puerta con un lector de tarjetas\n"
                               "A. usar la tarjeta para abrir la puerta\n"
                               "B. intentar hacerse pasar por un civil\n"
                               "ELIGE: ")


                    if(opc6=="a"):
                        clave=(random.randint(50,100))
                        print("\n", len(titulo) * "=")
                        opc7=input("te das cuenta que la puerta de te pide un codigo de aceso aparte de\n"
                                    "la tarjeta para poder entrar, despues de varios intentos esta te un\n"
                                    "recordatorio\n"

                                    "El pin se cambia segun la seccion y la tarjeta de acceso.\n" 

                                    "estas en la seccion 37 de la prision y el numero de la tarjeta es\n"
                                    "{}, los intentos se te acaban y el terminaal se va a bloquear\n"

                                    "A. juntar los dos numeros\n"
                                    "B. multiplicar los dos numeros\n"
                                    "C. sumar los dos numeros\n"
                                    "ELIGE: ".format(clave))


                        if(opc7=="a"):
                            print("\n", len(titulo) * "=")
                            print("la cerradura se bloqueo y salto la alarma de esta esto alerta a\n" 
                                  "todos los policias que estan en la sala de al lado, estos te\n" 
                                  "atrapan intentando forzar la cerradura, se te suman varios años\n"
                                  "a tu condena, no lograste escapar\n")


                        elif(opc7=="b"):
                            print("\n", len(titulo) * "=")
                            opercaion_a=(clave*37)
                            operacion_b=(clave*36)
                            opercaion_c=(clave*26)
                            opc8=input("la cerradura te pide el resultado de esta operacion\n"
                                       "A. {}\n"
                                       "B. {}\n"
                                       "C  {}\n"
                                       "ELIGE: "
                                       .format(opercaion_a,operacion_b,opercaion_c))
                            

                            if (opc8=="a"):
                                 print("\n", len(titulo) * "=")
                                 print("La cerradura se abrio con exito, entras en una sala\n"
                                       "donde te das cuenta que hay varios casilleros y ropa\n"
                                       "de persona civil, te cambias la ropa y fuerzas un casillero\n"
                                       "y tienes la buena suerte de encontrar las llaves de un vehiculo\n"
                                       "huyes de la prision con el vehiculo.")
                            
                            elif(opc8=="b"):
                                 print("\n", len(titulo) * "=")
                                 print("la cerradura se bloqueo y salto la alarma de esta esto alerta a\n" 
                                       "todos los policias que estan en la sala de al lado, estos te\n" 
                                       "atrapan intentando forzar la cerradura, se te suman varios años\n"
                                       "a tu condena, no lograste escapar\n")

                            
                            elif(opc8=="c"):
                                 print("\n", len(titulo) * "=")
                                 print("la cerradura se bloqueo y salto la alarma de esta esto alerta a\n" 
                                       "todos los policias que estan en la sala de al lado, estos te\n" 
                                       "atrapan intentando forzar la cerradura, se te suman varios años\n"
                                       "a tu condena, no lograste escapar\n")

                            else:
                                print("escoge una opcion valida")
                                exit()



                    elif(opc6=="b"):
                        print("\n", len(titulo) * "=")
                        print("los policias te reconocen y reconocen tu uniforme de la prision\n"
                              "te capturan sin mediar palabras. se te suman varios años\n"
                              "a tu condena, no lograste escapar\n")

                    

                    else:
                        print("escoge una opcion valida")
                        exit()



                elif(opc5=="b"):
                    print("\n", len(titulo) * "=")
                    print("entras a la sala de los oficiales te percatas que esta esta totalmente\n"
                          "vacia mientras escuchas un gran ruido en la armeria, te escabulles por\n"
                          "la salida de emergecia del edifico y logras salir con exito de la carcel\n"
                          "Felicidades has logrado escapar de la prision pero eres el mas buscado\n"
                          "en el pais por todas tus acciones\n")
                
                elif(opc5=="c"):
                    print("\n", len(titulo) * "=")
                    print("entras en la armerria pero en ese instante te das cuenta que hay varios\n"
                          "oficiales armadados que se alistan para entrar a la accion, todos te ven\n" 
                          "entrar a la sala y te inmovilizan de inmediato. se te imputan varios cargos\n" 
                          "y tu intento de escape de la prision queda en el olvido\n")
                
                else:
                    print("Escoge una opcion valida")
                    exit()



            else:
                print("Escoge una opcion valida")
                exit()
            
             
 

        elif(opc3=="b"):
            print("\n", len(titulo) * "=")
            opc4=input("Robas la pistola con exito, los agentes empiezan a reducir a los presos\n"
                       "y te encuentras en el medio de la batalla campal....\n"
                       "A. Enfrentar a los guardias\n"
                       "B. Huir mientras el resto se enfrenta contra ellos\n"
                       "ELIGE: ")


            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("los policias reprenden a los reos con porras y tasears en eso\n"
                      "momento tu disparas contra ellos hieres a uno de los policias\n" 
                      "pero esto causa que el resto use sus armas de dotacion contra ti\n"
                      "mueres en la revuelta, no lograste huir de prision.....\n")
             

            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                opc5=input("huyes a una sala continua y luego te encuentras con un corredor bastante\n" 
                           "extenso pero ves que hay dos puertas en este, una de estas puertas de la\n"
                           "sala de descanso de los oficiales y la ultima puerta es la armeria\n"
                           "A. seguir por el pasillo\n" 
                           "B. entrar en la sala de descanso de los oficiales\n"
                           "C. entrar en la armeria\n"
                           "ELIGE: ")
                
                
                
                if(opc5=="a"):
                    print("\n", len(titulo) * "=")
                    opc6=input("siegues por el pasillo a una sala, te das cuenta que esta es la recepcion de la prision y justo\n" 
                               "despues de todo esto esta la salida de la prision, pero te detienes en seco al ver que hay\n" 
                               "varios civiles que pensaban hacer visitas a sus seres queridos y un solo guardian acompañandolos\n"
                               "A. quitarte la camisa e intentar pasar desapercibido"
                               "B. amenazar a todos los presentes con la pistola"
                               "ELIGE: ")
                    

                    if(opc6=="a"):
                        print("\n", len(titulo) * "=")
                        print("logras pasar entre la multitud que hay en la recepcion pero a la\n"
                              "salida de la prision te topas con un equipo de asalto a fueras de\n" 
                              "la prision, estos te requisan y te encuentran el arma de dotacion\n"
                              "eres detenido inmediatamente. esta ahi quedo tu intento de escape\n"
                              "de la prision.")
                    

                    elif(opc6=="b"):
                        print("\n", len(titulo) * "=")
                        print("logras persuiadir a todos los presentes en la sala pero te das cuenta\n" 
                              "que a las afueras del resinto hay un equipo S.W.A.T listo para entrar\n" 
                              "el alboroto hace que estos apresuren su operacion, estos te abaten\n" 
                              "y mueres a las puertas de la libertad\n")
                    
                    else:
                        print("escoge una opcion valida")
                        exit()


                elif(opc5=="b"):
                    print("\n", len(titulo) * "=")
                    print("entras a la sala de los oficiales te percatas que esta esta totalmente\n"
                          "vacia mientras escuchas un gran ruido en la armeria, te escabulles por\n"
                          "la salida de emergecia del edifico y logras salir con exito de la carcel\n"
                          "Felicidades has logrado escapar de la prision pero eres el mas buscado\n"
                          "en el pais por todas tus acciones")
                
                elif(opc5=="c"):
                    print("\n", len(titulo) * "=")
                    print("entras en la armeria pero en ese instante te das cuenta que hay varios\n" 
                          "oficiales armadados que se alistan para entrar a la accion, todos te ven\n" 
                          "entrar a la sala y te inmovilizan de inmediato. se te imputan varios cargos\n" 
                          "y tu intento de escape de la prision queda en el olvido\n")
                
                else:
                    print("Escoge una opcion valida")
                    exit()



            else:
                print("Escoge una opcion valida")
                exit()
            
        

        elif(opc3=="c"):
            print("\n", len(titulo) * "=")
            opc4=input("Robas las llaves con exito, los agentes empiezan a reducir a los presos\n"
                       "y te encuentras en el medio de la batalla campal....\n"
                       "A. Enfrentar a los guardias\n"
                       "B. Huir mientras el resto se enfrenta contra ellos\n"
                       "ELIGE: ")


            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("los guardias logran reducir a todos los reos con sus armas de dotacion\n"
                      "incluyendote a ti, todos los reos son investigados y en la mayoria de los\n"
                      "casos se envian a diferentes prisiones y se les aumenta la condena y tu no eres\n"
                      "la exepcion.\n")
             


            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                opc5=input("huyes a una sala continua y luego te encuentras con un corredor bastante\n" 
                           "extenso pero ves que hay dos puertas en este, una de estas puertas de la\n"
                           "sala de descanso de los oficiales y la ultima puerta es la armeria\n"
                           "A. seguir por el pasillo\n" 
                           "B. entrar en la sala de descanso de los oficiales\n"
                           "C. entrar en la armeria\n"
                           "ELIGE: ")

                if(opc5=="a"):
                    print("\n", len(titulo) * "=")
                    print("sigues por el pasillo a una sala te das cuenta que esta\n" 
                          "es la recepcion y hay varios civiles siendo evacuados\n" 
                          "por varios agentes estos te ven y te reducen, no pudiste escapar\n"
                          "de prision.")

                elif(opc5=="b"):
                    print("\n", len(titulo) * "=")
                    print("entras a la sala de los oficiales te percatas que esta esta totalmente\n"
                          "vacia mientras escuchas un gran ruido en la armeria, te escabulles por\n"
                          "la salida de emergecia del edifico y logras salir con exito de la carcel\n"
                          "Felicidades has logrado escapar de la prision pero eres el mas buscado\n"
                          "en el pais por todas tus acciones\n")
                
                elif(opc5=="c"):
                    print("\n", len(titulo) * "=")
                    print("entras en la armerria pero en ese instante te das cuenta que hay varios\n" 
                          "oficiales armadados que se alistan para entrar a la accion, todos te ven\n" 
                          "entrar a la sala y te inmovilizan de inmediato. se te imputan varios cargos\n" 
                          "y tu intento de escape de la prision queda en el olvido")
                
                else:
                    print("Escoge una opcion valida")
                    exit()



            else:
                print("Escoge una opcion valida")
                exit()
            




        else:
            print("Escoge una opcion valida")
            exit()


#trabajo realizado por nicolas chiquiza rippe
#--------------------------------------------------------------------------------------



    elif(opc2=="b"):
        print("\n", len(titulo) * "=")
        opc3=input("todos los presos quedan contentos con la ejecucion del polica, pero en ese\n"
                   "momento entran varios policias a la sala\n"
                   "A. Robar la tarjeta de seguridad\n"
                   "B. Robar la pistola\n"
                   "C. Robar el juego de llaves del agente\n"
                   "ELIGE  :")
        
        if(opc3=="a"):
            print("\n", len(titulo) * "=")
            opc4=input("Robas la tarjeta con exito, los agentes empiezan a reducir a los presos\n"
                       "y te encuentras en el medio de la batalla campal....\n"
                       "A. Enfrentar a los guardias\n"
                       "B. Huir mientras el resto se enfrenta contra ellos\n"
                       "ELIGE: ")


            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("los guardias logran reducir a todos los reos con sus armas de dotacion\n"
                      "incluyendote a ti, todos los reos son investigados y en la mayoria de los\n"
                      "casos se envian a diferentes prisiones y se les aumenta la condena y tu no eres\n"
                      "la exepcion.\n")
             


            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                opc5=input("huyes a una sala continua y luego te encuentras con un corredor bastante\n" 
                           "extenso pero ves que hay dos puertas en este, una de estas puertas de la\n"
                           "sala de descanso de los oficiales y la ultima puerta es la armeria\n"
                           "A. seguir por el pasillo\n" 
                           "B. entrar en la sala de descanso de los oficiales\n"
                           "C. entrar en la armeria\n"
                           "ELIGE: ")
                
                if(opc5=="a"):
                    print("\n", len(titulo) * "=")
                    opc6=input("sigues el pasillo hasta una sala, te das cuenta que esta es la\n"
                               "recepcion de la prision, ves que hay personas civiles y varios agentes\n"
                               "evacuandolas, cerca de esta recepcion hay una puerta con un lector de tarjetas\n"
                               "A. usar la tarjeta para abrir la puerta\n"
                               "B. intentar hacerse pasar por un civil\n"
                               "ELIGE: ")


                    if(opc6=="a"):
                        clave=(random.randint(50,100))
                        print("\n", len(titulo) * "=")
                        opc7=input("te das cuenta que la puerta de te pide un codigo de aceso aparte de\n"
                                    "la tarjeta para poder entrar, despues de varios intentos esta te un\n"
                                    "recordatorio\n"

                                    "El pin se cambia segun la seccion y la tarjeta de acceso.\n" 

                                    "estas en la seccion 37 de la prision y el numero de la tarjeta es\n"
                                    "{}, los intentos se te acaban y el terminaal se va a bloquear\n"

                                    "A. juntar los dos numeros\n"
                                    "B. multiplicar los dos numeros\n"
                                    "C. sumar los dos numeros\n"
                                    "ELIGE: ".format(clave))


                        if(opc7=="a"):
                            print("\n", len(titulo) * "=")
                            print("la cerradura se bloqueo y salto la alarma de esta esto alerta a\n" 
                                  "todos los policias que estan en la sala de al lado, estos te\n" 
                                  "atrapan intentando forzar la cerradura, se te suman varios años\n"
                                  "a tu condena, no lograste escapar\n")


                        elif(opc7=="b"):
                            print("\n", len(titulo) * "=")
                            opercaion_a=(clave*37)
                            operacion_b=(clave*36)
                            opercaion_c=(clave*26)
                            opc8=input("la cerradura te pide el resultado de esta operacion\n"
                                       "A. {}\n"
                                       "B. {}\n"
                                       "C  {}\n"
                                       "ELIGE: "
                                       .format(opercaion_a,operacion_b,opercaion_c))
                            

                            if (opc8=="a"):
                                 print("\n", len(titulo) * "=")
                                 print("La cerradura se abrio con exito, entras en una sala\n"
                                       "donde te das cuenta que hay varios casilleros y ropa\n"
                                       "de persona civil, te cambias la ropa y fuerzas un casillero\n"
                                       "y tienes la buena suerte de encontrar las llaves de un vehiculo\n"
                                       "huyes de la prision con el vehiculo.")
                            
                            elif(opc8=="b"):
                                 print("\n", len(titulo) * "=")
                                 print("la cerradura se bloqueo y salto la alarma de esta esto alerta a\n" 
                                       "todos los policias que estan en la sala de al lado, estos te\n" 
                                       "atrapan intentando forzar la cerradura, se te suman varios años\n"
                                       "a tu condena, no lograste escapar\n")

                            
                            elif(opc8=="c"):
                                 print("\n", len(titulo) * "=")
                                 print("la cerradura se bloqueo y salto la alarma de esta esto alerta a\n" 
                                       "todos los policias que estan en la sala de al lado, estos te\n" 
                                       "atrapan intentando forzar la cerradura, se te suman varios años\n"
                                       "a tu condena, no lograste escapar\n")

                            else:
                                print("escoge una opcion valida")
                                exit()



                    elif(opc6=="b"):
                        print("\n", len(titulo) * "=")
                        print("los policias te reconocen y reconocen tu uniforme de la prision\n"
                              "te capturan sin mediar palabras. se te suman varios años\n"
                              "a tu condena, no lograste escapar\n")

                    

                    else:
                        print("escoge una opcion valida")
                        exit()



                elif(opc5=="b"):
                    print("\n", len(titulo) * "=")
                    print("entras a la sala de los oficiales te percatas que esta esta totalmente\n"
                          "vacia mientras escuchas un gran ruido en la armeria, te escabulles por\n"
                          "la salida de emergecia del edifico y logras salir con exito de la carcel\n"
                          "Felicidades has logrado escapar de la prision pero eres el mas buscado\n"
                          "en el pais por todas tus acciones\n")
                
                elif(opc5=="c"):
                    print("\n", len(titulo) * "=")
                    print("entras en la armerria pero en ese instante te das cuenta que hay varios\n"
                          "oficiales armadados que se alistan para entrar a la accion, todos te ven\n" 
                          "entrar a la sala y te inmovilizan de inmediato. se te imputan varios cargos\n" 
                          "y tu intento de escape de la prision queda en el olvido\n")
                
                else:
                    print("Escoge una opcion valida")
                    exit()



            else:
                print("Escoge una opcion valida")
                exit()
            
             
 

        elif(opc3=="b"):
            print("\n", len(titulo) * "=")
            opc4=input("Robas la pistola con exito, los agentes empiezan a reducir a los presos\n"
                       "y te encuentras en el medio de la batalla campal....\n"
                       "A. Enfrentar a los guardias\n"
                       "B. Huir mientras el resto se enfrenta contra ellos\n"
                       "ELIGE: ")


            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("los policias reprenden a los reos con porras y tasears en eso\n"
                      "momento tu disparas contra ellos hieres a uno de los policias\n" 
                      "pero esto causa que el resto use sus armas de dotacion contra ti\n"
                      "mueres en la revuelta, no lograste huir de prision.....\n")
             

            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                opc5=input("huyes a una sala continua y luego te encuentras con un corredor bastante\n" 
                           "extenso pero ves que hay dos puertas en este, una de estas puertas de la\n"
                           "sala de descanso de los oficiales y la ultima puerta es la armeria\n"
                           "A. seguir por el pasillo\n" 
                           "B. entrar en la sala de descanso de los oficiales\n"
                           "C. entrar en la armeria\n"
                           "ELIGE: ")
                
                
                
                if(opc5=="a"):
                    print("\n", len(titulo) * "=")
                    opc6=input("siegues por el pasillo a una sala, te das cuenta que esta es la recepcion de la prision y justo\n" 
                               "despues de todo esto esta la salida de la prision, pero te detienes en seco al ver que hay\n" 
                               "varios civiles que pensaban hacer visitas a sus seres queridos y un solo guardian acompañandolos\n"
                               "A. quitarte la camisa e intentar pasar desapercibido"
                               "B. amenazar a todos los presentes con la pistola"
                               "ELIGE: ")
                    

                    if(opc6=="a"):
                        print("\n", len(titulo) * "=")
                        print("logras pasar entre la multitud que hay en la recepcion pero a la\n"
                              "salida de la prision te topas con un equipo de asalto a fueras de\n" 
                              "la prision, estos te requisan y te encuentran el arma de dotacion\n"
                              "eres detenido inmediatamente. esta ahi quedo tu intento de escape\n"
                              "de la prision.")
                    

                    elif(opc6=="b"):
                        print("\n", len(titulo) * "=")
                        print("logras persuiadir a todos los presentes en la sala pero te das cuenta\n" 
                              "que a las afueras del resinto hay un equipo S.W.A.T listo para entrar\n" 
                              "el alboroto hace que estos apresuren su operacion, estos te abaten\n" 
                              "y mueres a las puertas de la libertad\n")
                    
                    else:
                        print("escoge una opcion valida")
                        exit()


                elif(opc5=="b"):
                    print("\n", len(titulo) * "=")
                    print("entras a la sala de los oficiales te percatas que esta esta totalmente\n"
                          "vacia mientras escuchas un gran ruido en la armeria, te escabulles por\n"
                          "la salida de emergecia del edifico y logras salir con exito de la carcel\n"
                          "Felicidades has logrado escapar de la prision pero eres el mas buscado\n"
                          "en el pais por todas tus acciones")
                
                elif(opc5=="c"):
                    print("\n", len(titulo) * "=")
                    print("entras en la armeria pero en ese instante te das cuenta que hay varios\n" 
                          "oficiales armadados que se alistan para entrar a la accion, todos te ven\n" 
                          "entrar a la sala y te inmovilizan de inmediato. se te imputan varios cargos\n" 
                          "y tu intento de escape de la prision queda en el olvido\n")
                
                else:
                    print("Escoge una opcion valida")
                    exit()



            else:
                print("Escoge una opcion valida")
                exit()
            
        

        elif(opc3=="c"):
            print("\n", len(titulo) * "=")
            opc4=input("Robas las llaves con exito, los agentes empiezan a reducir a los presos\n"
                       "y te encuentras en el medio de la batalla campal....\n"
                       "A. Enfrentar a los guardias\n"
                       "B. Huir mientras el resto se enfrenta contra ellos\n"
                       "ELIGE: ")


            if(opc4=="a"):
                print("\n", len(titulo) * "=")
                print("los guardias logran reducir a todos los reos con sus armas de dotacion\n"
                      "incluyendote a ti, todos los reos son investigados y en la mayoria de los\n"
                      "casos se envian a diferentes prisiones y se les aumenta la condena y tu no eres\n"
                      "la exepcion.\n")
             


            elif(opc4=="b"):
                print("\n", len(titulo) * "=")
                opc5=input("huyes a una sala continua y luego te encuentras con un corredor bastante\n" 
                           "extenso pero ves que hay dos puertas en este, una de estas puertas de la\n"
                           "sala de descanso de los oficiales y la ultima puerta es la armeria\n"
                           "A. seguir por el pasillo\n" 
                           "B. entrar en la sala de descanso de los oficiales\n"
                           "C. entrar en la armeria\n"
                           "ELIGE: ")

                if(opc5=="a"):
                    print("\n", len(titulo) * "=")
                    print("sigues por el pasillo a una sala te das cuenta que esta\n" 
                          "es la recepcion y hay varios civiles siendo evacuados\n" 
                          "por varios agentes estos te ven y te reducen, no pudiste escapar\n"
                          "de prision.")

                elif(opc5=="b"):
                    print("\n", len(titulo) * "=")
                    print("entras a la sala de los oficiales te percatas que esta esta totalmente\n"
                          "vacia mientras escuchas un gran ruido en la armeria, te escabulles por\n"
                          "la salida de emergecia del edifico y logras salir con exito de la carcel\n"
                          "Felicidades has logrado escapar de la prision pero eres el mas buscado\n"
                          "en el pais por todas tus acciones\n")
                
                elif(opc5=="c"):
                    print("\n", len(titulo) * "=")
                    print("entras en la armerria pero en ese instante te das cuenta que hay varios\n" 
                          "oficiales armadados que se alistan para entrar a la accion, todos te ven\n" 
                          "entrar a la sala y te inmovilizan de inmediato. se te imputan varios cargos\n" 
                          "y tu intento de escape de la prision queda en el olvido")
                
                else:
                    print("Escoge una opcion valida")
                    exit()



            else:
                print("Escoge una opcion valida")
                exit()
            




        else:
            print("Escoge una opcion valida")
            exit()
        





    elif(opc2=="c"):
        print("\n", len(titulo) * "=")
        print("los presos te tachan de debil y te comienzan a atacar por tener compasion,\n"
              "pero en ese momento entran varios uniformados a la sala en ese momento\n" 
              "te separan de todos los presos y al oficial herido, el oficicial rinde\n"
              "declaraciones y como este perdio el conocimiento este cree que le ayudaste,\n" 
              "por esto mismo se te da una reduccion a tu condena y se te da casa por carcel\n")



    else:
        print("escoge una opcion valida")
        exit() 






else:
    print("escoge una opcion valida")
    exit()

#trabajo realizado por nicolas chiquiza rippe
#gracias por cambiar mi vida :)
