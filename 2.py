## Questão 2
import numpy as np
from math import factorial as fact

x = list(range(10)) 
for i in range(10):
    if i%2 == 0:
        x[i] = 3 + 7*(fact(i)) 
    else:
        x[i] = 2 + 4*np.log(i)
print("Posição com o maior valor: {0} \nMédia: {1:.2f}".format(x.index(max(x)),np.mean(x)))
