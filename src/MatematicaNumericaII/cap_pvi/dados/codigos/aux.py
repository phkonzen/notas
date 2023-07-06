import sympy as sym
y = sym.Function('y')
t = sym.Symbol('t')
eq = sym.Eq(y(t).diff(t), y(t)**2 - t*y(t))
sol = sym.dsolve(eq)
# sol = sym.dsolve(eq, ics={y(1): 0})
print(sol)

import numpy as np

def taylor(Phi, t0, y0, h, n):
    t = t0
    y = y0
    for k in range(n):
        y += h*Phi(t, y, h)
        t += h
    return t, y

def f(t, y):
    return t**2*y

def fl(t, y):
    return 2*t*y + t**2*f(t,y)

def Phi(t, y, h):
    return f(t, y) + h/2*fl(t, y) 

# # analítica
# def exata(t):
#     return 0.5*np.cos(t) - 0.5*np.sin(t)

t0 = 1.
y0 = 0.5
tf = 3.
h = 1e-6
n = round((tf-t0)/h)
t, y = taylor(Phi, t0, y0, h, n)

# import matplotlib.pyplot as plt
# plt.plot(t, np.abs(y - exata(t)), ls='--', marker='.')
# plt.grid()
# plt.show()

print(f'\n{h:.1E}, {y:.5E}')
