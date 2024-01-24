from mpi4py import MPI
from dolfinx import mesh

# malha
domain = mesh.create_unit_square(MPI.COMM_WORLD, 16, 16)

from dolfinx import fem

# espaço de elementos finitos
Vh = fem.functionspace(domain, ("P",1))

# função do espaço V
uh = fem.Function(Vh)

# projeção
import ufl
from dolfinx.fem.petsc import LinearProblem
def uex(x, mod=ufl):
    return mod.sin(mod.pi*x[0])*mod.sin(mod.pi*x[1])

x = ufl.SpatialCoordinate(domain)
u = ufl.TrialFunction(Vh)
v = ufl.TestFunction(Vh)
a = ufl.dot(u,v)*ufl.dx
L = uex(x)*v*ufl.dx
problem = LinearProblem(a, L, bcs=[])
Phu = problem.solve()

# saída (paraview)
from dolfinx import io
from pathlib import Path
results_folder = Path("results")
results_folder.mkdir(exist_ok=True, parents=True)
filename = results_folder / "phu"
Phu.name = "Phu"
with io.VTXWriter(domain.comm, filename.with_suffix(".bp"), [Phu]) as vtx:
    vtx.write(0.0)
with io.XDMFFile(domain.comm, filename.with_suffix(".xdmf"), "w") as xdmf:
    xdmf.write_mesh(domain)
    xdmf.write_function(Phu, 0.0)