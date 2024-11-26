import numpy as np
import scipy as sp
from scipy.linalg import norm

def mgc(A, b, x, tol=1e-14):
  n, = b.shape
  r = b - A*x
  p = r
  nu = np.dot(r,r)
  for it in np.arange(n):
    q = A*p
    mu = np.dot(p,q)
    alpha = nu/mu
    x = x + alpha*p
    r = r - alpha*q
    nu0 = np.dot(r,r)
    beta = nu0/nu
    p = r + beta*p
    nu = nu0
    if (norm(r) < tol):
      print(it)
      return x
  raise ValueError("Falha de convergencia.")
