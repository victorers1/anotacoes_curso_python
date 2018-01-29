# Aplica uma lista de valores à uma função
testList = [1, -4, 8, -9]

def applyToEachV(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def quad(x):
    return x * x

applyToEachV(testList, quad)
print(testList)


# Aplica uma lista de funções a um valor
def applyToEachF(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(x):
    return x * x
def halve(x):
    return x / 2
def inc(x):
    return x + 1

l = applyToEachF([inc, square, halve, abs], -3)
print(l)