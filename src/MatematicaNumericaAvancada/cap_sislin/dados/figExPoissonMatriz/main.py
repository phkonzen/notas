import matplotlib.pyplot as plt
import numpy as np

def plotMat(A):
  M = np.argwhere(A != 0)
  plt.scatter(M[:,1], M[:,0],
              marker="*", color="black")
  ax = plt.gca()
  ax.set_xticks([])
  ax.set_yticks([])
  ax.set_aspect('equal')
  ax.invert_yaxis()
  plt.savefig('fig.png', bbox_inches='tight')


n = 7
A = np.zeros(((n-2)**2,(n-2)**2))
b = np.zeros((n-2)**2)

h = np.pi/(n-1)

def x(i):
  return (i-1)*h

def y(j):
  return (j-1)*h

def f(i,j):
  return np.sin(x(i)) * np.sin(y(j))

for j in np.arange(2,n):
  for i in np.arange(2,n):
    k = (i-1) + (j-2)*(n-2) - 1

    b[k] = h**2 * f(i,j)

    if (j==2):
      if (i==2):
        A[k,k] = 4.
        A[k,k+1] = -1
        A[k,k+n-2] = -1.

      if (i>=3) and (i<=n-2):
        A[k,k-1] = -1.
        A[k,k] = 4.
        A[k,k+1] = -1.
        A[k,k+n-2] = -1.

      if (i==n-1):
        A[k,k-1] = -1.
        A[k,k] = 4.
        A[k,k+n-2] = -1.
      
    if ((j>=3) and (j<=n-2)):
      if (i==2):
        A[k,k-(n-2)] = -1.
        A[k,k] = 4.
        A[k,k+1] = -1.
        A[k,k+n-2] = -1.

      if (i>=3) and (i<=n-2):
        A[k,k-1] = -1.
        A[k,k-(n-2)] = -1.
        A[k,k] = 4.
        A[k,k+1] = -1.
        A[k,k+n-2] = -1.

      if (i==n-1):
        A[k,k-1] = -1.
        A[k,k-(n-2)] = -1.
        A[k,k] = 4.
        A[k,k+n-2] = -1.

    if (j==n-1):
      if (i==2):
        A[k,k-(n-2)] = -1.
        A[k,k] = 4.
        A[k,k+1] = -1.

      if (i>=3) and (i<=n-2):
        A[k,k-1] = -1.
        A[k,k-(n-2)] = -1.
        A[k,k] = 4.
        A[k,k+1] = -1.

      if (i==n-1):
        A[k,k-1] = -1.
        A[k,k-(n-2)] = -1.
        A[k,k] = 4.

plotMat(A)
