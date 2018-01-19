#Os números 10 e 20 serão empacotados
lista = [10, 20]
#Os números 10 e 20 serão desempacotados
x, y = lista

#exemplo 1
def func(a, b):
    print(a ,b)
func(*lista)
func(10, 20)
func(a=10, b=20)

#exemplo 2
def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

tupla = "eXcript", "Brasil", 20
lista = ["eXcript", "Brasil", 20]
pessoa(tupla[0], tupla[1], tupla[2])  #mesma coisa
pessoa(*tupla)  #mesma coisa
pessoa(*lista)  #tbm funciona com listas


d = {"nome":"eXcript", "sobrenome":"Brasil", "idade":20}  #As chaves devem ter o mesmo nome dos parâmetros
pessoa(**d)

