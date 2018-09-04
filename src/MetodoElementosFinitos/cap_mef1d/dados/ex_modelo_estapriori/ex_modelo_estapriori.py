from __future__ import print_function, division
from fenics import *
import numpy as np
import matplotlib.pyplot as plt

#sol analitica
ua = Expression('-x[0]*x[0]/2+x[0]/2',
               degree=2)

for n in [2,4,8,16,32,64,128]:

    # malha
    mesh = IntervalMesh(n,0,1)

    # espaco
    V = FunctionSpace(mesh, 'P', 1)

    # condicoes de contorno
    def boundary(x,on_boundary):
        return on_boundary

    bc = DirichletBC(V,Constant(0.0),boundary)

    #MEF problem
    u = TrialFunction(V)
    v = TestFunction(V)
    f = Constant(1.0)
    a = dot(grad(u), grad(v))*dx
    L = f*v*dx

    #computa a sol
    uh = Function(V)
    solve(a == L, u, bc)

    e = errornorm(u,ua,'')

#grafico
#plot(u,marker="o",label="$u_h$")

xx = IntervalMesh(100,0,1)
plot(ua,mesh=xx,label="$u$")
plt.legend(numpoints=1)
plt.grid('on')
plt.show()
