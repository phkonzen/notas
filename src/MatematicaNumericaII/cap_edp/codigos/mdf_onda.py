import numpy as np
from numpy import pi, sin, cos

# params
nt = 40
ht = 2./nt
tt = np.linspace(0., 2., nt+1)

nx = 10
hx = 1./nx
xx = np.linspace(0., 1., nx+1)

# c.i.s
def f(x):
    return np.zeros_like(x)

def g(x):
    return pi*sin(pi*x)

# axiliares
lbda = ht**2/hx**2

A = np.zeros(((nx-1), (nx-1)))
A[0,0] = 2*(1. - lbda)
A[0,1] = lbda
for i in range(1,nx-2):
    A[i,i-1] = lbda
    A[i,i] = 2*(1 - lbda)
    A[i,i+1] = lbda
A[nx-2,nx-3] = lbda
A[nx-2,nx-2] = 2*(1 - lbda)

# laço no tempo
## c.i.s
u0 = f(xx)

u1 = u0.copy()
u1[1:-1] = u0[1:-1] + ht*g(xx[1:-1])

u = u1.copy()
for k in range(1,nt):
    
    print(f'{k+1}: t = {tt[k+1]:f}')

    u[1:-1] = A@u1[1:-1] - u0[1:-1]

    u0 = u1.copy()
    u1 = u.copy()
