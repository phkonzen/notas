from mpi4py import MPI
import numpy as np
import ufl
from dolfinx import mesh
from dolfinx import fem
from dolfinx import default_scalar_type
from dolfinx.fem.petsc import NonlinearProblem
from dolfinx.nls.petsc import NewtonSolver

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

# mef fun.s
uh = fem.Function(V)
v = ufl.TestFunction(V)

# condição inicial
t = 0.
u0 = fem.Function(V)
u0.interpolate(lambda x: 1./10*np.cos(np.pi*x[0])**2)

uh.x.array[:] = u0.x.array[:]

# visualização (paraview)
from dolfinx import io
from pathlib import Path
results_folder = Path("results")
results_folder.mkdir(exist_ok=True, parents=True)

# armazena para visualização (paraview)
filename = results_folder / f"u_{0:0>6}"
with io.XDMFFile(domain.comm, filename.with_suffix(".xdmf"), "w") as xdmf:
    xdmf.write_mesh(domain)
    xdmf.write_function(uh, 0.)


# iteração no tempo
for k in range(nt):
    t += ht

    # forma fraca
    F = theta * ufl.dot(ufl.grad(uh), ufl.grad(v)) * ufl.dx
    F -= theta * uh * (1. - uh) * v * ufl.dx
    F += uh * v / ht * ufl.dx

    F -= (theta-1.) * ufl.dot(ufl.grad(u0), ufl.grad(v)) * ufl.dx
    F -= (1.-theta) * u0 * (1. - u0) * v * ufl.dx
    F -= u0 * v / ht * ufl.dx

    problem = NonlinearProblem(F, uh)
    solver = NewtonSolver(MPI.COMM_WORLD, problem)
    n, converged = solver.solve(uh)
    assert(converged)

    # armazena para visualização (paraview)
    filename = results_folder / f"u_{k+1:0>6}"
    with io.XDMFFile(domain.comm, filename.with_suffix(".xdmf"), "w") as xdmf:
        xdmf.write_mesh(domain)
        xdmf.write_function(uh, t)

    u0.x.array[:] = uh.x.array[:]
