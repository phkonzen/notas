import numpy as np
import numpy.linalg as npla

# dados
xx = np.array([-2.5,
               -1.3,
               0.2,
               1.7,
               2.3])
yy = np.array([3.8,
               0.5,
               2.7,
               1.2,
               -1.3])

# matriz
m = 4
n = xx.size
A = np.empty((n,m))
A[:,0] = xx**3
A[:,1] = xx**2
A[:,2] = xx
A[:,3] = np.ones_like(xx)

# sol de mq
c = npla.solve(A.T@A, A.T@yy)
print(f'c =\n {c}')

def f(x, c=c):
    y = c[0]*x**3 + c[1]*x**2 + c[2]*x + c[3]
    return y

print(f'enorm = {npla.norm(yy - f(xx)):.4e}')


