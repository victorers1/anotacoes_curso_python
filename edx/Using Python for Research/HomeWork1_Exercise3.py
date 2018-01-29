import random
random.seed(1)

def moving_window_average(x, n_neighbors=1):
    lista_media = []
    n = len(x)
    width = n_neighbors*2 + 1
    for i in range(n):
        soma = 0
        for k in range(i-n_neighbors, i+n_neighbors+1):
            if k >= 0 and k < n:  # Como 'k' será usado como índice do vetor x, deve estar dentro do intervalo [ 0, len(x) )
                soma += x[k]
            else:
                soma += x[i]
        lista_media.append(soma/width)

    return lista_media
x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))

# Compute and store R=1000 random values from 0-1 as x
R=1000
x=[]
Y=[]
for i in range(R):
   x.append(random.uniform(0,1))

#Compute the moving window average for x for values of n_neighbors ranging from 1 to 9 inclusive
# Store x as well as each of these averages as consecutive lists in a list called Y
Y.append(x)
for i in range(1,10):
    Y.append(moving_window_average(x, i))

# For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.
# Print your answer. As the window width increases, does the range of each list increase or decrease?
ranges = []
for i in Y:
    ranges.append(max(i) - min(i))
print(ranges)