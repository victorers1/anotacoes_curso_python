#troca de valores
a=10
b=5
print("a={}, b={}".format(a,b))
a,b = b,a
print("a={}, b={}".format(a,b))

a1,a2,a3 = 2,4,8
print("a1={}, a2={},a3={}".format(a1,a2,a3))
a1,a2,a3 = a1**2, a1+a2+a3, a1*a2*a3
print("a1={}, a2={},a3={}".format(a1,a2,a3))

nome,sobrenome = "José", " da Silva"
print(nome + sobrenome)