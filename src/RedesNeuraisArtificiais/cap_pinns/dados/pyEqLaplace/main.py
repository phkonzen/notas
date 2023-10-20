import torch
import matplotlib.pyplot as plt
import random
import numpy as np

# modelo
## n camadas escondidas
nh = 3
## n neurônios por camada
nn = 50
## fun de ativação
fh = torch.nn.Tanh()
## arquitetura
model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(2,nn))
model.add_module('fun_1', fh)
for layer in range(2, nh):
    model.add_module(f'layer_{layer}', torch.nn.Linear(nn,nn))
    model.add_module(f'fun_{layer}', fh)
model.add_module(f'layer_{nh}', torch.nn.Linear(nn,1))

# SGD - (Stochastic) Gradient Descent
# optim = torch.optim.SGD(model.parameters(),
#                         lr = 1e-2,
#                         momentum = 0.9)
optim = torch.optim.Adam(model.parameters(),
                        lr = 1e-2)


# params treinamento
## n épocas
nepochs = 10001
## freq output loss
nout_loss = 100
## stop criterion
tol = 1e-4

## n amostras por eixo
ns = 101

lloss = []
for epoch in range(nepochs):

    # forward
    
    ## internal pts samples
    Xin = torch.rand((ns, 2), requires_grad=True)
    Uin = model(Xin)

    ## loss internal pts
    D1Uin = torch.autograd.grad(
        Uin, Xin,
        grad_outputs=torch.ones_like(Uin),
        retain_graph=True,
        create_graph=True)[0]
    D2Uin = torch.autograd.grad(
        D1Uin, Xin,
        grad_outputs=torch.ones_like(D1Uin),
        retain_graph=True,
        create_graph=True)[0]

    lin = torch.mean((D2Uin[:,0] + D2Uin[:,1])**2)

    ## bc 1
    xx = torch.rand((ns, 1))
    yy = torch.zeros((ns,1))
    Xbc1 = torch.hstack((xx, yy))
    Ubc1 = model(Xbc1)

    ## loss bc 1
    Uexp = xx*(1. - xx)
    lbc1 = torch.mean((Ubc1 - Uexp)**2)

    ## bc 3
    xx = torch.rand((ns, 1))
    yy = torch.ones((ns,1))
    Xbc3 = torch.hstack((xx, yy))
    Ubc3 = model(Xbc3)

    ## loss bc 3
    Uexp = xx*(1. - xx)
    lbc3 = torch.mean((Ubc3 - Uexp)**2)

    ## bc 2
    xx = torch.ones((ns, 1))
    yy = torch.rand((ns,1))
    Xbc2 = torch.hstack((xx, yy))
    Ubc2 = model(Xbc2)

    ## loss bc 2
    Uexp = yy*(yy - 1.)
    lbc2 = torch.mean((Ubc2 - Uexp)**2)

    ## bc 4
    xx = torch.zeros((ns, 1))
    yy = torch.rand((ns,1))
    Xbc4 = torch.hstack((xx, yy))
    Ubc4 = model(Xbc4)

    ## loss bc 3
    Uexp = yy*(yy - 1.)
    lbc4 = torch.mean((Ubc4 - Uexp)**2)

    # loss function
    loss = lin + lbc1 + lbc2 + lbc3 + lbc4

    lloss.append(loss.item())
    
    if (((epoch % nout_loss) == 0) or (loss.item() < tol)):
        print(f'{epoch}: loss = {loss.item():.4e}')
    
        # gráfico
        fig = plt.figure()
        ax = fig.add_subplot()

        npts = 50
        xx = torch.linspace(0., 1., npts)
        yy = torch.linspace(0., 1., npts)
        X, Y = torch.meshgrid(xx, yy)
        # exact
        Uexp = X*(1. - X) - Y*(1. - Y)
        c = ax.contour(X, Y, Uexp, levels=10, colors='white')
        ax.clabel(c)

        M = torch.hstack((X.reshape(-1,1),
                          Y.reshape(-1,1)))
        Uest = model(M).detach()
        Uest = Uest.reshape((npts, npts))
        cf = ax.contourf(X, Y, Uest, levels=10, cmap='coolwarm')
        plt.colorbar(cf)
        
        ax.grid()
        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        plt.title(f"epoch = {epoch}, loss = {loss.item():.4e}")
        plt.savefig(f'results/sol_{epoch:0>6}.png', bbox_inches='tight')
        plt.close()

    if (loss.item() < tol):
        break

    # backward
    optim.zero_grad()
    loss.backward()
    optim.step()


fig = plt.figure()
ax = fig.add_subplot()
ax.plot(lloss)
ax.set_yscale('log')
plt.show()
