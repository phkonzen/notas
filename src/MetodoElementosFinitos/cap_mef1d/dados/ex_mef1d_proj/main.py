from dolfinx import fem, mesh
from dolfinx.fem.petsc import LinearProblem
import ufl
from mpi4py import MPI

# malha
l0 = 0.25
l1 = 0.75
domain = mesh.create_interval(MPI.COMM_WORLD,
                              nx=5,
                              points=[l0, l1])
x = ufl.SpatialCoordinate(domain)

# espaço
V = fem.functionspace(domain, ("P", 1))

# fun
f = 3.*ufl.sin(2.*ufl.pi*x[0])

# project f
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)
a =  ufl.dot(u, v) * ufl.dx
L = ufl.dot(f, v) * ufl.dx
problem = LinearProblem(a, L, bcs=[])
Phf = problem.solve()

# gráfico
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(dpi=300)
ax = fig.add_subplot()
xx = np.linspace(0.25, 0.75)
yy = 3.*np.sin(2.*np.pi*xx)
ax.plot(xx, yy, label="$f$")
ax.plot(domain.geometry.x[:,0], Phf.x.array,
        ls='-', marker="o", label="$P_hf$")
ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
plt.savefig("fig.png", bbox_inches='tight')
plt.savefig("fig.pdf", bbox_inches='tight')
