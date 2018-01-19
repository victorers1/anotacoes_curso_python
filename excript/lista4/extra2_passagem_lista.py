def teste(lista):
    print("Original: {}".format(lista))
    lista[0] = "o"  # A lista original é alterada
    print("Depois de alterar: {}".format(lista))
    return lista

lis = [1, 2, 3, 4]
outra_lista = teste(lis)
print("{} <==> {}". format(lis, outra_lista))

def teste2(lista):
    print(40 * '-')
    l = list(lista)  # Usar essa linha para NÃO  alterar a lista original
    l = lista  # Usar essa linha para alterar a lista orginal
    print("Original: {}".format(l))
    l[0] = "o"  # A lista original é alterada
    print("Depois de alterar: {}".format(l))
    print(40 * '-')
    return l

lista = [1, 2, 3, 4]
lista2 = teste2(lista)
print("Original: {}".format(lista))
print("Lista mudada: {}".format(lista2))
