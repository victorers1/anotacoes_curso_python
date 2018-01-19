#Dicionário é um tipo de lista não ordenada na qual cada elemento está associado a uma chave
d1 = {} #dicionário vazio

d1['aaa'] = 1000 #nome_dict['chave'] = valor
print(d1)

d1['bbb'] = 2000
d1['ccc'] = 3000
d1['ddd'] = 4000
print("d1 =", d1)

d2 = {1.1:"teste1", 2.2:"teste2", 3:"teste3"}
print("d2 =", d2)

tel = {30301122:"Pericles", 12345678:"Menelau", 98764321:"Atreu", 43218765:"Tieste"}
print("{} tem {} elementos".format(tel, len(tel)))
del(tel[43218765])

lista_telefones = tel.keys()
lista_nomes = tel.values()

# for k,v in tel:
#     print(k,v)