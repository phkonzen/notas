import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })

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
U = u.copy()
for k in range(nt):
    
    print(f'{k+1}: t = {tt[k+1]:f}')

    fth = (1-theta)*f(tt[k],xx[1:-1]) + theta*f(tt[k+1],xx[1:-1])
    u[1:-1] = npla.solve(Jth, J1th@u0[1:-1]+ht*fth)
    U = np.vstack((U,u))
    u0 = u.copy()    

def exata(t,x):
    return np.exp(-t)*np.sin(np.pi*x)

T,X = np.meshgrid(tt, xx, indexing='ij')
Ue = exata(T,X)

plt.close()
fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection='3d')
ax.plot_surface(T, X, U, cmap='plasma',
                alpha=0.8)
ax.set_xlabel('$t$')
ax.set_ylabel('$x$')
ax.set_zlabel('$u$')
plt.savefig('fig_surface.png', bbox_inches='tight')
plt.savefig('fig_surface.pdf', bbox_inches='tight')

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
levels=np.linspace(0., 1., 11)
cb = ax.contourf(X, T, U, levels=levels,
                 cmap='plasma', antialiased=True)
cl = ax.contour(X, T, Ue, levels=levels, colors='white')
ax.clabel(cl, inline=True, fmt='%.1f')
ax.set_xlabel('$x$')
ax.set_ylabel('$t$')
plt.colorbar(cb)
plt.savefig('fig_contour.png', bbox_inches='tight')
plt.savefig('fig_contour.pdf', bbox_inches='tight')
