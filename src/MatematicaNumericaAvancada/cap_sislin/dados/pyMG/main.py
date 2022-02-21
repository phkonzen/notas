import numpy as np
import scipy as sp
from scipy.linalg import norm

def mg(A, b, x, tol=1e-14):
  n, = b.shape
  r = b - A*x
  for _ in np.arange(n):
    q = A*r
    alpha = np.dot(r,r)/np.dot(r,q)
    x = x + alpha*r
    r = r - alpha*q
    if (norm(r) < tol):
      return x
  raise ValueError("Falha de convergencia.")
