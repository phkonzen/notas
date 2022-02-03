import matplotlib.pyplot as plt
import numpy as np

n = 26
A = np.zeros((n,n))

for i in np.arange(n):
    if (i-7 >= 0):
        A[i,i-7] = 1.0
    if (i-1 >= 0):
        A[i,i-1] = 1.0
    A[i,i] = 1.0
    if (i+1 < n):
        A[i,i+1] = 1.0
    if (i+5 < n):
        A[i,i+5] = 1.0
    if (i+7 < n):
        A[i,i+7] = 1.0
        
plt.matshow(A, cmap="binary")
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('main.png', bbox_inches='tight')
