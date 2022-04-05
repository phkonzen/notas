import numpy as np
import numpy.linalg as npla

def metPot(A,q0,tol=1e-14):
  n = A.shape[0]
  q = q0/npla.norm(q0)
  nu0 = np.conjugate(q).dot(A @ q)
  print(f"{0}: {nu0}")

  for k in range(maxiter):
    z = A @ q
    q = z/npla.norm(z)
    nu = np.conjugate(q).dot(A @ q)

    print(f"{k+1}: {nu}")
    if (np.fabs(nu-nu0) < tol):
      return nu, q, 0
    elif (k+1 == maxiter):
      return nu, q, 1
      
    nu0 = nu
