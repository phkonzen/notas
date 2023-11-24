import torch
from torch import pi, sin

# modelo
nn = 50
model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(2,nn))
model.add_module('fun_1', torch.nn.Tanh())
model.add_module('layer_2', torch.nn.Linear(nn,nn))
model.add_module('fun_2', torch.nn.Tanh())
model.add_module('layer_3', torch.nn.Linear(nn,nn))
model.add_module('fun_3', torch.nn.Tanh())
model.add_module('layer_4', torch.nn.Linear(nn,1))

# otimizador
optim = torch.optim.SGD(model.parameters(),
                        lr = 1e-3, momentum=0.9)

# fonte
def f(x1, x2):
    return 2.*pi**2*sin(pi*x1)*sin(pi*x2)

# treinamento
ns_in = 400
ns_cc = 20
nepochs = 50000
tol = 1e-3

## pontos de validação
ns_val = 50
x1_val = torch.linspace(-1., 1., steps=ns_val)
x2_val = torch.linspace(-1., 1., steps=ns_val)
X1_val, X2_val = torch.meshgrid(x1_val, x2_val, indexing='ij')
X_val = torch.hstack((X1_val.reshape(ns_val**2,1),
                      X2_val.reshape(ns_val**2,1)))

for epoch in range(nepochs):
    
    # forward
    X1 = 2.*torch.rand(ns_in, 1) - 1.
    X2 = 2.*torch.rand(ns_in, 1) - 1.
    X = torch.hstack((X1, X2))
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
    F = f(X1, X2)
    
    # loss pts internos
    lin = torch.mean((F + D2UX1[:,0:1] + D2UX2[:,1:2])**2)
    
    # contornos
    ## c.c. 1
    X1 = 2.*torch.rand(ns_cc, 1) - 1.
    Xcc1 = torch.hstack((X1, -torch.ones((ns_cc,1))))
    Ucc1 = model(Xcc1)
    
    ## c.c. 3
    Xcc3 = torch.hstack((X1, torch.ones((ns_cc,1))))
    Ucc3 = model(Xcc3)
    
    ## c.c. 4
    X2 = 2.*torch.rand(ns_cc, 1) - 1.
    Xcc4 = torch.hstack((-torch.ones((ns_cc,1)), X2))
    Ucc4 = model(Xcc4)
    
    ## c.c. 2
    Xcc2 = torch.hstack((torch.ones((ns_cc,1)), X2))
    Ucc2 = model(Xcc2)
    
    # loss cc
    lcc = 1./(4.*ns_cc) * torch.sum(Ucc1**2 + Ucc2**2 + Ucc3**2 + Ucc4**2)
    
    # loss
    loss = lin + lcc
    
    if ((epoch % 500 == 0) or (loss.item() < tol)):
        print(f'{epoch}: loss = {loss.item():.4e}')        

        if (loss.item() < tol):
            break
    
    optim.zero_grad()
    loss.backward()
    optim.step()

# verificação
import matplotlib.pyplot as plt
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'Computer Modern Serif',
    'font.size': 14
    })

fig = plt.figure()
ax = fig.add_subplot()

## solução analítica
def ua(x1, x2):
    return sin(pi*x1)*sin(pi*x2)

Uexp = ua(X1_val, X2_val)

Uest = model(X_val).detach().reshape((ns_val, ns_val))

levels = torch.linspace(-1., 1., steps=10)
cb = ax.contourf(X1_val, X2_val, Uest, levels=levels, extend='both')
ax.contour(X1_val, X2_val, Uexp, levels=levels, colors='white')
## training pts
ax.scatter(X[:,0].detach(), X[:,1].detach(), 
           s=5, marker='*', color='red')
ax.scatter(X1, -torch.ones((ns_cc,1)), 
           s=5, marker='*', color='black')
ax.scatter(X1, torch.ones((ns_cc,1)), 
           s=5, marker='*', color='black')
ax.scatter(-torch.ones((ns_cc,1)), X2,
           s=5, marker='*', color='black')
ax.scatter(torch.ones((ns_cc,1)), X2,
           s=5, marker='*', color='black')
ax.set_xlim(-1.01, 1.01)
ax.set_ylim(-1.01, 1.01)
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
plt.colorbar(cb)
plt.savefig('fig.pdf', bbox_inches='tight')
plt.savefig('fig.png', bbox_inches='tight')