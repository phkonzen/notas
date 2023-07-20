import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
     "text.usetex": True,
     "font.family": "serif",
     "font.size": 12
     })

def euler(f, t0, y0, h, n):
    t = np.empty(n+1)
    m = y0.size
    y = np.empty((n+1, m))

    t[0] = t0
    y[0] = y0

    for k in range(n):
        t[k+1] = t[k] + h
        y[k+1] = y[k] + h*f(t[k], y[k])
    return t, y

def f(t, y):
    v = np.array([y[1], \
                  t*y[1] - y[0] \
                  + (2+t)*np.exp(-t)\
                  - t*np.cos(t)])
    return v


h = 1e-2
tf = 1.
n = round(tf/h)
t0 = 0.
y0 = np.array([1., 0])
t,y = euler(f, t0, y0, h, n)

fig = plt.figure(dpi=300)
ax1 = fig.add_subplot()
#ax2 = ax1.twinx()

# exata
tt = np.linspace(0, tf)
ax1.plot(tt, np.sin(tt) + np.exp(-tt), label='analítica')

ax1.plot(t[::10], y[::10,0],
         ls='--', marker='.', label='$euler$')

ax1.grid()
ax1.legend()
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y(t)$')
plt.savefig('fig.pdf')
plt.savefig('fig.png')
