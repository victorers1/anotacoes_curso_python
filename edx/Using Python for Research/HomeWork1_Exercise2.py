import random
import math
random.seed(1)

def distance(x, y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

def in_circle(x, origin = [0,0]):
    '''
    Checa se um ponto 'x' está dentro de uma circunferência de raio 1 centrada em 'origin'
    Retorna True se o ponto 'x' está dentro da circunferência de raio 1 centrada em 'origin', caso contrário, False
    '''
    if distance(x,origin) > 1:
        return False
    else:
        return True

def rand():
    return random.uniform(-1,1)

R = 10000
x = []  # Lista de pontos no formado de tuplas
inside = []  # Lista de respostas sobre o ponto estar dentro do círculo
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    if in_circle(point):
        inside.append(True)
    else:
        inside.append(False)

#print(inside)
print(sum(inside) / R)
print(math.pi/4)