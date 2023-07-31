import numpy as np

def dfc_h2(f, x, h=1e-7):
    df = (f(x+h) - f(x-h))/(2*h)
    return df

def dfr_h2(f, x, h=1e-7):
    df = 1/(2*h)*(3*f(x) - 4*f(x-h) + f(x-2*h))
    return df

def dfp_h2(f, x, h=1e-7):
    df = 1/(2*h)*(-3*f(x) + 4*f(x+h) - f(x+2*h))
    return df

f = lambda x: np.cos(x)
x = np.linspace(2,2.5,6)
y = np.array([1.86,
              1.90,
              2.01,
              2.16,
              2.23,
              2.31])
df1 = 1/0.2*(-3*y[0] + 4*y[1] - y[2])
print(df1)
df2 = 1/0.2*(3*y[5] - 4*y[4] + y[3])
print(df2)
