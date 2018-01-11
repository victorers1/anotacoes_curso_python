num = float(input("Insira um valor, por obséquio: "))
if(num>0.0):
    str = "positivo"
elif(num==0):
    str = "nulo"
else:
    str = "negativo"

print(num, "é " + str)