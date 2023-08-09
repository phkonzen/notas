import numpy as np

def pm_comp(f, a, b, n):
    h = (b-a)/n
    S = 0.
    for i in range(n):
        x = a + (i+0.5)*h
        S += f(x)
    S *= h
    return S

# intervalo
a = 0.
b = 1.
# integrando
def f(x):
    return x*np.exp(-x**2)

# quad
n = 1000
S = pm_comp(f, a, b, n)
# exata
I = 1./2 - np.exp(-1.)/2
# erro abs
print(f'{n}: {S:.5e}, {np.fabs(S-I):.1e}')
