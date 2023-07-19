import numpy as np
import numpy.linalg as npla
from itertools import chain

def poliLagrange(x, xpts, ypts):
    # num. pts
    n = xpts.size
    # Lagrange poli
    L = np.ones((x.size,n))
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
print(poliLagrange(x, xpts, ypts))
