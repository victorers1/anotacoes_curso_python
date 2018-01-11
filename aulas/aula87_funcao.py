from math import sqrt
def funcao():
    print("Fala galera.")

funcao()

#aula 88 a partir daqui
def soma(x, y):
    return x+y
s = soma(2, 3)
print(s)

#exemplo 1 - raízes de um polinômio do segundo grau
def bhaskara(a, b, c):
    if(a==0):
        print("a não pode ser 0")
        return (0, 0)
    else:
        delta = b**2 - 4*a*c
        if(delta<0):
            print("O polinômio tem raizes negativas.")
            return (0, 0)
        else:
            r1 = (-b + sqrt(delta)) / (2 * a)
            r2 = (-b - sqrt(delta)) / (2 * a)
            return (r1, r2)


a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
raizes = bhaskara(a, b, c)
r1 = raizes[0]
r2 = raizes[1]
print("Raízes do polinômio {}x^2 + {}*x + {} são {} e {}".format(a, b, c, r1, r2))