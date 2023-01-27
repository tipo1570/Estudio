var_num1 = int(input(" introducir un numero: "))
var_num2 = int(input(" introduce el segundo numero: "))
var_num3 = int(input(" intrduce el tercer numero: "))

print("el numero mayor entre {} {} y {} es {} y el numero menor es {}".format(var_num1, var_num2, var_num3,
                                                                              max(var_num1, var_num2, var_num3)
                                                                              , min(var_num1, var_num2, var_num3)
                                                                              )
      )