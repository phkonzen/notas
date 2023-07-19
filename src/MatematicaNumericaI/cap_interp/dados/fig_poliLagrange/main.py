import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

f = lambda x: np.sin(x)

x = np.array([0, np.pi/2, np.pi])
poli = lagrange(x, f(x))

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

ax.plot(x, f(x), ls='', marker='o', label='pts')
xx = np.linspace(-0.25, np.pi+0.25)
ax.plot(xx, f(xx), label='seno')
ax.plot(xx, np.polyval(poli, xx), label='lagrange')

ax.legend()
fig.savefig('fig.pdf')
fig.savefig('fig.png')
