from math import factorial as fac
def fatorial(x):
    return fac(x)

n = -1
while(n<0):
    n = int(input("Digite um valor inteiro não negativo: "))
else:
    print("Fatorial de {} é {}".format(n, fatorial(n)))
