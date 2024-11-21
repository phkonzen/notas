import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}"
     })

f = lambda x: np.cbrt(x)

fig = plt.figure(dpi=300, figsize=[4,4])
ax = fig.add_subplot()

xx = np.linspace(0.1, 1.5)
ax.plot(xx, f(xx), ls='--', color='blue')
xx = np.linspace(0.5, 1.5)
ax.plot(xx, f(xx), color='blue', label='y = g(x)')
ax.plot(xx, xx, ls='--', label='y = x')
ax.plot([1], [1], ls='', marker='o', color='red')
ax.plot([0.5]*2, [0.5,1.5], ls='--', color='red')
ax.plot([1.5]*2, [0.5,1.5], ls='--', color='red')
ax.plot([0.5,1.5], [0.5]*2, ls='--', color='red')
ax.plot([0.5,1.5], [1.5]*2, ls='--', color='red')


x1 = 0.6
ax.plot([x1, x1], [0, f(x1)], ls='--', color='gray')
ax.plot([x1, f(x1)], [f(x1)]*2, ls='--', color='gray')
ax.plot([x1],[f(x1)], marker='o', color='blue')
x2 = f(x1)
ax.plot([x2, x2], [0, f(x2)], ls='--', color='gray')
ax.plot([x2, f(x2)], [f(x2)]*2, ls='--', color='gray')
ax.plot([x2],[f(x2)], marker='o', color='blue')
x3 = f(x2)
ax.plot([x3, x3], [0, f(x3)], ls='--', color='gray')
ax.plot([x3, f(x3)], [f(x3)]*2, ls='--', color='gray')
ax.plot([x3],[f(x3)], marker='o', color='blue')


#ax.set_aspect('equal')
ax.grid()
ax.legend(loc='lower left')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xticks([0.1, 0.5, x1, x2, x3, 1, 1.5],
              ['', '$a$', '$x^{(0)}$', '$x^{(1)}$', '$x^{(2)}$', '', '$b$'])
ax.set_yticks([0.1, 0.5, x1, x2, x3, 1, 1.5],
              ['', '$a$', '', '', '', '', '$b$'])

fig.savefig('fig.png', bbox_inches='tight')
