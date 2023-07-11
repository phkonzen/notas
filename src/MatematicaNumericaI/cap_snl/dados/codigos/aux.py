import sympy as sym
import numpy as np
import numpy.linalg as npla

xs = np.array([-1., 2])

def newton(F, J, x0, maxiter=100, tol=1.49e-8):
    print(f'\n{0}: x = {x0}, norm = {npla.norm(x0 - xs):.1e}')
    info = -1
    for k in range(maxiter):
        x = x0 - npla.inv(J(x0))@F(x0)
        print(f'{k+1}: x = {x}, norm = {npla.norm(x - xs):.1e}')
        if (npla.norm(x - x0) < tol):
            info = 0
            break
        x0 = x.copy()
    return x, info

def F(x):
    n = x.size
    y = np.empty(n)
    y[0] = x[0]*x[1]**2 - x[0]**2*x[1] + 6
    y[1] = x[0] + x[0]**2*x[1]**3 - 7
    return y

def J(x):
    n = x.size
    y = np.empty((n,n))
    y[0,0] = x[1]**2 - 2*x[0]*x[1]
    y[0,1] = 2*x[0]*x[1] - x[0]**2
    y[1,0] = 1 + 2*x[0]*x[1]**3
    y[1,1] = 3*x[0]**2*x[1]**2
    return y

x0 = np.array([-1.5, 1.5])
x, info = newton(F, J, x0)
        
x,y = sym.symbols('x,y')
p = sym.plot_implicit(sym.Eq(x**2/4+y**2/9, 1), (x,-2,2), (y,-3,3), show=False)
q = sym.plot_implicit(sym.Eq(x, y**2*sym.sqrt(x)), (x,-3,3), (y,-4,4), show=False)
p.extend(q)
p.show()
