import numpy as np
import numpy.linalg as npla

# params
alpha = 1.
theta = 0.5

# malha temporal
nt = 10
ht = 1./nt
tt = np.linspace(0., 1., nt+1)

# malha espacial
nx = 10
h = 1./n
xx = np.linspace(0., 1., n+1)

# rhs
def f(t, x):
    return (np.pi**2-1)*np.exp(-t)*np.sin(np.pi*x)

# axiliares
lbda = alpha/h**2

# matriz difusão
A = np.zeros(((nx-1), (nx-1)))
A[0,0] = -2*lbda
A[0,1] = lbda
for i in range(1,nx-2):
    A[i,i-1] = lbda
    A[i,i] = -2*lbda
    A[i,i+1] = lbda
A[nx-2,nx-3] = lbda
A[nx-2,nx-2] = -2*lbda

# matrizes auxiliares
Jth = np.identity(A.shape[0]) - theta*ht*A
J1th = np.identity(A.shape[0]) + (1-theta)*ht*A

# c.i.
u0 = np.sin(np.pi * xx)

# laço no tempo
u = u0.copy()
for k in range(nt):    
    print(f'{k+1}: t = {tt[k+1]:f}')
    fth = (1-theta)*f(tt[k],xx[1:-1]) + theta*f(tt[k+1],xx[1:-1])
    u[1:-1] = npla.solve(Jth, J1th@u0[1:-1]+ht*fth)
    u0 = u.copy()    

