def soma_lista(lista, s=0):
    for i in lista:
        s += i
    return s

lista = [10, 10, 20, 0]
result = soma_lista(lista)
print("Soma da lista {}: {}".format(lista, result))

#Outra alternativa
valores = [1,2,34,5]
answer = sum(valores)
print("Soma da lista {}: {}".format(valores, answer))

#Resolução quando a lista contém strings e números
def soma_iteravel(lista, s=0):
    for i in list(range(len(lista))):
        if(type(lista[i]) is int or type(lista[i]) is float):
            s += lista[i]
    return s

upla = 2, 2, 3, "opa", True, 5
print("Soma da lista {}: {}" .format(upla, soma_iteravel(upla)))