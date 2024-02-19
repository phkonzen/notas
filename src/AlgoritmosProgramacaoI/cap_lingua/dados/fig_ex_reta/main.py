import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

a = 2
b = -1
f = lambda x: 2*x - 1 

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

ax.plot([0]*2, [-5,3], lw=0.5, color='black')
ax.text(1.95, -0.2, '$x$')
ax.plot([-2,2], [0]*2, lw=0.5, color='black')
ax.text(-0.05, 2.85, '$y$')

xx = np.linspace(-2, 2)
ax.plot(xx, f(xx))

ax.text(1.65, 2.1, '$y = ax + b$')
ax.text(0.55, -0.36, '$\\displaystyle-\\frac{b}{a}$')
ax.plot([0.5], [0], marker='o', color='red')


ax.set_xlim((-0.5, 2.1))
ax.set_ylim((-2.1, 3.1))
fig.savefig('fig.png')
