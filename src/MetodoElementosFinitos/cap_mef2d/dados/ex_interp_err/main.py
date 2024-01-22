from mpi4py import MPI
from dolfinx import mesh

# malha
domain = mesh.create_unit_square(MPI.COMM_WORLD, 64, 64)

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
bb_tree = geometry.bb_tree(domain, domain.topology.dim)

def fun_eval(u, points,
             domain=domain,
             bb_tree = bb_tree):
  u_values = []
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


# erro L2
import dolfinx.cpp as cpp
from scipy.integrate import dblquad

# mesh size
tdim = domain.topology.dim
num_cells = domain.topology.index_map(tdim).size_local
msh = cpp.mesh.Mesh_float64(MPI.COMM_WORLD, 
                                    domain.topology, 
                                    domain.geometry)
h = cpp.mesh.h(msh, tdim, range(num_cells))
  
# erro L2
l2_err = dblquad(lambda y,x: (fun_eval(uh, 
                              np.array([[x],[y],[0]]))
                            - u(np.array([x,y,0])))**2, 
                0., 1., 0., 1.)[0]
l2_err = np.sqrt(l2_err)
print(f'h = {h.max():.1e}, l2_err = {l2_err:.1e}')

