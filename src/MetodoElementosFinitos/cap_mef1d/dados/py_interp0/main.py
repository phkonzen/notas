from dolfinx import fem, mesh, plot, geometry
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


points = np.array([[0.5, 0., 0.]])
cells = []
points_on_proc = []
bb_tree = geometry.bb_tree(msh, msh.topology.dim)
cell_candidates = geometry.compute_collisions_points(bb_tree, points)
colliding_cells = geometry.compute_colliding_cells(msh, cell_candidates, points)
for i, point in enumerate(points):
    if len(colliding_cells.links(i)) > 0:
        points_on_proc.append(point)
        cells.append(colliding_cells.links(i)[0])
points_on_proc = np.array(points_on_proc, dtype=np.float64)
pif_values = pif.eval(points_on_proc, cells)

