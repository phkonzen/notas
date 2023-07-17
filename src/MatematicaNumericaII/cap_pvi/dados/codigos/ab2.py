import numpy as np

def ab2(f, t0, y0, h, n):

    # inicialização
    y1 = y0 + h/2*f(t0, y0)
    y1 = y0 + h*f(t0+h/2, y1)
    t1 = t0 + h

    # iterações
    for k in range(1,n):
        y = y1 + h/2*(3*f(t1, y1) \
                  - f(t0, y0))
        t = t1 + h
        
        t0 = t1
        y0 = y1
        
        t1 = t
        y1 = y
        
    return t, y

def f(t, y):
    return y + np.sin(t)

# analítica
def exata(t):
    return np.exp(t) - 0.5*np.sin(t) - 0.5*np.cos(t)

h = 1e-1
n = round(1./h)
t,y = ab2(f, 0., 0.5, h, n)
print(f'{h:.1e}: {y:.5e} {np.abs(y-exata(1)):.1e}')
