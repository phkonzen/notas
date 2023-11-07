#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 16
     })

xx = np.array([0., 1, 2, 3, 4, 5, 6])
def phi0(x):
    x = np.asarray(x)
    y = np.empty_like(x)
    for i,x in enumerate(x):
        if (x >= xx[0]) and (x <= xx[1]):
            y[i] = (x-xx[1])/(xx[0]-xx[1])
        else:
            y[i] = 0.
    return y

def phii(x):
    x = np.asarray(x)
    y = np.empty_like(x)
    for i,x in enumerate(x):
        if (x >= xx[2]) and (x <= xx[3]):
            y[i] = (x-xx[2])/(xx[3]-xx[2])
        elif (x >= xx[3]) and (x <= xx[4]):
            y[i] = (xx[4]-x)/(xx[4]-xx[3])
        else:
            y[i] = 0.
    return y

def phin(x):
    x = np.asarray(x)
    y = np.empty_like(x)
    for i,x in enumerate(x):
        if (x >= xx[5]) and (x <= xx[6]):
            y[i] = (x-xx[5])/(xx[6]-xx[5])
        else:
            y[i] = 0.
    return y

fig = plt.figure(dpi=300)
ax = fig.add_subplot()

xp = np.linspace(0., 6., num=500)

# phi0
ax.plot(xp, phi0(xp), color='C0')
ax.text(0., 1.05, '$\\varphi_0$')

# phi_i
ax.plot(xp, phii(xp), color='C1')
ax.text(3., 1.05, '$\\varphi_i$')

ax.text(1.35, -0.115, '$\cdots$')
ax.text(4.35, -0.115, '$\cdots$')

# phi_n
ax.plot(xp, phin(xp), color='C2')
ax.text(6., 1.05, '$\\varphi_n$')

ax.set_xticks(xx,
          ['$x_0$', '$x_1$',
           '$x_{i-1}$', '$x_{i}$', '$x_{i+1}$',
           '$x_{n-1}$', '$x_{n}$'])

ax.set_ylim((-0.05, 1.1))
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.savefig("fig.png",bbox_inches='tight')
fig.savefig("fig.pdf",bbox_inches='tight')

