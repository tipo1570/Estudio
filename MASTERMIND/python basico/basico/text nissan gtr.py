titulo=("Eres un  verdadero fan de los nissan GTR,vamos a ver cuanto sabes. ")

puntuacion=(0)

print(titulo + "\n" + len(titulo)* "-")

pregunta_1=input("-por favor contestar las preguntas con letra minuscula-\n"
                 "\npregunta 1 \n "
                 "Que motor lleva un nissan gtr r35\n"
                    "A. Un V6 twin turbo\n"
                    "B. Un motor en linea de 6 cilindros twin turbo\n"
                    "C. Un motor V8 naturalmente aspirado\n"
                    "R/ ")

if (pregunta_1 =="a"):
    print("respuesta correcta, mira ese potencial ")
    puntuacion+=10
elif (pregunta_1 =="b"):
    print("Casi, ese motor fue usado en la anterior generacion, no en la actual")
    puntuacion+=5
elif (pregunta_1 =="c"):
    print ("Estas LOCO, no es un americano es un japo")
    puntuacion+=0
else:
    print("escoje una opcion valida")

    exit()


pregunta_2=input("\npregunta 2\n"
                 "Que traccion es el nissan gtr?\n"
                     "A. AWD\n"
                     "B. FR\n"
                     "C. FD\n"
                     "R/ ")

if(pregunta_2 =="a"):
    print("Si que eres bueno, efectivamente es traccion AWD")
    puntuacion+=10
elif(pregunta_2 =="b"):
    print("Si que te gustan los americanos, respuesta incorrecta")
    puntuacion+=0
elif(pregunta_2 =="c" ):
    print("Enserio? acaso piensas que es un honda")
    puntuacion+=5
else:
    print("escoge una opcion valida")

    exit()


pregunta_3=input("\n pregunta 3\n"
                 "En que año salio el nissan gtr r35?\n"
                 "A. En el año 2005\n"
                 "B. En el año 2008\n"
                 "C. En el año 2009\n"
                 "R/ ")

if(pregunta_3== "a"):
    print("si que eres malo, salio 4 años despues\n")
    puntuacion+=0
elif(pregunta_3== "b"):
    print("casi, ese año salio para japon. te doy puntos por el intento\n")
    puntuacion+=5
elif(pregunta_3== "c"):
    print("Correcto en ese año salio para todo el mundo el nissan gtr r35\n")
    puntuacion+=10
else:
    print("escoge una opcion valida")

    exit()

if(puntuacion >=25):
    print("*Senpaiiii detentivamente eres un fan del gtr tu puntuacion es {}*".format(puntuacion))
elif(puntuacion >= 15):
    print("*eres bueno pero te falta algo, te falta odio sasuke. tu puntuacion es {}*".format(puntuacion))
elif(puntuacion>= 5 ):
    print("*eres perveso perversamente malo, sigue estudiando y vuelve. tu puntuacion es {}*".format(puntuacion))
else:
    print("*me das lastima prime*")

print("maxima puntacion posible: 30")

exit()