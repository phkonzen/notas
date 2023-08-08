import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })


# malha
n = 10
h = 1./n
xx = np.linspace(0., 1., n+1)

# fonte
def f(x):
    return np.pi**2*np.sin(np.pi*x)

# prob discreto
A = np.zeros((n+1, n+1))
b = np.empty(n+1)

# c.c. x = 0.
A[0,0] = 1.
b[0] = 0.

# pts internos
for i in range(1,n):
    A[i,i-1] = -1./h**2
    A[i,i] = 2./h**2
    A[i,i+1] = -1./h**2
    b[i] = f(xx[i])

# c.c. x = 1.
A[n,n] = 1.
b[n] = 0.

# resol
u = npla.solve(A, b)

# sol exata
def ue(x):
    return np.sin(np.pi*x)

fig = plt.figure(dpi=300)
ax = fig.add_subplot()

x = np.linspace(0., 1., 100)
ax.plot(x, ue(x), label='Analítica')
ax.plot(xx, u, ls='--', marker='o', label='MDF')
ax.grid()
ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$u(x)$')
plt.savefig('fig.png')
plt.savefig('fig.pdf')
