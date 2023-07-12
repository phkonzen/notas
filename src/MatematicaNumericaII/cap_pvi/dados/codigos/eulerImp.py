import numpy as np
from scipy.optimize import fsolve

def eulerimp(f, t0, y0, h, n):
    t = t0
    y = y0
    for k in range(n):
        y = fsolve(lambda x:
                   x - y - h*f(t+h, x),
                   x0 = y, xtol=1e-14)[0]
        t += h
    return t, y

def f(t, y):
    return y + np.sin(t)

# analítica
def exata(t):
    return np.exp(t) - 0.5*np.sin(t) - 0.5*np.cos(t)

h = 1e-1
n = round(1./h)
t,y = eulerimp(f, 0., 0.5, h, n)
print(f'{h:.1e}: {y:.5e} {np.abs(y-exata(1)):.1e}')
