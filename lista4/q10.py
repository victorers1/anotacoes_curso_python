def maior(*valores):
    v = list(valores)
    print(v)
    v = list(valores).sort(reverse=True)
    print(v)
    print(v)

m = maior(1,2,3,4,5,6,7)
print(m)