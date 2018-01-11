lista = [1,2,8,5,15,3,6,8]
type(lista)
print(lista[0]+lista[1])
l = ['a','b','c','d','e']

lista = list("eXcript")#lista de 7 elementos
print(lista)

lista = list((4,5,8))
print(lista)

lista = list(("eXcript",))#lista de 1 elemento
print(lista)

a = (5) #tipo k
print(type(a))

a = (5,)#tipo tupla
print(type(a))

lista = [['a','b','c'],[5,8,2],[]]

print(lista[0][1])

print(len(lista))

print(lista[-1])#retorna o último elemento da lista

#aula 69 a partir daqui
lista = [1,2,3,4,5]
lista = [0]+lista
lista = lista+[7,8,9,10]
print(lista)
lista.append(11)
lista.append([11])
del(lista[-1])
print(lista)
lista += 10*[0]
print(lista)

#aula 70 a partir daqui
lista_num = [100, 200,  300, 400, 500, 600, 700, 800]
#lista_ind = list(range(0, 4))
for item in range(len(lista_num)):
    lista_num[item] += 1000
print(lista_num)

le = ['aaa', 'bbb', 'ccc', 'ddd']
print(list(enumerate(le)))

for idx, item in enumerate(lista_num):
    lista_num[idx] += 1000

print(lista_num)