from __future__ import print_function, division
from fenics import *
import numpy as np
import matplotlib.pyplot as plt

#tolerance
tol=1e-14

# malha
mesh = IntervalMesh(10,0,pi/2)

# espaco
V = FunctionSpace(mesh, 'P', 1)

u_D = Expression('x[0]<pi/4 ? -0.3 : -0.1',degree=1)

def boundary(x,on_boundary):
    return on_boundary

bc = DirichletBC(V,u_D,boundary)

#MEF problem
u = TrialFunction(V)
v = TestFunction(V)
f = Expression('-cos(x[0])',degree=2)
a = u.dx(0)*v.dx(0)*dx
b = u.dx(0)*v * dx
c = 2* u * v * dx
L = f*v*dx

#computa a sol
u = Function(V)
solve(a+b+c == L, u, bc)

#sol analitica
ua = Expression('-0.1*(sin(x[0])+3*cos(x[0]))',
                degree=2)

#erro L2
print("Erro L2: %1.2E\n" % errornorm(u,ua,norm_type="L2"))

plot(u,mesh=mesh,marker='o',label=r"$u_h$")
mesh = IntervalMesh(100,0,pi/2)
plot(ua,mesh=mesh,label=r"$u$")
plt.legend(numpoints=1,loc='upper left')
plt.grid('on')
plt.show()
