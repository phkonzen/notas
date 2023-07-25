import numpy as np

def interpDDF(x, y):
    n = x.size
    M = np.empty((n,n))
    M[:,0] = y
    for j in range(1,n):
        for i in range(j,n):
            M[i,j] = (M[i,j-1] - M[i-1,j-1]) \
                / (x[i]-x[i-j])
    return np.diag(M)

def poliDDF(x, p, xpts):
    n = p.size
    pval = p[0]
    aux = 1.
    for i in range(1,n):
        aux *= (x-x[i-1])
        pval += p[i]*aux
    return pval

xpts = np.array([-1., 0, 1])
ypts = np.array([-1., 1, 1/2])
p = interpDDF(xpts, ypts)
print(poliDDF(xpts, p, xpts))

            
