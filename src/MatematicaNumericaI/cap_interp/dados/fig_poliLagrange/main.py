import numpy as np
from scipy.interpolate import lagrange
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

f = lambda x: np.sin(x)

x = np.array([0, np.pi/2, np.pi])
poli = lagrange(x, f(x))

fig = plt.figure()
ax = fig.add_subplot()
ax.grid()

ax.plot(x, f(x), ls='', marker='o', label='pts')
xx = np.linspace(-0.25, np.pi+0.25)
ax.plot(xx, f(xx), label='seno')
ax.plot(xx, np.polyval(poli, xx), ls='--', label='lagrange')

ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.savefig('fig.png', bbox_inches='tight')
