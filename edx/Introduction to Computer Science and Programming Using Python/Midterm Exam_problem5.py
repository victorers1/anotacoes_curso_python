def uniqueValues(aDict):
    '''
    aDict: um dicionário
    :returns: a lista de das chaves associadas aos inteiros que aparecem apenas uma vez no dicionário
    '''
    todos_valores = aDict.values()
    valores_inteiros = []
    valores_unicos = []
    chaves = []

    for i in todos_valores:  # Filtro 1: separa os valores inteiros
        if type(i) is int:
            valores_inteiros.append(i)

    for i in valores_inteiros: # Filtro 2: separa os inteiros únicos
        if valores_inteiros.count(i) == 1:
            valores_unicos.append(i)

    for i in aDict:  # Filtro 3: recolhe as chaves dos inteiros únicos
        if aDict[i] in valores_unicos:
            chaves.append(i)

    chaves.sort()
    return chaves

print(uniqueValues({1: 1, 2: 2, 3: 3}))