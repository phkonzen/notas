import numpy as np
import numpy.linalg as npla

def poliInterp(x, y):
    # num. pts
    n = x.size
    # Vandermonde
    A = np.empty((n,n))
    for j in range(n):
        A[:,j] = x**(n-1-j)
    print(f'{npla.cond(A):.2e}')
    # coefs
    p = npla.solve(A, y)
    return p

# exemplo
n = 100
h = 0.1
x = np.linspace(0, (n-1)*h, n)
y = x.copy()

# poli interp
p = poliInterp(x, y)

# # verificação
# print(np.polyval(p, x))
