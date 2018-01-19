# -*- coding: utf-8 -*-
# Calcula o resultado da operação: base^exp de modo iterativo
def iterPower(base, exp):
    '''
    entradas: base (float), exp (inteiros não negativos)
    retorno: base^exp
    '''
    result = 1
    for i in range(exp):
        result *= base

    return result  # Retorna 1 no caso de 0^0


b = float(input('Diga a base: '))
e = int(input('Diga o expoente: '))
print(iterPower(b, e))


# Calcula o resultado da operação: base^exp de modo recursivo
def recurPower(base, exp):
    '''
    entradas: base (float), exp(inteiros não negativos)
    retorno: base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)


b = float(input('Diga a base: '))
e = int(input('Diga o expoente: '))
print(recurPower(b, e))