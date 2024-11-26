import matplotlib.pyplot as plt
import numpy as np
import timeit

n = 10
h = 1.0/(n-1)
A = np.zeros((2*(n-2),2*(n-2)))

# Exemplo 1.1.1 F1

def ui(i):
  return 2*(i-1)-2

def vi(i):
  return 2*(i-1)-1

def x(i):
  return (i-1)*h

e = 0
A[e, ui(2)] = 2.0
A[e, ui(3)] = -1.0
A[e, vi(2)] = h**2

for e in np.arange(1,n-3):
  i = e + 2
  A[e, ui(i-1)] = -1.0
  A[e, ui(i)] = 2.0
  A[e, ui(i+1)] = -1.0
  A[e, vi(i)] = h**2

e = n-3
A[e, ui(n-2)] = -1.0
A[e, ui(n-1)] = 2.0
A[e, vi(n-1)] = h**2

e = n - 2
A[e, vi(2)] = 2.0
A[e, vi(3)] = -1.0
A[e, ui(2)] = -h**2

for e in np.arange(n-1, 2*(n-2)-1):
  i = e - n + 4
  A[e, vi(i-1)] = -1.0
  A[e, vi(i)] = 2.0
  A[e, vi(i+1)] = -1.0
  A[e, ui(i)] = -h**2

e = 2*(n-2)-1
A[e, vi(n-2)] = -1.0
A[e, vi(n-1)] = 2.0
A[e, ui(n-1)] = -h**2

# plota matriz
# plt.matshow(A != 0, cmap="binary")
M = np.argwhere(A != 0)
plt.scatter(M[:,1], M[:,0],
            marker="*", color="black")
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
ax.invert_yaxis()
plt.savefig('f1.png', bbox_inches='tight')

plt.clf()

# F2

A = np.zeros((2*(n-2),2*(n-2)))

def ui(i):
  return i-2

def vi(i):
  return i + n - 4

def x(i):
  return (i-1)*h

e = 0
A[e, ui(2)] = 2.0
A[e, ui(3)] = -1.0
A[e, vi(2)] = h**2

for e in np.arange(1,n-3):
  i = e + 2
  A[e, ui(i-1)] = -1.0
  A[e, ui(i)] = 2.0
  A[e, ui(i+1)] = -1.0
  A[e, vi(i)] = h**2

e = n-3
A[e, ui(n-2)] = -1.0
A[e, ui(n-1)] = 2.0
A[e, vi(n-1)] = h**2

e = n - 2
A[e, vi(2)] = 2.0
A[e, vi(3)] = -1.0
A[e, ui(2)] = -h**2

for e in np.arange(n-1, 2*(n-2)-1):
  i = e - n + 4
  A[e, vi(i-1)] = -1.0
  A[e, vi(i)] = 2.0
  A[e, vi(i+1)] = -1.0
  A[e, ui(i)] = -h**2

e = 2*(n-2)-1
A[e, vi(n-2)] = -1.0
A[e, vi(n-1)] = 2.0
A[e, ui(n-1)] = -h**2

# plota matriz
M = np.argwhere(A != 0)
plt.scatter(M[:,1], M[:,0],
            marker="*", color="black")
ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
ax.invert_yaxis()
plt.savefig('f2.png', bbox_inches='tight')
