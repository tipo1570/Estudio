import os


text=("\nplese introduce ramdon numers: ")
list_usr=[]

ex=()

while ex != "y":

    print(len(text)*"_")

    usr_input=int(input((text)))

    ex=input("you want to exit\n y|n: ")

    list_usr.append(usr_input)    

    os.system("cls")

print(len(text)*"_",
      "\nThe number list is {}"
      "\nThe smallest number is [{}]"
      "\nThe biggest number is [{}]"
      .format(list_usr,min(list_usr),max(list_usr)))

