import numpy as np
import matplotlib.pyplot as plt

h = np.array([3.5e-1,
              1.8e-1,
              8.8e-2,
              4.4e-2,
              2.2e-2])
err = np.array([6.0e-2,
                1.6e-2,
                3.9e-3,
                9.8e-4,
                2.4e-4])

fig = plt.figure(dpi=300)
ax = fig.add_subplot(111)
ax.loglog(h, err, ls='--', marker='o', ms=4)
ax.set_xlabel('$h$')
ax.set_ylabel('$\\|u_h-u\\|_{L^2(\\Omega)}$')
ax.grid(which='both', axis='both', ls=':')
ax.set_xticks([1e0, 1e-1, 1e-2])
ax.set_aspect('equal')
plt.savefig('fig.pdf', bbox_inches='tight')
plt.savefig('fig.png', bbox_inches='tight')
plt.show()
