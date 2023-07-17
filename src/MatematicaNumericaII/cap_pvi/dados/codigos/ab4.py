import numpy as np

def ab4(f, t0, y0, h, n):

    t = np.empty(5)
    t[0] = t0
    y = np.empty(5)
    y[0] = y0
    
    # inicialização
    for k in range(3):
        phi1 = f(t[k], y[k])
        phi2 = f(t[k]+h/2, y[k] + h*phi1/2)
        phi3 = f(t[k]+h/2, y[k] + h*phi2/2)
        phi4 = f(t[k]+h, y[k] + h*phi3)

        y[k+1] = y[k] + h/6 \
            * (phi1 + 2*phi2 + 2*phi3 + phi4)
        t[k+1] = t[k] + h

    # iterações
    for k in range(3,n):
        y[4] = y[3] + h/24*(55*f(t[3], y[3]) \
                            - 59*f(t[2], y[2]) \
                            + 37*f(t[1], y[1]) \
                            - 9*f(t[0], y[0]))
        t[4] = t[3] + h
        
        t[:4] = t[1:]
        y[:4] = y[1:]
        
    return t[4], y[4]

def f(t, y):
    return y + np.sin(t)

# analítica
def exata(t):
    return np.exp(t) - 0.5*np.sin(t) - 0.5*np.cos(t)

h = 1e-3
n = round(1./h)
t,y = ab4(f, 0., 0.5, h, n)
print(f'{h:.1e}: {y:.5e} {np.abs(y-exata(1)):.1e}')
