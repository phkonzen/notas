import numpy as np
import numpy.linalg as npla
# matriz dos coefs
A = np.array([[2, -1, 1],
              [-1, 1, 3],
              [1, 3, -3]])
# vet termos consts
b = np.array([-3, 6, 2])

# det(A)
detA = npla.det(A)
print(f'det(A) = {detA}')

# matrizes auxiliares
## A1
A1 = np.copy(A)
A1[:,0] = b
detA1 = npla.det(A1)
print(f'det(A1) = {detA1}')

## A2
A2 = np.copy(A)
A2[:,1] = b
detA2 = npla.det(A2)
print(f'det(A2) = {detA2}')

## A3
A3 = np.copy(A)
A3[:,2] = b
detA3 = npla.det(A3)
print(f'det(A3) = {detA3}')

# solucao
x = np.array([detA1/detA, detA2/detA, detA3/detA])
print(f'x = {x}')
