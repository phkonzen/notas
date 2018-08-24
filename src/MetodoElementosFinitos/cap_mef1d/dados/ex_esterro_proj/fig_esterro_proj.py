from __future__ import print_function, division
from fenics import *
import numpy as np
import matplotlib.pyplot as plt

# funcao
f = Expression('3*sin(2*pi*x[0])',
               degree=10)

n=5
el = []
hl = []
for k in np.arange(0,n):
    mesh = IntervalMesh(5*10**k,0.25,0.75)
    h = mesh.hmax()
    V = FunctionSpace(mesh, 'P', 1)
    Phf = project(f,V)
    e = errornorm(f,Phf,'L2')

    print("%d %1.0E %1.1E" % (k,h,e))
    hl.append(h)
    el.append(e)
    
# grafico
plt.plot(hl,el,marker='o')
plt.xlim(10**-1,10**-n)
plt.xscale('log')
plt.xlabel('$h$')
plt.yscale('log')
plt.ylabel('$\|f-P_h f\|_{L^2}$')
plt.grid()
plt.show()
# xx = IntervalMesh(100,0.25,0.75)
# plot(f,mesh=xx,label="$f$")
# plot(f,mesh=mesh,
#      marker='o',label="$\pi f$")
# plt.legend(numpoints=1)
# plt.grid('on')
# plt.show()
