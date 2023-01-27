titulo = ("\nEste programa sirve para poder escoger tu movil perfecto\n")

print(len(titulo) * "_" + titulo + len(titulo) * "_")

pregunta_1 = input("Que te gusta mas ios o android\n"
                   "I para ios y A para android: ")

if (pregunta_1 == "I"):
    pregunta_2 = input("Tienes dinero?\n(contestar con si o no)")
    if (pregunta_2 == "si"):
        print("tu telefono perfecto es el iphone ultra pro max")
    elif (pregunta_2 == "no"):
        print("tu telefono adecuado es un iphone de segunda mano")
    else:
        print("escoge una opcion valida")
        exit()
elif (pregunta_1 == "A"):
    pregunta_2 = input("Tienes dinero?\n(contestar con si o no)")
    if (pregunta_2 == "si"):
        pregunta_3 = input("te importa la camara?")
        if (pregunta_3 == "si"):
            print("Tu telefono adecuado es el google pixel")
        elif (pregunta_3 == "no"):
            print("Tu telefono adecuado es un buen android calidad precio")
        else:
            print("escoge una opcion valida")
            exit()
    elif (pregunta_2 == "no"):
        print("Tu telefono adecuado es un telefono chino de 100 euros")
    else:
        print("escoge una opcion valida")
        exit()
else:
    print("escoge una opcion valida")
    exit()
