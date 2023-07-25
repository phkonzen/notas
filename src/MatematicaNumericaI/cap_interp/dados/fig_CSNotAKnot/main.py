import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

# exemplo
xx = np.array([0.,
               np.pi/6,
               np.pi/3,
               np.pi/2])
yy = np.sin(xx)

# spline
cs = CubicSpline(xx, yy)

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

x = np.linspace(-0.25, np.pi/2+0.25)
ax.plot(x, np.sin(x), label='f', color='red')
ax.plot(xx, yy, ls='', marker='o', label='pts', color='blue')
ax.plot(x, cs(x), ls='--', label='spline', color='blue')

ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
fig.savefig('fig.pdf')
fig.savefig('fig.png')
