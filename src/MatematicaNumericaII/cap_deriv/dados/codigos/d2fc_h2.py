import numpy as np

def d2fc_h2(f, x, h=1e-7):
    df = (f(x+h) - 2*f(x) + f(x-h))/h**2
    return df

f = lambda x: x**2 + np.sin(x)
x = np.pi/6
h = 1e-1
d2fdx2 = d2fc_h2(f, x, h)
print(f'{h}: d2fdx2 = {d2fdx2:.5e}, erro = {np.fabs(d2fdx2-1.5):.1e}')
