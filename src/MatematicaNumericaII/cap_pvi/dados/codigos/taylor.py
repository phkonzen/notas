import numpy as np

def taylor(Phi, t0, y0, h, n):
    t = t0
    y = y0
    for k in range(n):
        y += h*Phi(t, y, h)
        t += h
    return t, y

def f(t, y):
    return y + np.sin(t)

def fl(t, y):
    return f(t, y) + np.cos(t)

def Phi(t, y, h):
    return f(t, y) + h/2*fl(t, y)

# analítica
def exata(t):
    return np.exp(t) - 0.5*np.sin(t) - 0.5*np.cos(t)

h = 1e-1
n = round(1/h)
t,y = taylor(Phi, 0., 0.5, h, n)
