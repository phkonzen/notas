import numpy as np

# f = lambda x: np.sin(x+np.pi/4)**2 \
#     - x**3 + np.pi/4*x**2 + 5*np.pi**2/16*x \
#     + 3*np.pi**3/64

f = lambda x: (-x**2+1.154*x-0.332929)*np.cos(x) + x**2 - 1.154*x + 0.332929

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

    

