import numpy as np

f = lambda x: np.sin(x+np.pi/4)**2 \
    - x**3 + np.pi/4*x**2 + 5*np.pi**2/16*x \
    + 3*np.pi**3/64

a = 2.
b = 3.
xs = 3.*np.pi/4
x = (a + b)/2
print(f"\n$1$ & ${x0:.4f}$ & ${np.fabs(x - xs):.1e}$")
for k in range(9):
    s = np.sign(f(a)*f(x))
    if (s == -1):
        b = x
    elif (s == 1):
        a = x
    else:
        break
    x = (a + b)/2
    print(f"${k+2}$ & ${x:.4f}$ & ${np.fabs(x-xs):.1e}$")
    
    

