def func(a, b, c, d):
    print(a+b+c+d)

lista = 1, 2, 3, 4
func(*lista)  #passando sem * é como se estivessemos dizendo que  a = lista e não tivessemos passando os valores de 'b', 'c', e 'd'