from dolfinx import fem, mesh, plot
import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

# malha
msh = mesh.create_interval(MPI.COMM_WORLD,
                           nx=1,
                           points=np.array([0.25, 0.75]))

# espaço
V = fem.functionspace(msh, ('Lagrange', 1))

# fun interpolada
pif = fem.Function(V)
pif.interpolate(lambda x: 3.*np.sin(2.*np.pi*x[0]))
