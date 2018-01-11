#Aula 95 - Exemplo de desempacotamento
lista = [11, 10, 12]
tupla = 11, 10, 12
def func(a, b, c):
    print(a)
    print(b)
    print(c)
    print(30*'-')

lista.sort()
func(*lista)

l = [*tupla]  #Ou l = list(tupla)
l.sort()
func(*l)

func(**dict(zip(("b", "a", "c"), tupla)))