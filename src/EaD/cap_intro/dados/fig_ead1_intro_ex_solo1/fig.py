import matplotlib.pyplot as plt
import numpy as np

nn = np.arange(5)
yy = np.zeros(5)
for n in np.arange(4):
    yy[n+1]=2*yy[n]-1

fig, ax = plt.subplots()
ax.plot(nn,yy,marker='o',markersize=4, ls='')
ax.set_xlabel('$n$')
ax.set_ylabel('$y(n)$')
ax.grid('on')
plt.show()
