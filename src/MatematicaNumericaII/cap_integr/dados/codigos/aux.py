import numpy as np

# intervalo
a = 0.
b = 1./4
# fun
f = lambda x: x*np.exp(-x**2)
# quad
h = b-a
I = h*(f((a+b)/2))
print(f'I = {I:.5e}')
