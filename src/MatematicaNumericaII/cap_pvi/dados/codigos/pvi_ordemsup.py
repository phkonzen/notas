import sympy as sym

t = sym.symbols('t')
y = sym.sin(t) + sym.exp(-t)
rhs = sym.simplify(y.diff(t,2) - t*y.diff(t) + y)
print(rhs)
