import numpy as np

def pca2(f, t0, y0, h, n):

    t = np.empty(3)
    t[0] = t0
    y = np.empty(3)
    y[0] = y0

    # inicialização (PM 2)
    y[1] = y[0] + h/2*f(t[0], y[0])
    y[1] = y[0] + h*f(t[0]+h/2, y[1])
    t[1] = t[0] + h

    
    # iterações
    for k in range(1,n):
        
        # preditor (AB 2)
        y[2] = y[1] + h/2*(3*f(t[1],y[1]) \
                             - f(t[0], y[0]))
        t[2] = t[1] + h
        # corretor (AM 2)
        y[2] = y[1] + h/12*(5*f(t[2],y[2]) \
                              + 8*f(t[1], y[1]) \
                              - f(t[0], y[0]))
        
        t[:2] = t[1:]
        y[:2] = y[1:]
        
    return t[2], y[2]

def f(t, y):
    return y + np.sin(t)

# analítica
def exata(t):
    return np.exp(t) - 0.5*np.sin(t) - 0.5*np.cos(t)

h = 1e-1
n = round(1./h)
t,y = pca2(f, 0., 0.5, h, n)
print(f'{h:.1e}: {y:.5e} {np.abs(y-exata(1)):.1e}')
