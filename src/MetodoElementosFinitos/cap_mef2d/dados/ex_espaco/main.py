from mpi4py import MPI
from dolfinx import mesh

# malha
domain = mesh.create_unit_square(MPI.COMM_WORLD, 5, 5)

from dolfinx import fem

# espaço de elementos finitos
V = fem.functionspace(domain, ("P",1))

# função do espaço V
uh = fem.Function(V)

# valor nodais
from numpy import sin, pi
for i,x in enumerate(domain.geometry.x):
  uh.x.array[i] = sin(pi*x[0])*sin(pi*x[1])

# gráfico
import pyvista
from dolfinx import plot
u_topology, u_cell_types, u_geometry = plot.vtk_mesh(V)
u_grid = pyvista.UnstructuredGrid(u_topology, u_cell_types, u_geometry)
u_grid.point_data["u"] = uh.x.array.real
u_grid.set_active_scalars("u")
u_plotter = pyvista.Plotter()
u_plotter.add_mesh(u_grid, show_edges=True)
u_plotter.view_xy()
if not pyvista.OFF_SCREEN:
  u_plotter.show()
else:
  figure = u_plotter.screenshot("u.png")
