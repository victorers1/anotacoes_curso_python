sentence = 'Jim quickly realized that the beautiful gowns are expensive'


def counter(sentence):
    '''
    sentence: string alphanumérica
    retorna: dicionário organizado como: {'letra':frequência}
    '''
    from string import ascii_letters as al  # Todas as letras minpusculas e maipusculas do alfabeto
    alphabet = al
    count_letters = {}  # Dicionário
    for i in sentence:
        if i in alphabet:  # 'i' assume uma letra diferente em cada iteração
            if i not in count_letters:
                count_letters[i] = 1
            else:
                count_letters[i] += 1
    return count_letters


address_count = counter(sentence)

maior = 0  # Frequência da letra com maior ocorrência
most_frequent_letter = ''
for i in address_count:  # 'i' assume o valor de uma chave diferente em cada iteração
    if address_count[i] > maior:
        maior = address_count[i]
        most_frequent_letter = i

print(most_frequent_letter)
