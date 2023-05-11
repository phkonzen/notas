import numpy as np

f = lambda x: np.sin(x+np.pi/4)**2 \
    - x**3 + np.pi/4*x**2 + 5*np.pi**2/16*x \
    + 3*np.pi**3/64

a = 2
b = 3
x = (a + b)/2
print(f"0: a={a:.4f}, b={b:.4f}, x={x:.4f}")
for k in range(10):
    s = np.sign(f(a)*f(x))
    if (s == -1):
        b = x
    elif (s == 1):
        a = x
    else:
        break
    x = (a + b)/2
    print(f"{k+1}: a={a:.4f}, b={b:.4f}, x={x:.4f}")
    

