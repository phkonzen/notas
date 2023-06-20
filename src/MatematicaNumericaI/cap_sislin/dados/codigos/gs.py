import numpy as np
import numpy.linalg as npla
np.set_printoptions(precision=2)

def jacobi(A, b, x0, maxiter = 100,
           tol=4.9e-8, atol=4.9e-8):
    
    n = b.size
    info = -1

    x = np.empty_like(x0)
    nres = npla.norm(A@x - b)
    print(f'\n{0}: {x0}, {nres:.1e}')
    
    # iterações
    for k in range(maxiter):
        for i in  range(n):
            x[i] = b[i]
            # x[i] -= np.dot(A[i,:i], x[:i])
            for j in range(i):
                x[i] -= A[i,j]*x[j]
            # x[i] -= np.dot(A[i,i+1:], x0[i+1:])
            for j in range(i+1,n):
                x[i] -= A[i,j]*x0[j]
            x[i] /= A[i,i]
        # critério de parada
        nres = npla.norm(A@x - b)
        print(f'{k+1}: {x}, {nres:.1e}')
        if (nres <= max(tol*npla.norm(b), atol)):
            info = 0
            break
        x0 = x

    return x, info    
                

# sistema
A = np.array([[-4., 2., -1.],
              [-2., 5., 2.],
              [1., -1., -3.]])

b = np.array([-11., -7., 0.])

x0 = np.zeros_like(b)
x, info = jacobi(A, b, x0)



