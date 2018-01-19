__author__ = "Victor Emanuel Ribeiro Silva"

# Nomenclatura de função: minha_funcao()
# Nomenclatura de classse: MinhaClasse()


class HelloWorld:  # Padrão CamelCase
    pass


class Pessoa:
    a = 10
    b = 20
    pass


p1 = Pessoa()
# p1 = None # desaloca o objeto
p2 = Pessoa()

print(id(p1))
print(id(p2))
