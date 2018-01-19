lista = "Bem-vindo ao Curso de Python"

print(lista[:20])  # lista[start : stop : step]
print(lista[20:])
print(lista[::2])
print(lista[2::2])
print(lista[::-1]) #inverte

#aula 72 a partir daqui
l = ['bbb', 'ccc', 'ddd']
l.append('eee')
l.insert(0, 'aaa')
l[1] = 'bbbb'
print(l)
l.pop()
l.pop(0)

print(l)

l.clear()
print(l)