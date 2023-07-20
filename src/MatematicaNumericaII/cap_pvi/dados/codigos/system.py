import sympy as sym

t,y1,y2 = sym.symbols('t,y1,y2')

# manu sol
y1 = sym.exp(t) - 2*sym.exp(-t) + sym.cos(t)
y2 = 2*sym.exp(t) + sym.exp(-t)

# rhs
print('rhs1')
print(y1.diff(t) + y1 - y2)
print('rhs2')
print(y2.diff(t) - 2*y1 - 3*y2)
