import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}",
     "figure.figsize": [4, 4],
     "figure.dpi": 300
     })

def poliInterp(x, y):
    # num. pts
    n = x.size
    # Vandermonde
    A = np.empty((n,n))
    for j in range(n):
        A[:,j] = x**(n-1-j)
    # coefs
    p = npla.solve(A, y)
    return p

# exemplo
x = np.array([-1., 0, 1])
y = np.array([-1., 1, 1/2])

# poli interp
p = poliInterp(x, y)

fig = plt.figure()
ax = fig.add_subplot()
ax.grid()

ax.plot(x, y, ls='', marker='o', label='pts')
xx = np.linspace(-1.25, 1.25)
ax.plot(xx, np.polyval(p, xx), label='interp')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend()

fig.savefig('fig.png', bbox_inches='tight')
