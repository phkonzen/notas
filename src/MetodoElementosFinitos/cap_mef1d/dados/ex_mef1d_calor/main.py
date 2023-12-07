from mpi4py import MPI
import ufl
from dolfinx import mesh
from dolfinx import fem
from dolfinx import default_scalar_type
from dolfinx.fem.petsc import LinearProblem

# parâmetros
tf = 1.
alpha = 1.

# esquema theta
theta = 0.5

# discretização no tempo
nt = 10
ht = tf/nt

# malha
domain = mesh.create_unit_interval(MPI.COMM_WORLD,
                                   nx = 5)
x = ufl.SpatialCoordinate(domain)

# espaço
V = fem.functionspace(domain, ('P', 1))

# fonte
f = fem.Function(V)
def f(t,x):
    return (ufl.pi**2-1.)*ufl.exp(-t)*ufl.sin(ufl.pi*x[0])

# condição de contorno
import numpy as np
uD = fem.Function(V)
uD.interpolate(lambda x: np.full(x.shape[1], 0.))

def boundary_D(x):
    return np.logical_or(np.isclose(x[0], 0.),
                         np.isclose(x[0], 1.))

dofs_D = fem.locate_dofs_geometrical(V, boundary_D)
bc = fem.dirichletbc(uD, dofs_D)

# mef fun.s
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)

# condição inicial
t = 0.
u0 = fem.Function(V)
u0.interpolate(lambda x: np.sin(np.pi*x[0]))

# fonte
def f(t, x):
    return (ufl.pi**2-1.)*ufl.exp(-t)*ufl.sin(ufl.pi*x[0])

# visualização (paraview)
from dolfinx import io
from pathlib import Path
results_folder = Path("results")
results_folder.mkdir(exist_ok=True, parents=True)

# iteração no tempo
for k in range(nt):
    t += ht

    # forma bilinear
    a = theta * ufl.dot(ufl.grad(u), ufl.grad(v)) * ufl.dx
    a += u * v / ht * ufl.dx

    # forma linear
    L = (theta-1.) * ufl.dot(ufl.grad(u0), ufl.grad(v)) * ufl.dx
    L += u0 * v / ht * ufl.dx
    L += theta * f(t, x) * v * ufl.dx
    L += (1.-theta) * f(t-ht, x) * v * ufl.dx

    problem = LinearProblem(a, L, bcs=[bc])
    uh = problem.solve()

    # armazena para visualização (paraview)
    filename = results_folder / f"u_{k:0>6}"
    with io.XDMFFile(domain.comm, filename.with_suffix(".xdmf"), "w") as xdmf:
        xdmf.write_mesh(domain)
        xdmf.write_function(uh, t)

    u0.x.array[:] = uh.x.array[:]
