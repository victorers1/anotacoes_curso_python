# -*- coding: utf-8 -*-
# Calcula o maior divisor comum entre dois números de modo iterativo
def gcdIter(a, b):
    '''
    a, b: inteiro positivos
    retorno: um inteiro positivo, o maior divisor comum entre 'a' e 'b'
    '''
    menor = a if a < b else b
    for i in range(menor, 0, -1):
        #print(i)
        if a%i==0 and b%i==0:
            return i

print(gcdIter(1, 57))

# Calcula o maior divisor comum entre dois números de modo recursivo
def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    elif a==0:
        return b
    else:
        return gcdRecur(b, a%b)

print(gcdRecur(9, 12))