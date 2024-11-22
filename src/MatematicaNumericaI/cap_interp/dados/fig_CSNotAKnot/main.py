import numpy as np
from scipy.interpolate import CubicSpline
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

# exemplo
xx = np.array([0.,
               np.pi/6,
               np.pi/3,
               np.pi/2])
yy = np.sin(xx)

# spline
cs = CubicSpline(xx, yy)

fig = plt.figure()
ax = fig.add_subplot()
ax.grid()

x = np.linspace(-0.25, np.pi/2+0.25)
ax.plot(x, np.sin(x), label='f', color='C0')
ax.plot(xx, yy, ls='', marker='o', label='pts', color='C1')
ax.plot(x, cs(x), ls='--', label='spline', color='C1')

ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.savefig('fig.png')
