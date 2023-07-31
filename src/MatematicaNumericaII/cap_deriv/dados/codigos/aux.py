import numpy as np

def dfc_h2(f, x, h=1e-7):
    df = (f(x+h) - f(x-h))/(2*h)
    return df

def dfr_h(f, x, h=1e-7):
    df = (f(x) - f(x-h))/h
    return df

def dfp_h(f, x, h=1e-7):
    df = (f(x+h) - f(x))/h
    return df

f = lambda x: np.cos(x)
x = np.pi/3
h = 1e-3
dfdx = dfc_h2(f, x, h)
print(f'{h}: dfdx = {dfdx:.5e}, erro = {np.fabs(dfdx-0.5):.1e}')
