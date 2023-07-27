# dados
xx = np.array([-1.0,
              0.0,
              1.0,
              1.5])
yy = np.array([1.2,
               -0.1,
               0.7,
               2.4])

# matriz
m = 3
n = xx.size
A = np.empty((n,m))
A[:,0] = np.sin(xx)
A[:,1] = np.cos(xx)
A[:,2] = np.ones_like(xx)

# sol de mq
c = npla.solve(A.T@A, A.T@yy)

def f(x, c=c):
    y = c[0]*np.sin(x) \
        + c[1]*np.cos(x) \
        + c[2]
    return y
