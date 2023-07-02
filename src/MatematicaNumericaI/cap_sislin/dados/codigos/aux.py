import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt

def mg(A, b, x0, alpha=1e-2,
       maxiter=100, atol=1.49e-8, rtol=1.49e-8):
    
    n = b.size
    x = x0.copy()
    res = b - A@x
    nres = npla.norm(res)
    print(f'0: {x}, nres = {nres:.1e}')
    info = -1
    for k in range(maxiter):
        x = x + alpha*res
        
        res = b - A@x
        nres = npla.norm(res)

        print(f'{k}: {x}, nres = {nres:.1e}')

        if (nres <= max(atol, rtol*npla.norm(b))):
            info = 0
            break

    return x, info


def mg_pl(A, b, x0,
       maxiter=100, atol=1.49e-8, rtol=1.49e-8):
    
    n = b.size
    x = x0.copy()
    res = b - A@x
    alpha = np.dot(res, res)/np.dot(res, A@res)
    l = [alpha]
    nres = npla.norm(res)
    print(f'0: alpha = {alpha}, nres = {nres:.1e}')
    info = -1
    for k in range(maxiter):
        x = x + alpha*res
        
        res = b - A@x
        alpha = np.dot(res, res)/np.dot(res, A@res)
        l.append(alpha)
        nres = npla.norm(res)

        print(f'{k+1}: alpha = {alpha}, nres = {nres:.1e}')

        if (nres <= max(atol, rtol*npla.norm(b))):
            info = 0
            break

    print(sum(l)/len(l))
    return x, info
            
# matriz coefs
n = 80
h = 1./n
A = np.zeros((n+1,n+1))
b = np.zeros(n+1)
A[0,0] = 1.
for i in range(1,n):
    A[i,i-1] = -1./h**2
    A[i,i] = 2./h**2
    A[i,i+1] = -1./h**2
    b[i] = 2
A[n,n] = 1.

#print(npla.eig(A))

#raise ValueError('oi')

# aprox. inicial
x0 = np.zeros_like(b)

#x, info = mg(A, b, x0, alpha=1e-4)
x, info = mg_pl(A, b, x0,
                maxiter=50000, atol=1e-4, rtol=0.)

plt.close()
plt.plot(np.linspace(0,1,n+1), x)
plt.grid()
plt.show()
