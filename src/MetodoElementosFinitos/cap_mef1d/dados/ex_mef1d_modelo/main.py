from mpi4py import MPI

# malha
from dolfinx import mesh
domain = mesh.create_unit_interval(MPI.COMM_WORLD,
                                   nx = 5)
# espaço
from dolfinx import fem
V = fem.functionspace(domain, ('P', 1))

# condição de contorno
import numpy as np
uD = fem.Function(V)
uD.interpolate(lambda x: np.full(x.shape[1], 0.))

tdim = domain.topology.dim
fdim = tdim - 1
domain.topology.create_connectivity(fdim, tdim)
boundary_facets = mesh.exterior_facet_indices(domain.topology)
boundary_dofs = fem.locate_dofs_topological(V, fdim,
                                            boundary_facets)
bc = fem.dirichletbc(uD, boundary_dofs)

# problema mef
import ufl
from dolfinx import default_scalar_type
from dolfinx.fem.petsc import LinearProblem
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)

f = fem.Constant(domain, default_scalar_type(1.))

a = ufl.dot(ufl.grad(u), ufl.grad(v)) * ufl.dx
L = f * v * ufl.dx

problem = LinearProblem(a, L, bcs=[bc])
uh = problem.solve()

# armazena para visualização (paraview)
from dolfinx import io
from pathlib import Path
results_folder = Path("results")
results_folder.mkdir(exist_ok=True, parents=True)
filename = results_folder / "u"
with io.XDMFFile(domain.comm, filename.with_suffix(".xdmf"), "w") as xdmf:
    xdmf.write_mesh(domain)
    xdmf.write_function(uh)
