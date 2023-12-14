from mpi4py import MPI
import numpy as np
import ufl
from dolfinx import mesh
from dolfinx import fem
from dolfinx import default_scalar_type
from dolfinx.fem.petsc import NonlinearProblem
from dolfinx.nls.petsc import NewtonSolver

# parâmetros
tf = 5.

# esquema theta
theta = 0.5

# discretização no tempo
nt = 100
ht = tf/nt

# malha
domain = mesh.create_unit_interval(MPI.COMM_WORLD,
                                   nx = 5)
x = ufl.SpatialCoordinate(domain)

# espaço
V = fem.functionspace(domain, ('P', 1))

# mef fun.s
v = ufl.TestFunction(V)
u = fem.Function(V)

# condição inicial
t = 0.
u0 = fem.Function(V)
u0.interpolate(lambda x: np.cos(np.pi*x[0])**2)

# inicialização
u.x.array[:] = u0.x.array[:]

# visualização (paraview)
from dolfinx import io
from pathlib import Path
results_folder = Path("results")
results_folder.mkdir(exist_ok=True, parents=True)

# armazena para visualização (paraview)
filename = results_folder / f"u_{0:0>6}"
with io.XDMFFile(domain.comm, filename.with_suffix(".xdmf"), "w") as xdmf:
    xdmf.write_mesh(domain)
    xdmf.write_function(u, 0.)


# iteração no tempo
for k in range(nt):
    
    t += ht
    print(f"{k+1}: t = {t:.4g}")

    # forma fraca
    ## time term
    F = 1./ht * u * v * ufl.dx
    F -= 1./ht * u0 * v * ufl.dx
    ## diffusion term
    F += theta * ufl.dot(ufl.grad(u), ufl.grad(v)) * ufl.dx
    F += (1.-theta) * ufl.dot(ufl.grad(u0), ufl.grad(v)) * ufl.dx
    ## reaction term
    F -= theta * u * (1. - u) * v * ufl.dx
    F -= (1.-theta) * u0 * (1. - u0) * v * ufl.dx

    problem = NonlinearProblem(F, u)
    solver = NewtonSolver(MPI.COMM_WORLD, problem)
    n, converged = solver.solve(u)
    print(f"\tNewton iterations: {n}")
    assert(converged)

    # armazena para visualização (paraview)
    filename = results_folder / f"u_{k+1:0>6}"
    with io.XDMFFile(domain.comm, filename.with_suffix(".xdmf"), "w") as xdmf:
        xdmf.write_mesh(domain)
        xdmf.write_function(u, t)

    u0.x.array[:] = u.x.array[:]
