import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

x0 = 1.
x1 = 2.

phi0 = lambda x: (x-x1)/(x0-x1)
phi1 = lambda x: (x-x0)/(x1-x0)

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()

xx = np.array([1., 2.])
# phi0
ax.plot(xx, phi0(xx),
        ls='-', marker='o', label='$\\varphi_0$')
# phi1
ax.plot(xx, phi1(xx),
        ls='-', marker='o', label='$\\varphi_1$')

ax.set_xticks([1., 2.],
              ['$x_0$', '$x_1$'])
ax.set_yticks(np.linspace(0., 1., 5))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend()
plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')
