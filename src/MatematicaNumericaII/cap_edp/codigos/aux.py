import numpy as np
from numpy import pi, sin, cos
import numpy.linalg as npla
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })

# params
nt = 600
ht = 1.5/nt
tt = np.linspace(0., 1.5, nt+1)

nx = 100
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
U = u0.copy()

u1 = u0.copy()
u1[1:-1] = u0[1:-1] + ht*g(xx[1:-1])
U = np.vstack((U,u1))

u = u1.copy()
for k in range(1,nt):
    
    print(f'{k+1}: t = {tt[k+1]:f}')

    u[1:-1] = A@u1[1:-1] - u0[1:-1]
    U = np.vstack((U,u))

    u0 = u1.copy()
    u1 = u.copy()

print(f'{u[nx//2]:.4f}')

def exata(t,x):
    return sin(pi*t)*sin(pi*x)

T,X = np.meshgrid(tt, xx, indexing='ij')
Ue = exata(T,X)

# x = 0.5
plt.close()
fig = plt.figure()
ax = fig.add_subplot()
ax.grid()

ax.plot(tt, Ue[:,5], label='exata')
ax.plot(tt, U[:,5], ls='--', label='numérica')

ax.set_xlabel('$t$')
ax.set_ylabel('$u(t,0.5)$')
ax.legend()
plt.show()
