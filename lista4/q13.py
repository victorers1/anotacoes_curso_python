def inverte_lista(lista):
    a = list(lista)  #Nunca esquecer do list() para NÃO alterar a lista original
    for i in list(range(0, int(len(a)/2))):
        a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]
    return a


lista1 = [1, 2, True, 3, "opa", 4, 5]
lista2 = ["um", "dois", "três", "quatro"]
lista3 = "Victor"

print("{} invertido fica {}" .format(lista1, inverte_lista(lista1)))
print("{} invertido fica {}" .format(lista2, inverte_lista(lista2)))
print("{} invertido fica {}" .format(lista3, inverte_lista(lista3)))

