import numpy as np
import numpy.linalg as npla

x = np.array([-2.5, -1.3, 0.2, 1.7, 2.3]).reshape(-1,1)
y = np.array([3.8, 0.5, 2.7, 1.2, -1.3]).reshape(-1,1)

A = np.sin(x)
A = np.hstack((A,np.cos(x)))
A = np.hstack((A,np.ones((x.size,1))))
c = npla.solve(A.T@A,A.T@y)

def f(x, c=c):
    return c[0]*np.sin(x) + c[1]*np.cos(x) + c[2]

print(npla.norm(y - f(x)))
