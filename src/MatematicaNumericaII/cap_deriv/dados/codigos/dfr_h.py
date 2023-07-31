import numpy as np

def dfr_h(f, x, h=1e-7):
    df = (f(x) - f(x-h))/h
    return df

f = lambda x: np.sin(x)
x = np.pi/3
h = 1e-5
dfdx = dfr_h(f, x, h)
print(f'{h}: dfdx = {dfdx:.5e}, erro = {np.fabs(dfdx-0.5):.1e}')
