inf = int(input("Insira o limite inferior: "))
sup = int(input("Insira o limite superior: "))

n1 = int(input("Valor ingnorado1: "))
n2 = int(input("Valor ingnorado2: "))
n3 = int(input("Valor ingnorado3: "))

for i in range(inf,sup+1):
    if(i != n1 and i != n2 and i != n3):
        print(i)