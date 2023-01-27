# programa para calcular grados celius a farenheit y viceversa

print("Este programa sirve para hacer converciones")

print(" 1. farenheit a celcius ")
print(" 2. celcius a farenheit ")

opc = int(input("escoja una opcion "))

if (opc == 1):
    var_num1 = int(input("introduzca el valor en farenheit : "))
    var = (var_num1 - 32) * 5 / 9
    print("el resultado es", var)
elif (opc == 2):
    var_num2 = int(input(" introduza el valor en celsius : "))
    var2 = ((var_num2*9/5)+32)
    print( "el resultado es", var2)
else:
    print ("escoja una opcion valida")