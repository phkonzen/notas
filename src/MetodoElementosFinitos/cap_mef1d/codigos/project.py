from dolfinx import fem, mesh
from dolfinx.fem.petsc import LinearProblem
import ufl
import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

# malha
msh = mesh.create_interval(MPI.COMM_WORLD,
                           nx=10,
                           points=[0.25, 0.75])

# espaço
V = fem.functionspace(msh, ("P", 1))

# fun
pif = fem.Function(V)
f = lambda x: 3.*np.sin(2.*np.pi*x[0])
pif.interpolate(f)

# project f
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)
a =  ufl.dot(u, v) * ufl.dx
L = ufl.dot(pif, v) * ufl.dx
problem = LinearProblem(a, L, bcs=[])
fh = problem.solve()

# gráfico
# grafico
fig = plt.figure(dpi=300)
ax = fig.add_subplot()
xx = np.linspace(0.25, 0.75)
ax.plot(xx, 3.*np.sin(2.*np.pi*xx), label="$f$")
ax.plot(msh.geometry.x[:,0:1], pif.x.array.real, marker="o", label="$\pi f$")
ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
plt.savefig("fig.png", bbox_inches='tight')
plt.savefig("fig.pdf", bbox_inches='tight')




