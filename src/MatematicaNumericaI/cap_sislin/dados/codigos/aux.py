import numpy as np
import numpy.linalg as npla
np.set_printoptions(precision=4)
A = np.array([[-1., 2., -2.],
              [3., 4., 1.],
              [-4., -5., 3.]])
Ainv = npla.inv(A)
print(Ainv)

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

