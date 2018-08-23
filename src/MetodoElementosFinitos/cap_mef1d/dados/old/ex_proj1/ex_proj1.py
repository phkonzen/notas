from __future__ import print_function
from fenics import *
import numpy as np
import matplotlib.pyplot as plt

# Create mesh and define function space
mesh = IntervalMesh(4,0.25,0.75)
V = FunctionSpace(mesh, 'P', 1)

# Define function
f = Expression('3*sin(2*pi*x[0])',element=V.ufl_element())

# Compute projection
Phf = Function(V)
Phf.interpolate(f)

# def boundary(x, on_boundary):
#     return on_boundary

# bc = DirichletBC(V, u_D, boundary)

# # Define variational problem
# u = TrialFunction(V)
# v = TestFunction(V)
# f = Constant(-6.0)
# a = dot(grad(u), grad(v))*dx
# L = f*v*dx

# # Compute solution
# u = Function(V)
# solve(a == L, u, bc)

# Plot
xx = np.linspace(0.25,0.75)
plt.plot(xx,3*np.sin(2*np.pi*xx))
plot(Phf)
plt.show()

# # Save solution to file in VTK format
# vtkfile = File('poisson/solution.pvd')
# vtkfile << u

# # Compute error in L2 norm
# error_L2 = errornorm(u_D, u, 'L2')

# # Compute maximum error at vertices
# vertex_values_u_D = u_D.compute_vertex_values(mesh)
# vertex_values_u = u.compute_vertex_values(mesh)
# import numpy as np
# error_max = np.max(np.abs(vertex_values_u_D - vertex_values_u))

# # Print errors
# print('error_L2  =', error_L2)
# print('error_max =', error_max)

# # Hold plot
# #interactive()
