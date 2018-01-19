S = [x**2 for x in range(10)]  # Define uma lista de x^2 tal que x são os números entre 0 e 9
M = [x for x in S if x%2==0]  # Define uma lista de x tal que cada x será um elemento de S somente se "x%2==0"

print(S)
print(M)

# Achando primos de 2 até 50
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)

word = "The quick brown fox jumped over the lazy dog".split()
stuff = [[w.upper(), w.lower(), len(w)] for w in word]

for i in stuff:  # Para uma impressão mais organizada
    print(i)