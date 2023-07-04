import math as m
import numpy as np

def euler(f, t0, y0, h, n):
    t = t0
    y = y0
    for k in range(n):
        y += h*f(t, y)
        t += h
        # print(k+1, t, y)
    return t, y

def f(t, y):
    return -30*y

def exata(t):
    return 1./3*np.exp(-30*t)

h = 1e-1
n = round(1/h)
t,y = euler(f, 0., 1./3, h, n)
print(f'{h}: {t}, {y:.5E}, {np.abs(y - exata(1.5)):.1E}')
#print(f'{h}: {t}, {y:.4E}')
