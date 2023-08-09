import numpy as np

def trap_comp(f, a, b, n):
    h = (b-a)/n
    S = f(a)
    for i in range(1,n):
        x = a + i*h
        S += 2*f(x)
    S += f(b)
    S *= h/2
    return S

# intervalo
a = 0.
b = 1.
# integrando
def f(x):
    return x*np.exp(-x**2)

# quad
n = 10
S = trap_comp(f, a, b, n)
# exata
I = 1./2 - np.exp(-1.)/2
# erro abs
print(f'{n}: {S:.5e}, {np.fabs(S-I):.1e}')
