import numpy as np
import matplotlib.pyplot as plt

# exata
def ua(t,x):
    return np.exp(-t)*np.sin(np.pi*x)

x = np.fromfile('results/x.dat', dtype=np.float64)

fig = plt.figure()
ax = fig.add_subplot()
ax.grid()

ht = 1e-2;
for k in range(0,100,10):
    u = np.fromfile(f'results/u_{k:0>6d}.dat', 
                    dtype=np.float64)

    ax.plot(x, ua(k*ht, x), 
            lw=0.55, color=f'C{k}')
    ax.plot(x, u, ls='--', color=f'C{k}')

plt.show()