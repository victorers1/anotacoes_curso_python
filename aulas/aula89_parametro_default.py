def login(usuario = "root", senha = "123"):
    print("Usuário: ", usuario)
    print("Senha: ", senha)

login("Claudio")

#aula 90 a partir daqui - argumentos posicionais e nomeados
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}, Sobrenome: {}, Idade: {}, Sexo: {}".format(nome, sobrenome,idade,sexo))

#dados_pessoais("Cláudio", "Rogério", 30, True)
dados_pessoais(idade=30,
               sobrenome="Carvalho",
               nome="Cláudio",
               sexo=True)

#aula 92 a partir daqui - retorno de múltiplos valores

def func():
    return 20, 30
#t = (10, 20)
#a, b = t #<- desempacotamento
x, y = func()

def potencia(x):
    quad = x**2
    cubo = x**3
    return quad, cubo
q, c = potencia(10)
print("{}, {}".format(q, c))