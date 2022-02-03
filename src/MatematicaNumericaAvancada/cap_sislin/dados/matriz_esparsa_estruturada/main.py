import matplotlib.pyplot as plt
import numpy as np

n = 50
A = np.zeros((n,n))

for i in np.arange(6,n-6,6):
    ini = max(0,i-3)
    fin = min(i+3,n)
    A[ini:fin,ini:fin] = np.ones((fin-ini,fin-ini))


for i in np.arange(n):
    A[i,i] = 1.
    if (i-20 >= 0):
        A[i,i-20] = 1.
    if (i+20 < 50):
        A[i,i+20] = 1.

plt.matshow(A, cmap="binary")
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('main.png', bbox_inches='tight')
