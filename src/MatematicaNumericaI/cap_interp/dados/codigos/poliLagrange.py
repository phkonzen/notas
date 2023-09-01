import numpy as np
from itertools import chain

def poliLagrange(x, xpts, ypts):
    # num. pts
    n = xpts.size
    # Lagrange poli
    L = np.ones((n,x.size))
    y = 0
    for i in range(n):
        for j in chain(range(i),range(i+1,n)):
            L[i] *= (x-xpts[j])/(xpts[i]-xpts[j])
        y += ypts[i] * L[i]
    return y

# exemplo
xpts = np.array([-1., 0, 1])
ypts = np.array([-1., 1, 1/2])

# verificação
x = xpts.copy()
print(poliLagrange(x, xpts, ypts))
