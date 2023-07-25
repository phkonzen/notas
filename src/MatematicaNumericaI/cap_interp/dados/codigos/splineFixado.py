import numpy as np
from scipy.interpolate import CubicSpline

# dados
f = lambda x: np.sin(x)
xx = np.array([0.,
              np.pi/6,
              np.pi/3,
              np.pi/2])
yy = f(xx)

# spline
cs = CubicSpline(xx, yy,
                 bc_type=((1, 1.),
                          (1, 0.)))

# coefs
print(cs.c)
