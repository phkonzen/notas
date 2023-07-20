import numpy as np
import numpy.linalg as npla

def euler(f, t0, y0, h, n):
    t = t0
    y = y0.copy()

    for k in range(n):
        y += h*f(t, y)
        t += h
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

def exata(t):
    v = np.array([np.exp(t) \
                  - 2*np.exp(-t) \
                  + np.cos(t),
                  2*np.exp(t) \
                  + np.exp(-t)])
    return v


h = 1e-6
n = round(1./h)
t0 = 0.
y0 = np.array([0., 3.])
t,y = euler(f, t0, y0, h, n)
np.set_printoptions(precision=3)
print(f'{h:.1e}: {y}, {npla.norm(y-exata(1)):.1e}')
