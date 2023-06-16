import numpy as np
import numpy.linalg as npla
A = np.array([[1., -1., 2.],
              [-2., np.pi, 4.],
              [7., -5., np.sqrt(2)]])
B = np.array([[1., -1., 3.],
              [-2., 1, 4.],
              [7., -1., np.sqrt(2)]])
norm_A = npla.norm(A)
norm_B = npla.norm(A)
print(npla.norm(A@B))
print(norm_A * norm_B)

u = np.array([1., -2., 3., -4.])
v = np.array([-1., 2., 0., 1.])
nupv = npla.norm(u+v)
nupnv = npla.norm(u) + npla.norm(v)
print('\nu.v <= ||u||.||v||?')
print(nupv <= nupnv)

import numpy as np
import numpy.linalg as npla
v = np.array([-1., 2., 0., 1.])
norm_v = npla.norm(v)
print(f'\n||v|| = {norm_v}')

