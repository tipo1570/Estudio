import random




clave=(random.randint(50,100))

opc7=input("te das cuenta que la puerta de te pide un codigo de aceso aparte de\n"
                                    "la tarjeta para poder entrar, despues de varios\n" 
                                    "intentos esta te da un recordatorio\n"

                                    "El pin se cambia segun la seccion y la tarjeta de acceso.\n" 

                                    "estas en la seccion 37 de la prision y el numero de la tarjeta es\n"
                                    "{}, los intentos se te acaban y el terminaal se va a bloquear\n"

                                    "A. juntar los dos numeros\n"
                                    "B. multiplicar los dos numeros\n"
                                    "C. sumar los dos numeros\n"
                                    "ELIGE: ".format(clave))


if(opc7=="a"):

                            print("la cerradura se bloqueo y salto la alarma de esta esto alerta a\n" 
                                  "todos los policias que estan en la sala de al lado, estos te\n" 
                                  "atrapan intentando forzar la cerradura, se te suman varios años\n"
                                  "a tu condena, no lograste escapar\n")


elif(opc7=="b"):

                            opercaion_a=(clave*37)
                            operacion_b=(clave*36)
                            opercaion_c=(clave*26)

                            opc8=input("la cerradura te pide el resultado de esta operacion\n"
                                       "A. {}\n"
                                       "B. {}\n"
                                       "C  {}\n"
                                       .format(opercaion_a,operacion_b,opercaion_c))



else:
    print("f")