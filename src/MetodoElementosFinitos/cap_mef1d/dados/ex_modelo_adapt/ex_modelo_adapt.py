from __future__ import print_function, division
from fenics import *
import numpy as np
import matplotlib.pyplot as plt

# malha
mesh = IntervalMesh(10,0,1)

# espaco
V = FunctionSpace(mesh, 'P', 1)

# fonte
f = Expression('exp(-100*pow(fabs(x[0]-0.5),2))',degree=1)

# condicoes de contorno
def boundary(x,on_boundary):
    return on_boundary

#iteracoes
for iter in np.arange(6):

    #problema
    bc = DirichletBC(V,Constant(0.0),boundary)
    u = TrialFunction(V)
    v = TestFunction(V)
    a = u.dx(0)*v.dx(0)*dx
    L = f*v*dx

    #resolve
    u = Function(V)
    solve(a == L, u, bc)

    #grafico
    plt.close('all')
    xx = mesh.coordinates()[:,0]
    sorted_indices =  np.argsort(xx)
    yy = u.compute_vertex_values()
    plt.plot(xx[sorted_indices],yy[sorted_indices],
                 marker="o",label=r"$u_h$")
    plt.legend(numpoints=1)
    plt.grid('on')
    plt.show()

    DG = FunctionSpace(mesh, "DG", 0)
    v = TestFunction(DG)
    a = CellVolume(mesh)
    eta = assemble(f**2*v*a*dx).array()

    # refinamento da malha
    cell_markers = MeshFunction("bool", mesh, mesh.topology().dim(), False)
    eta_max = np.amax(eta)
    print("%d %d %1.1E\n" % (iter,mesh.num_cells(),eta_max))
    alpha = 0.5
    for i,cell in enumerate(cells(mesh)):
        if (eta[i] > alpha*eta_max):
            cell_markers[cell] = True

    mesh = adapt(mesh, cell_markers)
    V = adapt(V,mesh)
