import numpy as np
import numpy.linalg as npla

# malha
n = 10
h = 1./n
xx = np.linspace(0., 1., n+1)
yy = np.linspace(0., 1., n+1)

# rhs
def f(x,y):
    return -2*np.pi**2*np.sin(np.pi*x)*np.sin(np.pi*y)

# problema discreto
A = np.zeros(((n+1)**2, (n+1)**2))
b = np.empty((n+1)**2)

# c.c.
for j in range(n+1):
    # i = 0
    k = j*(n+1)
    A[k,k] = 1.
    b[k] = 0.
    # i = n
    k = n + j*(n+1)
    A[k,k] = 1.
    b[k] = 0.

for i in range(1,n):
    # j = 0
    k = i
    A[k,k] = 1.
    b[k] = 0.
    # j = n
    k = i + n*(n+1)
    A[k,k] = 1.
    b[k] = 0.

# pts internos
for i in range(1,n):
    for j in range(1,n):
        k = i + j*(n+1)
        A[k,k-n-1] = 1./h**2
        A[k,k-1] = 1./h**2
        A[k,k] = -4./h**2
        A[k,k+1] = 1./h**2
        A[k,k+n+1] = 1./h**2
        b[k] = f(xx[i],yy[j])

# resol p.d.
u = npla.solve(A, b)
