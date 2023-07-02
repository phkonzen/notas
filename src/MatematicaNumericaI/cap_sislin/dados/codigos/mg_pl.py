import numpy as np
import numpy.linalg as npla

def mg_pl(A, b, x0,
       maxiter=100, atol=1.49e-8, rtol=1.49e-8):
    
    n = b.size
    x = x0.copy()
    res = b - A@x
    alpha = np.dot(res, res)/np.dot(res, A@res)
    nres = npla.norm(res)
    print(f'0: {x}, alpha = {alpha}, nres = {nres:.1e}')
    info = -1
    for k in range(maxiter):
        x = x + alpha*res
        
        res = b - A@x
        alpha = np.dot(res, res)/np.dot(res, A@res)
        nres = npla.norm(res)

        print(f'{k}: {x}, alpha = {alpha}, nres = {nres:.1e}')

        if (nres <= max(atol, rtol*npla.norm(b))):
            info = 0
            break

    return x, info
            
# matriz coefs
A = np.array([[2., -1., 0., 0.],
              [-1., 2., -1., 0.],
              [0., -1., 2., -1.],
              [0., 0., -1., 2.]])
# vetor constante
b = np.array([-3., 2., 2., -3.])

# aprox. inicial
x0 = np.zeros_like(b)

x, info = mg_pl(A, b, x0)
