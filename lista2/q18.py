data = ""
while(len(data)!=10):
    data = input("Insira uma data válida no formato DD/MM/AAAA: ")

d,m,a = data.split("/")
d = int(d)
m = int(m)
a = int(a)

def verAno(ano):
    return True if (ano >= 0) else False
def verMes(mes):
    return False if(mes not in range(1, 13)) else True
def verDia(dia, mes, ano):
    if (mes in [1, 3, 5, 7, 8, 10, 12]):
        dataCorreta = True if (dia in list(range(1, 32))) else False  # dia entre 1 e 31

    elif (mes in [4, 6, 9, 11]):
        dataCorreta = True if (dia in list(range(1, 31))) else False  # dia entre 1 e 30

    else:
        bissexto = True if (ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0)) else False
        if (bissexto):
            dataCorreta = True if (dia in list(range(1, 30))) else False  # dia entre 1 e 28
        else:  # não for bissexto
            dataCorreta = True if (dia in list(range(1, 29))) else False
    return dataCorreta

dataCorreta = verAno(a)
if(dataCorreta):
    dataCorreta = verMes(m)
    if(dataCorreta):
        dataCorreta = verDia(d, m, a)

result = "válida" if(dataCorreta) else "inválida"
print("Data inserida é " + result)