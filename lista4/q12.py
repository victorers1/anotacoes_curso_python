#Resolução quando a lista contém strings e números
def soma_iteravel(lista, s=1):
    for i in list(range(len(lista))):
        if(type(lista[i]) is int or type(lista[i]) is float):
            s *= lista[i]
    return s

upla = 2, 2, 3, "opa", True, 5
print("Multiplicação da lista {}: {}" .format(upla, soma_iteravel(upla)))