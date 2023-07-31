import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })


fig = plt.figure(dpi=300)
ax = fig.add_subplot()

f = lambda x: (x-1)*(1-x+1)
xx = np.linspace(0., 1.75)
ax.plot(xx, f(xx), label='f')

x0 = 0.5
rt = lambda x: (3 - 2*x0)*(x-x0) + f(x0)
xx = np.linspace(0.25, 1)
ax.plot(xx, rt(xx), ls='--', label='tangente')

x1 = 0.75
rs = lambda x: (f(x1) - f(x0))/(x1-x0)*(x-x0) + f(x0)
xx = np.linspace(0.25, 1)
ax.plot(xx, rs(xx), ls='-.', label='secante')

ax.plot([x0], [f(x0)], ls='', marker='o', color='red')
ax.plot([x1], [f(x1)], ls='', marker='o', color='green')


ax.grid()
ax.legend(loc='lower right')
ax.set_xticks([x0, x1],
              ['$x$', '$x+h$'])
ax.set_yticks([f(x0), f(x1)],
              ['$f(x)$', '$f(x+h)$'])
plt.savefig('fig.pdf')
plt.savefig('fig.png')
