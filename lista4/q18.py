def primo(num): #deve receber um número maior que 3 e retornar True se ele é primo, False caso contrário
    qtdDiv = 0
    d=2 #primeiro candidato a divisor
    while(qtdDiv == 0 and d < num): # só é testamos até a divisão de num por num/2 logo só precisamos encontrar um divisor
        if(num%d == 0):
            qtdDiv += 1
        if(qtdDiv == 1): #encontrar um divisor significa que não é primo
            return False #não é primo
        d += 1
    if(qtdDiv == 0):
        return True #é primo


def imprime_primo(*p):
    for i in p:
        if(primo(i)):
            print(i)


imprime_primo(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)