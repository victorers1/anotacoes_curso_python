__author__ = "Victor Emanuel Ribeiro Silva"

class A:
    def __init__(self):
        #print(id(self))
        pass

a = A()
#print(id(a))


#aula 125 a partir daqui - Classe Retângulo com métodos acessores
class Retangulo:
    def __init__(self):
        self._altura = 0
        self._largura = 0

    def set_altura(self,num):
        '''
        Recebe o valor da altura do retângulo
        :param num: inteiro que representa a altura do retângulo
        :return:
        '''
        if not(isinstance(num, int) and num > 0):
            raise ValueError("Altura inválida: {}".format(num))
        self._altura = num

    def set_largura(self, num):
        '''
        Recebe o valor da largura do retângulo
        :param num: inteiro que representa a largura do retângulo
        :return:
        '''
        if not(isinstance(num, int) and num > 0):
            raise ValueError("Largura inválida: {}".format(num))
        self._largura = num

    def get_area(self):
        '''
        Calcula a área do retângulo
        :return: produto entre os atributos 'largura' e 'altura'
        '''
        return self._largura * self._altura


# r1 = Retangulo(largura=10, altura=5)  # não funciona mais
# r2 = Retangulo(largura=-10, altura=5)   # não funciona mais

#Aula 130 - Atributos privados
r1 = Retangulo()
r1.set_altura(10)
r1.set_largura(5)
print(r1.get_area())