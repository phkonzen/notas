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

def exata(x,y):
    return np.sin(np.pi*x)*np.sin(np.pi*y)

X, Y = np.meshgrid(xx, yy, indexing='xy')
Ue = exata(X,Y)
U = u.reshape((n+1,n+1))

fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection='3d')
#ax.plot_surface(X, Y, Ue, cmap='viridis', alpha=0.25)
ax.plot_surface(X, Y, U, cmap='plasma',
                alpha=0.9, lw=0.1, antialiased=True)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.savefig('fig_surface.png', bbox_inches='tight')
plt.savefig('fig_surface.pdf', bbox_inches='tight')

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
levels=np.linspace(-0.0001, 1., 11)
cb = ax.contourf(X, Y, U, levels=levels,
                 cmap='plasma', antialiased=True)
cl = ax.contour(X, Y, Ue, levels=levels, colors='white')
ax.clabel(cl, inline=True, fmt='%.1f')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.colorbar(cb)
plt.savefig('fig_contour.png', bbox_inches='tight')
plt.savefig('fig_contour.pdf', bbox_inches='tight')




