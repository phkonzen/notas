import numpy as np

def euler(f, t0, y0, h, n):
    t = np.empty(n+1)
    t[0] = t0
    y = np.empty(n+1)
    y[0] = y0
    for k in range(n):
        t[k+1] = t[k] + h
        y[k+1] = y[k] + h*f(t[k], y[k])
    return t, y

def f(t, y):
    return np.pi*(np.cos(np.pi*t)**2 - np.sin(np.pi*t)**2)

# analítica
def exact(t):
    return np.sin(np.pi*t)*np.cos(np.pi*t)

h = 1e-1
n = 15
t,y = euler(f, 0., 0., h, n)
