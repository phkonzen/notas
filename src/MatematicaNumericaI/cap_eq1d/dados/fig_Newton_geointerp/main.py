import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}"
     })


f = lambda x: (x - 2.)**2 - 1.
fl = lambda x: 2*(x - 2.)

def rt(x, x0):
    return fl(x0)*(x-x0) + f(x0)

fig = plt.figure(dpi=300, figsize=(4,4))
ax = fig.add_subplot()
ax.grid()

a = -0.2
b = 1.5
xx = np.linspace(a, b)
ax.plot(xx, f(xx), label='função obj.')

x0 = 0
ax.plot([x0], [f(x0)], marker='o', ms=4, color='green')
xx = np.linspace(-0.2, 0.9)
ax.plot(xx, rt(xx, x0),
        lw='0.75', ls='--', color='red', label='reta tangente')

x1 = x0 - f(x0)/fl(x0)
ax.plot([x1], [f(x1)], marker='o', ms=4, color='green')
xx = np.linspace(0.5, 1.1)

x2 = x1 - f(x1)/fl(x1)
ax.plot([x2], [f(x2)], marker='o', ms=4, color='green')
ax.plot(xx, rt(xx, x1), lw='0.75', ls='--', color='red')


xs = 1.
ax.plot([xs], [f(xs)], marker='o', markersize=4, color='red')


ax.set_xticks([a, x0, x1, x2, xs, b],
              ['', '$x^{(0)}$', '$x^{(1)}$',
               '$\\overset{x^{(2)}}{}$', '$\\underset{x^*}{}$', ''])
ax.set_yticks([f(a), f(x0), f(x1), f(x2), f(xs), f(b)],
              ['', '$f(x^{(0)})$', '$f(x^{(1)})$',
               '', '$0$', ''])
ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

fig.savefig('fig.png', bbox_inches='tight')
