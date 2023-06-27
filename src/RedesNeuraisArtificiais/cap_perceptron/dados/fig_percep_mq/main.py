import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

# use LaTeX
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "savefig.bbox": 'tight'})
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = np.array([0.5, 1.0, 1.5, 2.0])
y = np.array([1.2, 2.1, 2.6, 3.6])
ax.plot(x, y, ls='', marker='o',
        color='red', label='dados')
w = 1.54
b = 0.45
xx = np.linspace(0, 2.5)
yy = w*xx + b
ax.plot(xx, yy, color='blue', label='modelo')

ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend()
fig.savefig("main.png")
