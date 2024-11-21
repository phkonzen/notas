import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12,
     "font.sans-serif": "Computer Modern Roman",
     "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb}"
     })


f = lambda x: np.sin(x+np.pi/4)**2 \
    - x**3 + np.pi/4 * x**2 + 5*np.pi**2/16 * x + 3*np.pi**3/64
fl = lambda x: 2*np.sin(x+np.pi/4)*np.cos(x+np.pi/4) \
    - 3*x**2 + np.pi/2 * x + 5*np.pi**2/16

fig = plt.figure(figsize=[4,4], dpi=300)
ax = fig.add_subplot()

xx = np.linspace(-2.5, 3.5)
ax.plot(xx, f(xx), ls='--', label='$f$')
ax.plot(xx, fl(xx), ls='-', label="$f'$")

a = -1
ax.plot(a, fl(a), marker='o', color='blue')

b = 0
ax.plot(b, fl(b), marker='o', color='blue')

x1 = -np.pi/4
ax.plot(x1, f(x1), marker='o', color='red')
x2 = 3*np.pi/4

ax.set_xlabel('$x$')
ax.set_xticks([-2, x1, 0, x2, 3],
              ["$-2$", "$-\\frac{\pi}{4}$", "$0$", "$\\frac{3\pi}{4}$", "$3$"])
ax.set_ylabel('$y$')
ax.grid()
ax.legend()

plt.savefig('fig.png', bbox_inches='tight')
