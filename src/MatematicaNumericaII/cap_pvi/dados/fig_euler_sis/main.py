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
    v = np.array([-y[0] + y[1] \
                  - np.exp(-t) \
                  + np.cos(t) \
                  - np.sin(t), \
                  2*y[0] + 3*y[1]
                  - 6*np.exp(t)
                  - 2*np.cos(t)])
    return v


h = 1e-2
n = round(1./h)
t0 = 0.
y0 = np.array([0., 3.])
t,y = euler(f, t0, y0, h, n)

fig = plt.figure(dpi=300)
ax1 = fig.add_subplot()
#ax2 = ax1.twinx()

ax1.plot(t[::10], y[::10,0],
         ls='--', marker='.',
         color = 'blue', label='$y_1$')
ax1.plot(t[::10], y[::10,1],
         ls='--', marker='.',
         color = 'red', label='$y_2$')

# # exata
t = np.linspace(0, 1.)
ax1.plot(t, np.exp(t) - 2*np.exp(-t) + np.cos(t),
         color = 'blue')
ax1.plot(t, 2*np.exp(t) + np.exp(-t),
         color = 'red')

ax1.grid()
ax1.legend()
ax1.set_xlabel('$t$')
ax1.set_ylabel('$y_{1,2}(t)$')
plt.savefig('fig.pdf')
plt.savefig('fig.png')
