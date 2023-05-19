import matplotlib.pyplot as plt
import numpy as np

xx = np.linspace(-1.5, 1.5)
plt.plot(xx, xx**2*np.exp(-xx**2))
plt.plot(xx, xx)
plt.show()

import numpy as np

# fun obj
f = lambda x: np.sin(x+np.pi/4)**2 \
    - x**3 + np.pi/4*x**2 + 5*np.pi**2/16*x \
    + 3*np.pi**3/64

fl = lambda x: 2*np.sin(x+np.pi/4)*np.cos(x+np.pi/4) \
    -3*x**2 + np.pi/2*x + 5*np.pi**2/16

# param
alpha = 0.1
# fun pto fixo
g = lambda x: x - alpha*fl(x)

xx = np.linspace(-1, 0)
plt.plot(xx, xx)
plt.plot(xx, g(xx))
plt.plot([-np.pi/4], [g(-np.pi/4)], marker='o')
plt.grid()
plt.show()


# aprox inicial
x0 = -0.5
print(f'\n{1}: {x0:.4f}')
for k in range(4):
    x = g(x0)
    nd = np.fabs(x-x0)
    print(f'{k+2}: {x:.4f}, {nd:.1e}')
    x0 = x



xx = np.linspace(0.55, 0.65)
yy = f(xx)
plt.plot(xx, yy)
plt.show()

a = 0.55
b = 0.65
x0 = a - (b-a)/(f(b)-f(a))*f(a)
print(f"{k+1}: {x0:.4f}")
for k in range(100):
    
    s = np.sign(f(a)*f(x0))
    if (s == -1):
        b = x0
    elif (s == 1):
        a = x0
    else:
        break

    x = a - (b-a)/(f(b)-f(a))*f(a)
    
    print(f"{k+2}: {x:.6f}")
    
    if np.fabs(x - x0) < 1e-4:
        break
    x0 = x

    

g = lambda x: 16/(5*np.pi**2)*(-np.sin(x+np.pi/4)**2 \
                               + x**3 - np.pi/4*x**2 - 3*np.pi**2/64)
x = 0.7
print('\n{1}: {x:.5f}')
for k in range(20000):
