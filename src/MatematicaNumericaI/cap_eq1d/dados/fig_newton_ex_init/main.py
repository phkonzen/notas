import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}"
     })


f = lambda x: (x-1.)*np.exp(-x**2)
fl = lambda x: (2*x - 2*x**2 + 1)*np.exp(-x**2)
def rt(x,x0):
    return fl(x0)*(x-x0) + f(x0)

fig = plt.figure(dpi=300, figsize=(4,4))
ax = fig.add_subplot()
ax.grid()

a = 0
b = 3
xx = np.linspace(a, b)
ax.plot(xx, f(xx))

xs = 1
ax.plot([xs], [f(xs)], marker='o', color='red')

x0 = 0.5
ax.plot([x0], [f(x0)], marker='o', color='green')
xx = np.linspace(0.25, 0.9)
ax.plot(xx, rt(xx,x0), lw='0.75', ls='--',
        color='red')

x1 = 1.5
ax.plot([x1], [f(x1)], marker='o', color='green')
xx = np.linspace(1.1, 2.9)
ax.plot(xx, rt(xx,x1), lw='0.75', ls='--',
        color='red')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.savefig('fig.png', bbox_inches='tight')
