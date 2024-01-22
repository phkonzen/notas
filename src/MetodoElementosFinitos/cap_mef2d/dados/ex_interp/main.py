from mpi4py import MPI
from dolfinx import mesh

# malha
domain = mesh.create_unit_square(MPI.COMM_WORLD, 16, 16)

from dolfinx import fem

# espaço de elementos finitos
V = fem.functionspace(domain, ("P",1))

# função do espaço V
uh = fem.Function(V)

# interpolate
import numpy as np
def u(x, mod=np):
    return mod.sin(mod.pi*x[0])*mod.sin(mod.pi*x[1])

uh.interpolate(lambda x: u(x))

# eval fun
from dolfinx import geometry

def fun_eval(u, points,
             domain=domain):
  u_values = []
  bb_tree = geometry.bb_tree(domain, domain.topology.dim)
  cells = []
  points_on_proc = []
  # Find cells whose bounding-box collide with the the points
  cell_candidates = geometry.compute_collisions_points(bb_tree, 
                                                       points.T)
  # Choose one of the cells that contains the point
  colliding_cells = geometry.compute_colliding_cells(domain, 
                                                     cell_candidates, 
                                                     points.T)
  for i, point in enumerate(points.T):
    if len(colliding_cells.links(i)) > 0:
      points_on_proc.append(point)
      cells.append(colliding_cells.links(i)[0])

  points_on_proc = np.array(points_on_proc, dtype=np.float64)
  u_values = u.eval(points_on_proc, cells)
  return u_values

# gráfico
import numpy as np
nx = ny = 101
xx0 = np.linspace(0., 1., nx)
xx1 = np.linspace(0., 1., ny)
X0, X1 = np.meshgrid(xx0, xx1, indexing='ij')
points = np.zeros((3, nx*ny))
points[0] = X0.reshape(-1)
points[1] = X1.reshape(-1)

yh = fun_eval(uh, points)
Yh = yh.reshape((nx,ny))

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()
levels=10
cb = ax.contourf(X0, X1, Yh, levels = levels)
fig.colorbar(cb)
Y = u([X0, X1])
cl = ax.contour(X0, X1, Y, levels = levels, colors='w')
ax.clabel(cl)
plt.savefig('fig.pdf', bbox_inches='tight')
plt.savefig('fig.png', bbox_inches='tight')
plt.show()

# # L2-norm
# from scipy.integrate import dblquad
# l2_err = dblquad(lambda y,x: (fun_eval(uh, 
#                                        np.array([[x],[y],[0]]))
#                               - u(np.array([x,y,0])))**2, 
#                  0., 1., 0., 1.)[0]