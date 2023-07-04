import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

def f(t, y):
    return y + np.sin(t)

def euler(f, t0, y0, h, n):
    t = np.empty(n+1)
    t[0] = t0
    y = np.empty(n+1)
    y[0] = y0
    for k in range(n):
        t[k+1] = t[k] + h
        y[k+1] = y[k] + h*f(t[k], y[k])
    return t, y

# analítica
def exact(t):
    return np.exp(t) - 0.5*np.sin(t) - 0.5*np.cos(t)


fig = plt.figure(dpi=300)
ax = fig.add_subplot()

h = 1e-1
t,y = euler(f, 0., 0.5, h, 10)
plt.plot(t, y, ls='--', marker='.', label='$h=0.1$')

# exata
t = np.linspace(0, 1.)
y = exact(t)
plt.plot(t, y, ls='-', label='exata')

ax.legend()
ax.set_xlabel('$t$')
ax.set_ylabel('$y(t)$')
ax.grid()
fig.savefig('fig.pdf')
fig.savefig('fig.png')
