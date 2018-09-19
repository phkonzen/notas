from __future__ import print_function, division
from fenics import *
import numpy as np
import matplotlib.pyplot as plt

def boundary(x,on_boundary):
    return on_boundary

def solver(n):
    # malha
    mesh = IntervalMesh(n,0,1)

    # espaco
    V = FunctionSpace(mesh, 'P', 1)

    bc = DirichletBC(V,Constant(0.0),boundary)

    #MEF problem
    u = TrialFunction(V)
    v = TestFunction(V)
    f = Constant(1.0)
    a = dot(grad(u), grad(v))*dx
    L = f*v*dx

    #computa a sol
    u = Function(V)
    solve(a == L, u, bc)

    return u

#sol analitica
ua = Expression('-x[0]*x[0]/2+x[0]/2',
                degree=2)


lerrors=[]
for n in [2,4,8,16,32,64,128]:
    u = solver(n)
    e = errornorm(u,ua,norm_type='H10')
    lerrors.append(e)

plt.plot([2,4,8,16,32,64,128],lerrors)
plt.xscale('log',base=2)
#plt.yscale('log',base=2)
plt.xlabel(r"$n$")
plt.ylabel(r"$\|(u-u_h)'\|_{L^2(I)}$")
plt.xlim((2,128))
plt.xticks([2,4,8,16,32,64,128],[2,4,8,16,32,64,128])
plt.grid('on')
plt.show()
