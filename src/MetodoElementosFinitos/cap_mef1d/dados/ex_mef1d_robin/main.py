from mpi4py import MPI

# malha
from dolfinx import mesh
domain = mesh.create_unit_interval(MPI.COMM_WORLD,
                                   nx = 5)
# espaço
from dolfinx import fem
V = fem.functionspace(domain, ('P', 1))

# boundary colors
from dolfinx.mesh import locate_entities
from dolfinx.mesh import meshtags
boundaries = [(0, lambda x: np.isclose(x[0], 0.)),
              (1, lambda x: np.isclose(x[0], 1.))]
facet_indices, facet_markers = [], []
fdim = domain.topology.dim - 1
for (marker, locator) in boundaries:
    facets = locate_entities(domain, fdim, locator)
    facet_indices.append(facets)
    facet_markers.append(np.full_like(facets, marker))
facet_indices = np.hstack(facet_indices).astype(np.int32)
facet_markers = np.hstack(facet_markers).astype(np.int32)
sorted_facets = np.argsort(facet_indices)
facet_tag = meshtags(domain, fdim, facet_indices[sorted_facets], facet_markers[sorted_facets])

# problema mef
import ufl
from dolfinx import default_scalar_type
from dolfinx.fem.petsc import LinearProblem
u = ufl.TrialFunction(V)
v = ufl.TestFunction(V)

f = fem.Constant(domain, default_scalar_type(1.))
g = fem.Constant(domain, default_scalar_type(1.))

ds = ufl.Measure('ds', domain=domain, subdomain_data=facet_tag)

a = ufl.dot(ufl.grad(u), ufl.grad(v)) * ufl.dx
a += u * v * ds(1) + u * v * ds(0)
L = f * v * ufl.dx
L += g * v * ds(1)

problem = LinearProblem(a, L, bcs=[])
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
