import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

alpha = -0.1

g = lambda x: x - alpha*(np.sin(x+np.pi/4)**2 \
    - x**3 + np.pi/4 * x**2 + 5*np.pi**2/16 * x + 3*np.pi**3/64)

gl = lambda x: 1. - alpha*(2*np.sin(x+np.pi/4)*np.cos(x+np.pi/4) \
    -3*x**2 + np.pi/2*x + 5*np.pi**2/16)

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

xx = np.linspace(1.5, 3.5)
ax.plot(xx, g(xx), label='$y=g(x)$')
ax.plot(xx, np.fabs(gl(xx)), label="$y=|g'(x)|$")

a=2
b=3
ax.plot([a]*2, [a,b], ls='--', color='red')
ax.plot([a,b], [a]*2, ls='--', color='red')

ax.plot([b]*2, [a,b], ls='--', color='red')
ax.plot([a,b], [b]*2, ls='--', color='red')

ax.plot([a, b], [a, b], ls='--', color='red')

xs = 3*np.pi/4
ax.plot([xs], [xs], marker='o', color='red')

ax.set_aspect('equal')
ax.legend()
fig.savefig('fig.pdf')
fig.savefig('fig.png')
