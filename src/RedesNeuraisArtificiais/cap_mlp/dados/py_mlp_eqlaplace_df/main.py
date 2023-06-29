import torch
import matplotlib.pyplot as plt
import random
import numpy as np

# modelo
model = torch.nn.Sequential(
    torch.nn.Linear(2,50),
    torch.nn.Tanh(),
    torch.nn.Linear(50,10),
    torch.nn.Tanh(),
    torch.nn.Linear(10,5),
    torch.nn.Tanh(),
    torch.nn.Linear(5,1)
)

# SGD - (Stochastic) Gradient Descent
optim = torch.optim.SGD(model.parameters(),
                        lr = 1e-3,
                        momentum = 0.9,
                        dampening = 0.)

# Solução esperada
def u(x, y):
    return a*x*(1-x) - a*y*(1-y)


def laplace_loss(A, U, h2, n, uc=u, p=1.):
    # num de amostras
    nc = 2*n + 2*(n-2)
    ni = n**2 - nc

    # loss interno
    li = 0.
    for i in range(1,n-1):
      for j in range(1,n-1):
        s = j + i*n
        l = (U[s-n, 0] - 2 * U[s, 0] + U[s+n, 0])/h2 # x
        l += (U[s-1, 0] - 2 * U[s, 0] + U[s+1, 0])/h2 # y
        li += l**2
    li /= ni 

    # loss contorno
    lc = 0.
    # 0 <= x <= 1 e y == 0
    for i in range(n):
        s = i*n
        x = M[s,0]
        y = M[s,1]
        lc += (U[s,0] - uc(x,y))**2
    # 0 <= x <= 1 e y == 1
    for i in range(n):
        s = n-1 + i*n
        x = M[s,0]
        y = M[s,1]
        lc += (U[s,0] - uc(x,y))**2
    # 0 == x e 0 < y < 1
    for j in range(1, n-1):
        s = j
        x = M[s,0]
        y = M[s,1]
        lc += (U[s,0] - uc(x,y))**2
    # 1 == x e 0 < y < 1
    for j in range(1, n-1):
        s = j + n*(n-1)
        x = M[s,0]
        y = M[s,1]
        lc += (U[s,0] - uc(x,y))**2
    lc *= p/nc
    
    loss = li + lc
    return loss

    
# dados do problema

# collocation points
a = 1
n = 11
ns = n**2
h = 1./(n-1)
h2 = h**2

# malha
x = torch.linspace(0, 1, n)
y = torch.linspace(0, 1, n)

M = torch.empty((ns, 2))
s = 0
for i, xx in enumerate(x):
  for j, yy in enumerate(y):
    M[s,0] = xx
    M[s,1] = yy
    s += 1

# gráfico
X, Y = np.meshgrid(x, y)
U_esp = u(X, Y)

# training
nepochs = 5001
nout = 1000

for epoch in range(nepochs):

    # forward
    U_est = model(M)

    # loss function
    loss = laplace_loss(M, U_est, h2, n, u, p=10.)

    print(f'{epoch+1}: loss = {loss.item():.4e}')
    
    # output current solution
    if (epoch+1) % nout == 0:
        # verificação
        fig = plt.figure()
        ax = fig.add_subplot()

        ns = 50
        x1 = torch.linspace(0., 1., ns)
        x2 = torch.linspace(0., 1., ns)
        X1, X2 = torch.meshgrid(x1, x2)
        # exact
        Z_esp = torch.empty_like(X1)
        for i,x in enumerate(x1):
            for j,y in enumerate(x2):
                Z_esp[i,j] = u(x, y)
        c = ax.contour(X1, X2, Z_esp, levels=10, colors='white')
        ax.clabel(c)

        X_plot = torch.cat((X1.reshape(-1,1),
                            X2.reshape(-1,1)), dim=1)
        Z_est = model(X_plot)
        Z_est = Z_est.reshape((ns,ns))
        cf = ax.contourf(X1, X2, Z_est.detach(), levels=10, cmap='coolwarm')
        plt.colorbar(cf)
        
        ax.grid()
        ax.set_xlabel('$x_1$')
        ax.set_ylabel('$x_2$')
        plt.show()        

    # backward
    optim.zero_grad()
    loss.backward()
    optim.step()
