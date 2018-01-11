def contagem(s):
    contM = contm = 0
    for i in s:
        if(i.isalpha()):
            if (i.isupper()):
                contM += 1
            else:
                contm += 1
    return contM, contm

str = input("Insira um texto qualquer: ")
qtdM, qtdm = contagem(str)
print("Quantidade de letras maiúsculas: {}\nQuantidade de letras minúsculas: {}".format(qtdM, qtdm))