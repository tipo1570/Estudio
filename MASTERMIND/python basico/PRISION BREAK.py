#"prison break el juego"

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
                          "sin familian, sin tiempo y sin vida. es tu destino ")
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


#--------------------------------------------------------------------------------------------------------------------------------------------------------


elif (opc1=="b"):
    print("\n", len(titulo) * "=")
    gun=input("te encierras en la celda con el guardia de seguridad,\n" 
              "pero esto causa que todos los presos te quieran matar\n"
              "te das cuenta que la pistola del policia esta en el suelo\n"
              "A. recoger la pistola del suelo\n"
              "B. dejar la pistola ahi\n")



    print("\n", len(titulo) * "=")
    opc2=input("los presos se acercan cada vez mas a tu celda te quieren\n"
              "muerto, estos intentan forzar la cerradura que haras?\n"
              "A. llamar a mas guardias con la radio del policia\n"
              "B. amenazar a los presos con la pistola del policia"
              "C. detener la puerta con tu cuerpo")

              


















































elif(opc1=="c"):
    input("")


else:
    print("escoge una opcion valida")
    exit()