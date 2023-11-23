from dolfinx import fem, mesh
import ufl
import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt

# malha
l0 = 0.25
l1 = 0.75
domain = mesh.create_interval(MPI.COMM_WORLD,
                              nx = 5,
                              points = [l0, l1])
x = ufl.SpatialCoordinate(domain)

# espaço
V = fem.FunctionSpace(domain, ('P', 1))

# fun
def fun(x, mod):
    return 3.*mod.sin(2.*mod.pi*x)

x = ufl.SpatialCoordinate(domain)
f_expr = fem.Expression(fun(x[0], ufl),
                        V.element.interpolation_points())

# interpolação
pif = fem.Function(V)
pif.interpolate(f_expr)

# gráfico
fig = plt.figure()
ax = fig.add_subplot()

# fun
xx = np.linspace(l0, l1)
ax.plot(xx, fun(xx, np), color='C0', label='$f$')

# vértices
x = V.tabulate_dof_coordinates()
x_order = np.argsort(x[:,0])
ax.plot(x[x_order, 0], pif.x.array[x_order],
        ls='-', marker='o', color='C1', label='$\pi f$')

ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')
