import numpy as np
u = np.array([1., -2., 3., -4.])
v = np.array([-1., 2., 0., 1.])
destria = np.dot(u,v) <= npla.norm(u) \
    + npla.norm(v)
print(f'\nu.v <= ||u||.||v||? {destria}')

import numpy as np
import numpy.linalg as npla
v = np.array([-1., 2., 0., 1.])
norm_v = npla.norm(v)
print(f'\n||v|| = {norm_v}')

