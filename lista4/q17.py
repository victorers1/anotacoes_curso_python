def conj(lista):
    L = list(lista)
    aux = []
    for i in L:
        if(i not in aux):
            aux.append(i)
    return aux

lista = [1,2,3,5,3,5,3,7,7,7,4,5,5,1,1,2,3,7]
conjunto = conj(lista)

print("{} <==> {}".format(lista, conjunto))
