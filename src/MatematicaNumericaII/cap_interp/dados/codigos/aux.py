import numpy as np
import scipy.integrate as scint

# intervalo
a = np.pi/6
b = np.pi/4
# fun
f = lambda x: np.exp(-x)*np.cos(x)

Ie = scint.quad(f, a, b)[0]
print(Ie)

# quad
h = b-a
Iq = h*f((a+b)/2)
print(f'Iq = {Iq:.5e}, err = {np.fabs(Iq-Ie):.1e}')

xx = np.linspace(2., 2.4, 5)
yy = np.array([1.86, 1.90, 2.01, 2.16, 2.23])
h = 0.4/2
tI = h/3*(yy[0] + 4*yy[2] + yy[4])
print(f'{tI:.5e}')
h = 0.2/2
tI1 = h/3*(yy[0] + 4*yy[1] + yy[2])
print(f'{tI1:.5e}')
h = 0.2/2
tI2 = h/3*(yy[2] + 4*yy[3] + yy[4])
print(f'{tI2:.5e}')
print(f'{tI1+tI2:.5e}')
