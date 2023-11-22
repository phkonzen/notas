from dolfinx import fem, mesh
from dolfinx.fem.petsc import LinearProblem
import ufl
import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

# malha
msh = mesh.create_interval(MPI.COMM_WORLD,
                           nx=4,
                           points=[0.25, 0.75])

# espaço
V = fem.functionspace(msh, ("P", 1))


# pif = fem.Function(V)
# f = lambda x: 3.*np.sin(2.*np.pi*x[0])
# pif.interpolate(f)

x = ufl.SpatialCoordinate(msh)
f = 3.*ufl.sin(2.*ufl.pi*x[0])

# project f
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)
a =  ufl.dot(u, v) * ufl.dx
L = ufl.dot(f, v) * ufl.dx
problem = LinearProblem(a, L, bcs=[])
fh = problem.solve()

# gráfico
fig = plt.figure(dpi=300)
ax = fig.add_subplot()
xx = np.linspace(0.25, 0.75)
ax.plot(xx, 3.*np.sin(2.*np.pi*xx), label="$f$")
ax.plot(msh.geometry.x[:,0:1], fh.x.array, marker="o", label="$P_hf$")
ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
plt.savefig("fig.png", bbox_inches='tight')
plt.savefig("fig.pdf", bbox_inches='tight')




