#practica 1
#programa para determinar un numero mayor y menor en una box

print("\ndigitar varios numeros enteros")
print("_________________________________________________________ \n")
num_usuario1=int(input("por favor digitar un numero entero: "))
num_usuario2=int(input("por favor digitar un numero entero: "))
num_usuario3=int(input("por favor digitar un numero entero: "))
num_usuario4=int(input("por favor digitar un numero entero: "))

nummenor=min(num_usuario1,num_usuario2,num_usuario3,num_usuario4)

nummayor=max(num_usuario1,num_usuario2,num_usuario3,num_usuario4)


print("\n el numenor mayor es ", nummayor," y el numero menor es", nummenor)