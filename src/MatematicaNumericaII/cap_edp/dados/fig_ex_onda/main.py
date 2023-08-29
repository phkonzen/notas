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

def exata(t,x):
    return sin(pi*t)*sin(pi*x)

T,X = np.meshgrid(tt, xx, indexing='ij')
Ue = exata(T,X)

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

# t = 0.
ax.plot(xx, Ue[0], color='C0', label='exata')
ax.plot(xx, U[0], ls = '--', marker='.', color='C1', label='numérica')
ax.text(0.71, Ue[0,7], '$t=0.00$',
        fontsize=8, backgroundcolor='w')

# t = 0.05
ax.plot(xx, Ue[1], color='C0')
ax.plot(xx, U[1], ls = '--', marker='.', color='C1')
ax.text(0.31, Ue[1,3], '$t=0.05$', fontsize=8, backgroundcolor='w')

# t = 0.1
ax.plot(xx, Ue[2], color='C0')
ax.plot(xx, U[2], ls = '--', marker='.', color='C1')
ax.text(0.71, Ue[2,7], '$t=0.10$', fontsize=8, backgroundcolor='w')

# t = 0.5
ax.plot(xx, Ue[10], color='C0')
ax.plot(xx, U[10], ls = '--', marker='.', color='C1')
ax.text(0.71, Ue[10,7], '$t=0.5$', fontsize=8, backgroundcolor='w')

# t = 1.1
ax.plot(xx, Ue[22], color='C0')
ax.plot(xx, U[22], ls = '--', marker='.', color='C1')
ax.text(0.71, Ue[22,7], '$t=1.10$', fontsize=8, backgroundcolor='w')

# t = 1.5
ax.plot(xx, Ue[30], color='C0')
ax.plot(xx, U[30], ls = '--', marker='.', color='C1')
ax.text(0.71, Ue[30,7], '$t=1.50$', fontsize=8, backgroundcolor='w')

ax.set_xlabel('$x$')
ax.set_ylabel('$u(t,x)$')
ax.legend(loc='lower left')
plt.savefig('fig_xx.png', bbox_inches='tight')
plt.savefig('fig_xx.pdf', bbox_inches='tight')

# x = 0.5
fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

ax.plot(tt, Ue[:,5], label='exata')
ax.plot(tt, U[:,5], ls='--', label='numérica')

ax.set_xlabel('$t$')
ax.set_ylabel('$u(t,0.5)$')
ax.legend()
plt.savefig('fig_x05.png', bbox_inches='tight')
plt.savefig('fig_x05.pdf', bbox_inches='tight')
