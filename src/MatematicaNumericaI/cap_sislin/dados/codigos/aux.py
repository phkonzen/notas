import numpy as np
import numpy.linalg as npla
np.set_printoptions(precision=None)

A = np.array([[-1., 2, -2],
              [3, -4, 1.],
              [1, -5., 3]])
# x = np.array([0.  , 0.75, 1.  , 0.75, 0.  ])
b = np.array([6., -11, -10])

print('Jacobi')
x0 = np.zeros_like(b)
x, info = jacobi(A, b, x0)

print('Gauss-Seidel')
x0 = np.zeros_like(b)
x, info = gs(A, b, x0)
