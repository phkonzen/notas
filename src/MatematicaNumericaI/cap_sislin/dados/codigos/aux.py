import numpy as np
import numpy.linalg as npla

# sistema
A = np.array([[-4., 2., -1.],
              [-2., 5., 2.],
              [1., -1., -3.]])
b = np.array([-11., -7., 0.])

# A = L + D + U
L = np.tril(A, -1)
D = np.diag(np.diag(A))
U = np.triu(A, 1)

# matriz de Jacobi
T = npla.inv(D) @ (L + U)
# vetor de Jacobi
c = npla.inv(D) @ b

