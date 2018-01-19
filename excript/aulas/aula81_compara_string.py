print('a'>'A')
print('a'>'b')
print('a'>'0')

for i in range(32,127):
    print(chr(i))

#aula 82 a partir daqui - propriedades das Strings
s = "Lista de Caracteres"
print("A String s tem {} caracteres.".format(len(s)))
lista = s.split(' ')

s = lista[0] + ' ' + lista[-1]
print(s)

s = "Lista de Caracteres"
s = s.replace('de ', '')
print(s)

#aula 83 a partir daqui - iterando String
#Exemplo 1
s = "Iterando String"
for c in s:
    print(c)

#Exemplo 2
s = "Iterando String"
ind = 0
while(ind < len(s)):
    print(ind, s[ind])
    ind+=1

#Exemplo 3
for k,v in enumerate("Iterando String"):
    print(k, v)