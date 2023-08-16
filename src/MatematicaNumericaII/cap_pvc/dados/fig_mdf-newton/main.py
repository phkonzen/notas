import numpy as np
import numpy.linalg as npla
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })

# parâmetros
n = 10
h = 1./n
xx = np.linspace(0., 1., n+1)

# c.c. Dirichlet
ua = 0.
ub = 0.

def f(x, u, ux):
    return u*ux - pi*sin(pi*x)*(pi + cos(pi*x))

def fu(x, u, ux):
    return ux

def fux(x, u, ux):
    return u

# rhs
def F(u):
    y = np.empty(n+1)
    # f_1
    y[0] = u[0] - ua
    # f_i
    for i in range(1,n):
        ux = u[i+1]/(2*h) - u[i-1]/(2*h) 
        y[i] = -1./h**2*u[i-1] + 2./h**2*u[i] - 1./h**2*u[i+1] \
            + f(xx[i], u[i], ux)
    # f_{n+1}
    y[n] = u[n] - ub

    return y

# jacobiana
def J(u):
    J = np.zeros((n+1,n+1))
    J[0,0] = 1.
    for i in range(1,n):
        ux = 1./(2*h)*u[i+1] - 1./(2*h)*u[i-1]
        J[i,i-1] = -1./h**2 - 1/(2*h)\
            * fux(xx[i], u[i], ux)
        J[i,i] = 2/h**2 + fu(xx[i], u[i], ux)
        J[i,i+1] = -1./h**2 + 1/(2*h)\
            * fux(xx[i], u[i], ux)
    J[n,n] = 1.

    return J

# aprox inicial
u = np.zeros(n+1)

# iterações de Newton
maxiter = 10
for k in range(maxiter):

    # passo de Newton
    dlta = npla.solve(J(u), -F(u))

    # atualização
    u += dlta

    ndlta = npla.norm(dlta)
    print(f'{k+1}: norm = {ndlta:.2e}')
    if (ndlta < 1e-10):
        print('convergiu.')
        break
    

# sol exata
def ue(x):
    return sin(pi*x)

fig = plt.figure(dpi=300)
ax = fig.add_subplot()

x = np.linspace(0., 1., 100)
ax.plot(x, ue(x), label='Analítica')
ax.plot(xx, u, ls='--', marker='o', label='MDF-Newton')
ax.grid()
ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$u(x)$')
plt.savefig('fig.png')
plt.savefig('fig.pdf')
