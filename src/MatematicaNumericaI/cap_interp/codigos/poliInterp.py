import numpy as np
import numpy.linalg as npla

def poliInterp(x, y):
    # num. pts
    n = x.size
    # Vandermonde
    A = np.empty((n,n))
    for j in range(n):
        A[:,j] = x**(n-1-j)
    # coefs
    p = npla.solve(A, y)
    return p

# exemplo
x = np.array([-1., 0, 1])
y = np.array([-1., 1, 1/2])

# poli interp
p = poliInterp(x, y)

# verificação
print(np.polyval(p, x))
