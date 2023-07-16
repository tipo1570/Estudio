#crear un programa que cuente espacios puntos y comas

texto_usuario="hola me llamo nico, tu como te llamas"



espacio = " "
espacios_encontrados = 0



puntos = "."
puntos_encontrados = 0



comas = ","
comas_encontrados = 0


print(texto_usuario)

for espacio in texto_usuario:
    print("he encontrado una '{}'".format(espacio))
    espacios_encontrados += 1


for puntos in texto_usuario:
    print("he encontrado una '{}'".format(puntos))
    puntos_encontrados += 1

for comas in texto_usuario:
    print("he encontrado una '{}'".format(comas))
    comas_encontrados += 1


print("espacios encotrados {}\n"
      "puntos encontrados {}\n"
      "comas encontradas {}\n"
      .format(espacios_encontrados,puntos_encontrados,comas_encontrados))