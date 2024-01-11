from mpi4py import MPI
from dolfinx import mesh

# malha triangular
domain = mesh.create_unit_square(MPI.COMM_WORLD, 
                                 nx = 5, ny = 5)

# gráfico da malha
import pyvista
# pyvista.set_jupyter_backend('static')
print(pyvista.global_theme.jupyter_backend)

from dolfinx import plot
pyvista.start_xvfb()
tdim = domain.topology.dim
topology, cell_types, geometry = plot.vtk_mesh(domain, tdim)
grid = pyvista.UnstructuredGrid(topology, cell_types, geometry)

plotter = pyvista.Plotter()
plotter.add_mesh(grid, show_edges=True)
plotter.view_xy()
pyvista.OFF_SCREEN=True
if not pyvista.OFF_SCREEN:
    plotter.show()
else:
    figure = plotter.screenshot("malha.png")