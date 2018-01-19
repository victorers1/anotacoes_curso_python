print()
print("inicio")
i=0
while(i<10):
    i+=1
    if(i%2==0):
        continue
    if(i>5):
        break #não executa o else
    print(i)
else:
    print("fim")
print()