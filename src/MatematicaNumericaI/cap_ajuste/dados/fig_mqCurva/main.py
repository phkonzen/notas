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

# dados
x = np.array([-1.0,
              0.0,
              1.0,
              1.5])
y = np.array([1.2,
               -0.1,
               0.7,
               2.4])

# matriz
m = 3
n = x.size
A = np.empty((n,m))
A[:,0] = np.sin(x)
A[:,1] = np.cos(x)
A[:,2] = np.ones_like(x)

# sol de mq
c = npla.solve(A.T@A, A.T@y)

def f(x, c=c):
    y = c[0]*np.sin(x) \
        + c[1]*np.cos(x) \
        + c[2]
    return y

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

ax.plot(x, y, ls='', marker='o', label='$\\text{pts}$')
xx = np.linspace(-1.25, 1.75)
ax.plot(xx, f(xx), label='$f(x; \\pmb{c})$')

ax.legend()
ax.set_xticks(x)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.savefig('fig.png', bbox_inches='tight')
