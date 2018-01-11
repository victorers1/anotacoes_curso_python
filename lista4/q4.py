def funcao(a, b, c):
    lista = [a, b, c]
    lista.sort()

    print(lista)
    media = (a+b+c)/3
    print("Média = %.3f" %media)


#Bateria de testes
funcao(3,2,1)
funcao(2,3,1)
funcao(1,2,3)
funcao(1,3,2)
funcao(3,1,2)
funcao(2,1,3)

funcao(3,3,1)
funcao(3,2,2)
funcao(3,2,3)
funcao(1,1,1)