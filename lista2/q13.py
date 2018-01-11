a = float(input("Bote um valor: "))
b = float(input("Bote um valor: "))
c = float(input("Bote um valor (último): "))

print("O maior é")
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)