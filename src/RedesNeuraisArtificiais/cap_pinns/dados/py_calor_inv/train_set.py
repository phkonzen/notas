import numpy as np
import direct_solver as solver

# parâmetros
n = 10
ns = n*n

# saídas
cs = np.linspace(0., 1., 10)
Y = np.empty((ns, 2))
s = 0
for i,c0 in enumerate(cs):
    for j,c1 in enumerate(cs):
        Y[s,0] = c0
        Y[s,1] = c1
        s += 1

# entradas
nt = 10
nx = 10
X = np.empty((ns, 2*(nt+1)))
for s in range(ns):
    print(f'Training sample: {s+1}/{ns}.')
    u, xx = solver.calor(Y[s,0], Y[s,1])
    X[s,:nt+1] = u[:,0]
    X[s,nt+1:] = u[:,nx]

# save for later
np.save('x_train.npy', X)
np.save('y_train.npy', Y)
    

