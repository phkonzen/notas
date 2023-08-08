import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })


# malha
n = 20
h = 2./n
xx = np.linspace(-1., 1., n+1)

# fonte
def f(x):
    return 2.

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
    return 1 - x**2

print(f'{h}: {npla.norm(u - ue(xx)):.1e}')

plt.plot(xx, ue(xx))
plt.plot(xx, u, ls='--')
plt.show()
