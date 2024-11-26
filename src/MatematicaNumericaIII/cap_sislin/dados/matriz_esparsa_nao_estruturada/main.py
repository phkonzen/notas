import matplotlib.pyplot as plt
import numpy as np

n = 50
A = np.zeros((n,n))

for i in np.arange(4,n-4,4):
    ini = max(0,i-2)
    fin = min(i+2,n)
    A[ini:fin,ini:fin] = np.ones((fin-ini,fin-ini))


for i in np.arange(n):
    A[i,i] = 1.
    j = i - np.random.randint(17,23)
    if (j >= 0):
        A[i,j] = 1.
    j = i + np.random.randint(17,23)
    if (j < 50):
        A[i,j] = 1.

plt.matshow(A, cmap="binary")
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('main.png', bbox_inches='tight')
