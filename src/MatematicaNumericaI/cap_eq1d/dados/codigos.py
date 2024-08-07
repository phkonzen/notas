import numpy as np
import matplotlib.pyplot as plt

# fun obj
f = lambda x: np.sin(x+np.pi/4)**2 \
    - x**3 + np.pi/4*x**2 + 5*np.pi**2/16*x \
    + 3*np.pi**3/64

x0 = 2.6
x1 = 2.5
print(f'\n0: {x0:.4f}, {x1:.4f}')
for k in range(5):
    x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    x0 = x1
    x1 = x
    print(f'{k+1}: {x0:.4f}, {x1:.4f}, {np.fabs(x1-x0):.1e}')


fl = lambda x: -3*x**2 + np.pi*x/2 + \
    2*np.sin(x + np.pi/4)*np.cos(x + np.pi/4) + 5*np.pi**2/16

fll = lambda x: -6*x - 2*np.sin(x + np.pi/4)**2 \
    + 2*np.cos(x + np.pi/4)**2 + np.pi/2

