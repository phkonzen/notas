from __future__ import print_function, division
from fenics import *
import numpy as np
import matplotlib.pyplot as plt

# malha
Nx = 5
Ny = 5
mesh = UnitSquareMesh(Nx,Ny)

# espaco
V = FunctionSpace(mesh, 'P', 1)

# funcao
f = Expression('sin(pi*x[0])*cos(pi*x[1])',degree=3)

# interpolacao
pif = interpolate(f,V)

# exportanto em vtk
vtkfile = File('pif.pvd')
vtkfile << pif
