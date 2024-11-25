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
A[:,0] = x**2
A[:,1] = x
A[:,2] = np.ones_like(x)

# sol de mq
p = npla.solve(A.T@A, A.T@y)

fig = plt.figure()
ax = fig.add_subplot()
ax.grid()

ax.plot(x, y, ls='', marker='o', label='pts')
xx = np.linspace(-1.25, 1.75)
ax.plot(xx, np.polyval(p, xx), label='p(x)')

ax.legend()
ax.set_xticks(x)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.savefig('fig.png', bbox_inches='tight')
