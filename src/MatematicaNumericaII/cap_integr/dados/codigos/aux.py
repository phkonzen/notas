import numpy as np
from numpy.polynomial.legendre import leggauss

# integrando
f = lambda x: np.cos(x)
# quadratura
n = 4
x,w = leggauss(n)
# aproximação
S = np.sum(f(x)*w)
print(f'{n}: S = {S:.5e}')
