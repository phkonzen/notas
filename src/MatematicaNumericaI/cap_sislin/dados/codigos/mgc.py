import numpy as np
import numpy.linalg as npla

def mgc(A, b, x0,
       maxiter=100, atol=1.49e-8, rtol=1.49e-8):
    
    n = b.size
    x = x0.copy()
    r = b - A@x
    d = r.copy()
    nr = npla.norm(r)
    print(f'0: {x}, nr = {nr:.1e}')
    info = -1
    for k in range(maxiter):
        rdr = np.dot(r, r)
        Ad = A@d
        alpha = rdr/np.dot(d,Ad)
        x = x + alpha*d

        r = r - alpha*Ad
        beta = np.dot(r,r)/rdr
        d = r + beta*d

        nr = npla.norm(r)
        print(f'{k+1}: {x}, nr = {nr:.1e}')

        if (nr <= max(atol, rtol*npla.norm(b))):
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

x, info = mgc(A, b, x0)
