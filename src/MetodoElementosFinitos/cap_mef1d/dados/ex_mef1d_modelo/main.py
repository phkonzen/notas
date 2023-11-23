from mpi4py import MPI

# malha
from dolfinx import mesh
domain = mesh.create_unit_interval(MPI.COMM_WORLD,
                                   nx = 5)
# espaço
from dolfinx import fem
V = fem.functionspace(domain, ('P', 1))

# condição de contorno
import numpy as np
uD = fem.Function(V)
uD.interpolate(lambda x: np.full(x.shape[1], 0.))

tdim = domain.topology.dim
fdim = tdim - 1
domain.topology.create_connectivity(fdim, tdim)
boundary_facets = mesh.exterior_facet_indices(domain.topology)
boundary_dofs = fem.locate_dofs_topological(V, fdim,
                                            boundary_facets)
bc = fem.dirichletbc(uD, boundary_dofs)

# problema mef
import ufl
from dolfinx import default_scalar_type
from dolfinx.fem.petsc import LinearProblem
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)

f = fem.Constant(domain, default_scalar_type(1.))

a = ufl.dot(ufl.grad(u), ufl.grad(v)) * ufl.dx
L = f * v * ufl.dx

problem = LinearProblem(a, L, bcs=[bc])
uh = problem.solve()

# gráfico
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot()

# sol analítica
def ua(x):
    return 0.5*(x - x**2)

xx = np.linspace(0., 1.)
yy = ua(xx)
ax.plot(xx, yy, label='$u$')
ax.plot(domain.geometry.x[:,0], uh.x.array,
        marker='o', label='$u_h$')
ax.legend()
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')

