from dolfinx import fem, mesh, plot
import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

# malha
msh = mesh.create_interval(MPI.COMM_WORLD,
                           nx=1,
                           points=np.array([0.25, 0.75]))

# espaço
V = fem.FunctionSpace(msh, ('Lagrange', 1))

# fun interpolada
pif = fem.Function(V)
pif.interpolate(lambda x: 3.*np.sin(2.*np.pi*x[0]))

# grafico
fig = plt.figure(dpi=300)
ax = fig.add_subplot()
xx = np.linspace(0.25, 0.75)
ax.plot(xx, 3.*np.sin(2.*np.pi*xx), label="$f$")
ax.plot([0.25, 0.75], pif.x.array.real, marker="o", label="$\pi f$")
ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
plt.savefig("fig.png", bbox_inches='tight')
plt.savefig("fig.pdf", bbox_inches='tight')
