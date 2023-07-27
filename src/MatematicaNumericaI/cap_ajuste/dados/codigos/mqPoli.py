import numpy as np
import numpy.linalg as npla

# dados
xx = np.array([-1.0,
              0.0,
              1.0,
              1.5])
yy = np.array([1.2,
               -0.1,
               0.7,
               2.4])

# matriz
m = 3
n = xx.size
A = np.empty((n,m))
A[:,0] = xx**2
A[:,1] = xx
A[:,2] = np.ones_like(xx)

# sol de mq
p = npla.solve(A.T@A, A.T@yy)
print(p)
