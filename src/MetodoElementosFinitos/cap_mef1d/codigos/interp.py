from dolfinx import fem, mesh, plot
import numpy as np
import pyvista
from mpi4py import MPI

# malha
msh = mesh.create_interval(MPI.COMM_WORLD,
                           nx=1,
                           points=[0.25, 0.75])

# espaço
V = fem.functionspace(msh, ("P", 1))

# fun
f = lambda x: np.sin(2.*np.pi*x[0])

# pif
pif = fem.Function(V)
pif.interpolate(f)

# grafico
pyvista.start_xvfb()
topology, cell_types, geometry = plot.vtk_mesh(msh, msh.topology.dim)
grid = pyvista.UnstructuredGrid(topology, cell_types, geometry)
plotter = pyvista.Plotter()
plotter.add_mesh(grid, show_edges=True)
plotter.view_xy()
pyvista.OFF_SCREEN=True
if not pyvista.OFF_SCREEN:
    plotter.show()
else:
    figure = plotter.screenshot("tmp/mesh.png")


