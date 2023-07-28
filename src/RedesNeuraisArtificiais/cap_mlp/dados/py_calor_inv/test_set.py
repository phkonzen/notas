import numpy as np
import direct_solver as solver

# test data

# parâmetros
n = 10
ns = n*n

# saídas randômicas
Y_test = np.random.rand(ns, 2)

# entradas
nt = 10
nx = 10
X_test = np.empty((ns, 2*(nt+1)))
for s in range(ns):
    print(f'Training sample: {s+1}/{ns}.')
    u, xx = solver.calor(Y_test[s,0], Y_test[s,1])
    X_test[s,:nt+1] = u[:,0]
    X_test[s,nt+1:] = u[:,nx]

# save for later
np.save('x_test.npy', X_test)
np.save('y_test.npy', Y_test)
