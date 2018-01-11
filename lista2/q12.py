n = float(input("Insira um valor: "))
inteiro = int(n)
n = n - inteiro

if(n==0.0):
    str ="inteiro"
else:
    str = "real"
print("Valor inserido era " + str)
