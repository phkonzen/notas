import numpy as np
from numpy.polynomial.legendre import leggauss

# integral
a = 0
b = 1
f = lambda x: x*np.exp(-x**2)
# quadratura
n = 2
x,w = leggauss(n)
# mud de var
x = (b-a)/2*(x+1)+a
w = (b-a)/2*w
# aproximação
S = np.sum(f(x)*w)
print(f'{n}: S = {S:.5e}')
