# -*- coding: utf-8 -*-
# Adivinhar o número (entre 0 e 100) que o usuário está pensando usando o método da bisseção

inf = 0 # limite inferior
sup = 100 # limite superior
n = (sup+inf)//2
ans = ''
print('Please think of a number between 0 and 100!')

while True:
    print('Is your secret number {}?'.format(n))
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans == 'c':
        break
    elif ans == 'h':
        sup = n
        n = (sup+inf)//2
    elif ans == 'l':
        inf = n
        n = (sup+inf)//2
    else:
        print('Sorry, I did not understand your input.')
        continue

print('Game over. Your secret numbers was: {}'.format(n))