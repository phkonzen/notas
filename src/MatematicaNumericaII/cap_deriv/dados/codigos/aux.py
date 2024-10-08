import numpy as np

def d2fc_h2(f, x, h=1e-7):
    df = (f(x+h) - 2*f(x) + f(x-h))/h**2
    return df

f = lambda x: np.exp(x)*np.log(x+1)-x
x = 1.
h = 1e-3
d2fdx2 = d2fc_h2(f, x, h)
print(f'{h}: d2fdx2 = {d2fdx2:.5e}')
