import numpy as np
import matplotlib.pyplot as plt

def calor(c0, c1, tf=1., nt=10000, nx=10, nout=1000):
    # malha
    ht = tf/nt
    tt = np.linspace(0., 1., nt+1)
    hx = 1./nx
    xx = np.linspace(0., 1., nx+1)
    # diffusion coefs
    dc = np.empty_like(xx)
    for i,x in enumerate(xx):
        if (x <= 0.5):
            dc[i] = c0
        else:
            dc[i] = c1
    # fonte
    f = lambda x: 4.*x*(1-x)

    # output
    uout = np.empty((nt//nout+1, nx+1))

    t0 = 0.
    u0 = np.zeros(nx+1)
    uout[0,:] = u0
    u = u0.copy()
    for k in range(nt):
        t = t0 + ht
        for i in range(1,nx):
            u[i] = u0[i]
            u[i] += ht*dc[i]*(u0[i-1] - 2*u0[i] + u0[i+1])/hx**2
            u[i] += ht*f(xx[i])
        # bcs
        u[0] = u[1]
        u[nx] = u[nx-1]

        if (((k+1) % nout) == 0):
            uout[(k+1)//nout,:] = u.copy()
            
        t0 = t
        u0 = u.copy()
    return uout, xx


# u, xx = calor(0.0, 0.0)
# for k in range(u.shape[0]):
#     plt.plot(xx, u[k,:])
# plt.grid()
# plt.show()
