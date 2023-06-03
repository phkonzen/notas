import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 14
     })
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


f = lambda x: np.sin(x+np.pi/4)**2 \
    - x**3 + np.pi/4 * x**2 + 5*np.pi**2/16 * x + 3*np.pi**3/64

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

xx = np.linspace(-2.5, 3.5)
ax.plot(xx, f(xx))

a = -2
ax.plot(a, f(a), marker='o', color='blue')

b = 3
ax.plot(b, f(b), marker='o', color='blue')

x1 = -np.pi/4
ax.plot(x1, f(x1), marker='o', color="red")

x2 = 3*np.pi/4
ax.plot(x2, f(x2), marker='o', color="red")

x0 = 2.6
ax.plot(x0, f(x0), marker='o', color="green")


ax.set_xticks([a, x1, 0, x2, x0, b],
              ["$-2$", "$-\\frac{\pi}{4}$",
               "$0$", "$\\overset{\\frac{3\pi}{4}}{}$",
               "$\\underset{x^{(0)}}{}$", "$3$"])

fig.savefig('fig.pdf')
fig.savefig('fig.png')
