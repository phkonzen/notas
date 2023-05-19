import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })

f = lambda x: x**2-1

fig = plt.figure(dpi=300)
ax = fig.add_subplot()

xx = np.linspace(-2, 2)
ax.plot(xx, f(xx), label='y = g(x)')

ax.plot(xx, xx, label='y = x')

xf = np.roots([1,-1,-1])
ax.plot([xf[0], xf[0]], [0, f(xf[0])], ls='--', color='gray')
ax.plot([-2, xf[0]], [f(xf[0])]*2, ls='--', color='gray')
ax.plot([xf[1]]*2, [0, f(xf[1])], ls='--', color='gray')
ax.plot([-2, xf[1]], [f(xf[1])]*2, ls='--', color='gray')
ax.plot(xf, f(xf), ls='',
        marker='o', color='red', label='pto. fixo')


ax.set_aspect('equal')
ax.set_xticks([-2,-1,0,1,2])
ax.set_yticks([-2,-1,0,1,2])
ax.grid()
ax.set_xlim((-2,2))
ax.set_ylim((-2,2))
ax.legend()

fig.savefig('fig.pdf')
fig.savefig('fig.png')
