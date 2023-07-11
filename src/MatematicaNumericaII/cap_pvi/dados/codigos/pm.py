import numpy as np

def pm(f, t0, y0, h, n):
    t = t0
    y = y0
    for k in range(n):
        ya = y + h/2*f(t, y)
        y += h*f(t+h/2, ya)
        t += h
    return t, y

def f(t, y):
    return y + np.sin(t)

# analítica
def exata(t):
    return np.exp(t) - 0.5*np.sin(t) - 0.5*np.cos(t)

h = 1e-1
n = round(1./h)
t,y = pm(f, 0., 0.5, h, n)
print(f'{h:.1e}: {y:.5e} {np.abs(y-exata(1)):.1e}')
