import torch
from torch import pi, sin
import matplotlib.pyplot as plt

# modelo
nn = 25
model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(2,nn))
model.add_module('fun_1', torch.nn.Tanh())
model.add_module('layer_2', torch.nn.Linear(nn,nn))
model.add_module('fun_2', torch.nn.Tanh())
model.add_module('layer_3', torch.nn.Linear(nn,nn))
model.add_module('fun_3', torch.nn.Tanh())
model.add_module('layer_4', torch.nn.Linear(nn,1))

# otimizador
optim = torch.optim.SGD(model.parameters(), #lr=1e-3)
                        lr = 1e-3, momentum=0.9)

# fonte
def f(x1, x2):
    return 2.*pi**2*sin(pi*x1)*sin(pi*x2)

# treinamento
ns = 25
nepochs = 50000
tol = 1e-3

for epoch in range(nepochs):

    # forward
    x1 = 2.*torch.rand(ns) - 1.
    x2 = 2.*torch.rand(ns) - 1.
    X1, X2 = torch.meshgrid(x1, x2, indexing='ij')
    X = torch.hstack((X1.reshape(-1,1),
                      X2.reshape(-1,1)))
    X.requires_grad = True

    U = model(X)

    # gradientes
    D1U = torch.autograd.grad(
        U, X,
        grad_outputs=torch.ones_like(U),
        retain_graph=True,
        create_graph=True)[0]
    D2UX1 =  torch.autograd.grad(
        D1U[:,0:1], X,
        grad_outputs=torch.ones_like(D1U[:,0:1]),
        retain_graph=True,
        create_graph=True)[0]
    D2UX2 =  torch.autograd.grad(
        D1U[:,1:2], X,
        grad_outputs=torch.ones_like(D1U[:,1:2]),
        retain_graph=True,
        create_graph=True)[0]

    # fonte
    F = f(X1, X2).reshape(-1,1)

    # loss
    
    # pts internos
    lin = torch.mean((F + D2UX1[:,0:1] + D2UX2[:,1:2])**2)

    # contornos
    ## c.c. 1
    Xbc1 = torch.hstack((X1.reshape(-1,1),
                         -torch.ones((ns**2,1))))
    Ubc1 = model(Xbc1)
    lbc1 = torch.mean(Ubc1**2)

    ## c.c. 3
    Xbc3 = torch.hstack((X1.reshape(-1,1),
                         torch.ones((ns**2,1))))
    Ubc3 = model(Xbc3)
    lbc3 = torch.mean(Ubc3**2)
    
    ## c.c. 4
    Xbc4 = torch.hstack((-torch.ones((ns**2,1)),
                         X2.reshape(-1,1)))
    Ubc4 = model(Xbc4)
    lbc4 = torch.mean(Ubc4**2)

    ## c.c. 2
    Xbc2 = torch.hstack((torch.ones((ns**2,1)),
                         X2.reshape(-1,1)))
    Ubc2 = model(Xbc2)
    lbc2 = torch.mean(Ubc2**2)

    loss = lin + lbc1 + lbc2 + lbc3 + lbc4

    if ((epoch % 100 == 0) or (loss.item() == 0)):
        print(f'{epoch}: loss = {loss.item():.4e}')

    if (loss.item() < tol):
        break

    optim.zero_grad()
    loss.backward()
    optim.step()

# verificação
def exact(x1, x2):
    return sin(pi*x1)*sin(pi*x2)

ns = 50
x1 = torch.linspace(-1, 1, steps=ns)
x2 = torch.linspace(-1, 1, steps=ns)
X1, X2 = torch.meshgrid(x1, x2, indexing='ij')

Uexp = exact(X1, X2)

X = torch.hstack((X1.reshape(-1,1),
                  X2.reshape(-1,1)))
Uest = model(X).detach().reshape((ns, ns))

levels = 10
cb = plt.contourf(X1, X2, Uest, levels=levels)
plt.contour(X1, X2, Uexp, levels=levels, colors='white')
plt.colorbar(cb)
plt.show()
