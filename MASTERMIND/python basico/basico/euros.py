#tabla de valores

dolar_euro= 1.16
libra_euro= 0.85


titulo=("\n-este programa sirve para realizar conversiones de divisas\n"
      "\nPOR FAVOR COLOCAR LA RESPUESTA EN MINISCULA\n")
texto="\ninserte la cantidad de dinero que\ndesea convertir de {} a {}: "

print(len(titulo)* "-" +titulo+ len(titulo)* "-")

opc=input("eliga la operacion que desa realizar\n"
      "A.Euros a dolar\n"
      "B.Dolar a euros\n"
      "C.libras a euros\n"
      "D.euros a libras\n"
      "R/ ")


if(opc== "a" ):
    cantidad_de_dinero=float(input(texto.format("euros","dolar")))
    print("la cantidad de dolares es {}".format(cantidad_de_dinero*dolar_euro))

elif(opc == "b"):
    cantidad_de_dinero = float(input(texto.format("dolar", "euros")))
    print("la cantidad de euros es {}".format(cantidad_de_dinero / dolar_euro))

elif(opc == "c"):
    cantidad_de_dinero = float(input(texto.format("libras", "euros")))
    print("la cantidad de euros es {}".format(cantidad_de_dinero / libra_euro))

elif(opc == "d"):
    cantidad_de_dinero = float(input(texto.format("euros", "libras")))
    print("la cantidad de libras es {}".format(cantidad_de_dinero * libra_euro))
