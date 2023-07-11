import numpy as np

def rk4(f, t0, y0, h, n):
    t = t0
    y = y0
    for k in range(n):
        phi1 = f(t, y)
        phi2 = f(t + h/2, y + h/2*phi1)
        phi3 = f(t + h/2, y + h/2*phi2)
        phi4 = f(t + h, y + h*phi3)
        
        y += h/6 * (phi1 + 2*phi2 + 2*phi3 + phi4)
        t += h
    return t, y

def f(t, y):
    return y + np.sin(t)

# analítica
def exata(t):
    return np.exp(t) - 0.5*np.sin(t) - 0.5*np.cos(t)

h = 1e-4
n = round(1./h)
t,y = rk4(f, 0., 0.5, h, n)
print(f'{h:.1e}: {y:.5e} {np.abs(y-exata(1)):.1e}')
