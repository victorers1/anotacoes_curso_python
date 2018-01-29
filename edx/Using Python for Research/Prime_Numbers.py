#Código checa se x é primo
import numpy as np
x=97
primo = not np.any([x%i == 0 for i in range(2, x)])

print("É primo?", primo)