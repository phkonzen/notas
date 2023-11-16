from dolfinx import fem, mesh, geometry
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

# funcao
def fun(x):
    x = np.asarray(x).reshape(-1,1)
    return 3.*np.sin(2.*np.pi*x[0])

# eval fem fun
def fem_fun_eval(x, f, msh):
  # ptos
  x = np.asarray(x)
  npts = x.size
  # 1d ptos
  points = np.hstack((x.reshape(-1,1),
                      np.zeros((npts,2))))
  # bounding box tree
  bb_tree = geometry.bb_tree(msh, msh.topology.dim)
  # localizando a célula
  cell_candidates = geometry.compute_collisions_points(bb_tree, points)
  colliding_cells = geometry.compute_colliding_cells(msh,
                                                     cell_candidates,
                                                     points)
  # pontos e células nessa proc
  points_on_proc = []
  cells = []
  for i, point in enumerate(points):
      if len(colliding_cells.links(i)) > 0:
          points_on_proc.append(point)
          cells.append(colliding_cells.links(i)[0])

  points_on_proc = np.array(points_on_proc, dtype=np.float64)
  f_values = f.eval(points_on_proc, cells)
  return f_values.reshape(-1)

n=5
el = []
hl = []
for k in np.arange(1,n+1):
    h = 0.5*10.**-k
    msh = mesh.create_interval(MPI.COMM_WORLD,
                               nx=10,
                               points=[0.25, 0.75])
    V = fem.functionspace(msh, ('P', 1))
    pif = fem.Function(V)
    pif.interpolate(fun)

    # error norm l2
    e = quad(lambda x: (fem_fun_eval(x, pif, msh) - fun(x))**2,
             a = 0.25, b = 0.75)[0]
    print("%d %1.0E %1.1E" % (k,h,e))
    hl.append(h)
    el.append(e)
    
# grafico
plt.plot(hl,el,marker='o')
plt.xlim(10**-1,10**-n)
plt.xscale('log')
plt.xlabel('$h$')
plt.yscale('log')
plt.ylabel('$\|f-\pi f\|_{L^2}$')
plt.grid()
plt.show()
# xx = IntervalMesh(100,0.25,0.75)
# plot(f,mesh=xx,label="$f$")
# plot(f,mesh=mesh,
#      marker='o',label="$\pi f$")
# plt.legend(numpoints=1)
# plt.grid('on')
# plt.show()
