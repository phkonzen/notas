import numpy as np

def solSisTriaInf(A, b):
    n = b.size
    x = np.zeros_like(b)
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= A[i,j]*x[j]
        x[i] /= A[i,i]
    return x
    

# mat coefficientes
A = np.array([[1., 0., 0.],
              [-3., 2., 0.],
              [-1., 1., -1.]])

# vet termos constantes
b = np.array([2., -8., 0.])

# resol sis lin
x = solSisTriaInf(A, b)
print(x)

