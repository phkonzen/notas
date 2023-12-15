'''
Exact solution for the Fisher eq

$$u_t = u_xx + lmbda*u(1-u)$$
'''
import sympy as sp

t,x = sp.symbols('t x')
lmbda = sp.symbols('lmbda', constant=True)

# solução
lmbda = 6.
u = 1./(1.+sp.exp(sp.sqrt(lmbda/6)*x-5./6*lmbda*t))**2

# verificação
u_t = sp.diff(u,t)
u_xx = sp.diff(u, x, 2)

sol = sp.simplify(u_t-u_xx-lmbda*u*(1-u))
print(sol)

# c.c.
u_x = sp.diff(u,x)
print(f'u_x(t,0) = {u_x.subs(x,0)}')
print(f'u_x(t,1) = {u_x.subs(x,1)}')
