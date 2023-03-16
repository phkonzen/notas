import numpy as np
import numpy.linalg as npla

def metPot(A, q0, maxiter=1000, tol=1e-14):
  q = q0/npla.norm(q0)
  nu0 = np.dot(q, A @ q)
  print(f"{0}: {nu0}")

  info = -1
  for k in range(maxiter):
    z = A @ q
    q = z/npla.norm(z)
    nu = np.dot(q, A @ q)

    print(f"{k+1}: {nu}")
    if (np.fabs(nu-nu0) < tol):
      info = 0
      break

    nu0 = nu

  return nu, q, info

