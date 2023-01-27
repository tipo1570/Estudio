print(" este es un juego donde se debe escoger un numero del 1 al 10. ")

int_num= (2)

int_numes=int(input("escoge un numero entre 1 y 10: "))

if int_numes==int_num:
    print("has escogido el numero correcto")
elif int_numes>int_num:
    print("un poco mas abajo")
elif int_numes<int_num:
    print("mas arriba")
else :
    print("y era entre 1 y 10")
