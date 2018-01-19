idade = int(input("Informe sua idade: "))
if(idade <=0):
    print("A sua idade dever ser um valor positivo")
elif(idade>150):
    print("Você deve ter menos de 150 anos")
elif(idade<18):
    print("Você deve ter mais de 18 anos")

num1 = input("Digite um valor: ")
num1 = int(num1)

num2 = input("Digite outro valor: ")
num2 = int(num2)

if(num1==num2):
    print("O {} é igual à {}".format(num1,num2))
elif(num1>num2):
    print("{} é maior que {}".format(num1,num2))
else:
    print("{} é menor que {}".format(num1,num2))