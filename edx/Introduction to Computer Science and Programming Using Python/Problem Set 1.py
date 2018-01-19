# -*- coding: utf-8 -*-

# Contar quantidade de vogais numa string
s = 'straeiou'
v = 0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        v += 1

print('Number of vowels:', v)

# Contar quantidade de 'bob' numa string
s = 'azcbobobeggbobob'
bob = 0
for i in range(len(s)-2):
    if s[i]=='b' and s[i+1]=='o' and s[i+2]=='b':
        bob +=1
print('Number os times bob occurs is:', bob)

# Imprimir a maior sequência de letras organizadas em ordem alfabética
s = 'zyxwvutsrqponmlkjihgfedcba'
c = s[0]
maior_seq = c
for i in range(0, len(s)-1):
    if s[i] <= s[i+1]:
        c += s[i+1]
        if len(c) > len(maior_seq):
            maior_seq = c
    else:
        c = s[i+1]
print('Longest substring in alphabetical order is:', maior_seq)