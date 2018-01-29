#Simulando a jogada de 10 dados de 6 faces
#Em cada jogada, os valores nos dados são somados
#Um histograma é criado com X=valores possíveis de 'soma' (0 à 60), Y=frequência na qual 'soma' ocorreu
import random
import numpy as np
import matplotlib.pyplot as plt

num_dados = 10
num_jogadas = 10000
ys = []
for i in range(num_jogadas):
    soma = 0
    for dados in range(num_dados):
        valor_dado = random.choice([1,2,3,4,5,6])
        soma += valor_dado
    ys.append(soma)

plt.hist(ys)
plt.show()

X = np.random.randint(1,7, (10000,10))
Y = np.sum(X, axis=1)
plt.hist(Y)