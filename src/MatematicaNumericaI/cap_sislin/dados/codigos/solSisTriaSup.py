import numpy as np

def solSisTriaSup(A, b):
    n = b.size
    x = np.zeros_like(b)
    for i in range(n-1,-1,-1):
        x[i] = b[i]
        for j in range(n-1,i,-1):
            x[i] -= A[i,j]*x[j]
        x[i] /= A[i,i]
    return x
    

# mat coefficientes
A = np.array([[2., -1., 2.],
              [0., 2., -1.],
              [0., 0., 3.]])

# vet termos constantes
b = np.array([7., -3., 3.])

# sol sis lin
x = solSisTriaSup(A, b)
print(x)

