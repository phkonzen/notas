import numpy as np
import numpy.linalg as npla

# mat coefs
A = np.array([[-3.11, -1.03, 1.04, -1.17],
              [0.88, 0.29, -0.29, 0.33],
              [-2.82, -0.94, 0.94, -1.06],
              [4.00, 1.33, -1.34, 1.50]])

# 1. LU
L, U = lu(A)
