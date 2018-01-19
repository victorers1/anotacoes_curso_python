def func2(x, y):
    return x+y

def func1(x, y):
    return func2(x, y)

a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
soma = func1(a, b)
print(soma)