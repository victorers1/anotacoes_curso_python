def limite(inf, sup, x):
    return True if(x >= inf and x <= sup) else False

inf = int(input("Insira o limite inferior: "))
sup = int(input("Insira o limite superior: "))
x = int(input("Insira um valor real: "))


if(limite(inf, sup, x)):
    result = ""
else:
    result = "não "

print("{} {}está no limite fechado de [{}, {}]".format(x,result,inf, sup))