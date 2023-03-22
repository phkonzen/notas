import numpy as np
import numpy.linalg as npla

def qr_iter(A, Q=None, maxiter=10, tol=1e-5):
    Q = np.eye(A.shape[0]) if Q==None else Q
    T0 = Q.T @ A @ Q
    info = -1
    for k in range(maxiter):
        Q, R = npla.qr(T0)
        T = R @ Q
        if (npla.norm(T-T0) < tol):
            info = 0
            break
        T0 = T
    return T, info
        
