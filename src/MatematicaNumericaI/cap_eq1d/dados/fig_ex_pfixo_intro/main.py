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

g1 = lambda x: 16/(5*np.pi**2)*(-np.sin(x+np.pi/4)**2 \
                                + x**3 - np.pi/4*x**2 - 3*np.pi**3/64)

g2 = lambda x: np.cbrt(np.sin(x+np.pi/4)**2 \
                       + np.pi/4*x**2 + 5*np.pi**2/16*x + 3*np.pi**3/64)

fig = plt.figure(dpi=300, figsize=[4,4])
ax = fig.add_subplot()

xx = np.linspace(-2, 3, 100)
ax.plot(xx, f(xx), label='$y = f(x)$')
ax.plot(xx, g1(xx), ls='-.', label='$y = g_1(x)$')
ax.plot(xx, g2(xx), ls='--', label='$y = g_2(x)$')
ax.plot(xx, xx, ls='-', label='$y = x$')

x1 = -np.pi/4
ax.plot([x1]*2, [0,x1], ls='--', color="gray")
ax.plot([-2,x1], [x1]*2, ls='--', color="gray")
ax.plot(x1, x1, marker='o', color="red")

x2 = 3*np.pi/4
ax.plot([x2]*2, [0,x2], ls='--', color="gray")
ax.plot([-2,x2], [x2]*2, ls='--', color="gray")
ax.plot(x2, x2, marker='o', color="red")

ax.grid()
ax.set_xlim((-2, 3))
ax.set_ylim((-6, 6))
ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.savefig('fig.png', bbox_inches='tight')
