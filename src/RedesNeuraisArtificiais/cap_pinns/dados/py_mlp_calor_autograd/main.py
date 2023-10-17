import torch
from torch import pi, sin, exp
from collections import OrderedDict
import matplotlib.pyplot as plt

# modelo
hidden = [50]*8
activation = torch.nn.Tanh()
layerList = [('layer_0', torch.nn.Linear(2, hidden[0])),
             ('activation_0', activation)]
for l in range(len(hidden)-1):
    layerList.append((f'layer_{l+1}',
                      torch.nn.Linear(hidden[l], hidden[l+1])))
    layerList.append((f'activation_{l+1}', activation))
layerList.append((f'layer_{len(hidden)}', torch.nn.Linear(hidden[-1], 1)))
layerDict = OrderedDict(layerList)
model = torch.nn.Sequential(OrderedDict(layerDict))

# otimizador
# optim = torch.optim.SGD(model.parameters(),
#                          lr = 1e-3, momentum=0.85)
optim = torch.optim.Adam(model.parameters(),
                         lr = 1e-2)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optim,
                                                       factor=0.1,
                                                       patience=100)

# treinamento
nt = 10
tt = torch.linspace(0., 1., nt+1)
nx = 20
xx = torch.linspace(-1., 1., nx+1)
T,X = torch.meshgrid(tt, xx, indexing='ij')
tt = tt.reshape(-1,1)
xx = xx.reshape(-1,1)

# t = 0
Sic = torch.hstack((torch.zeros_like(xx), xx))
Uic = sin(pi*xx)

# x = -1
Sbc0 = torch.hstack((tt[1:,:], -1.*torch.ones_like(tt[1:,:])))
Ubc0 = torch.zeros_like(tt[1:,:])

# x = 1
Sbc1 = torch.hstack((tt[1:,:], 1.*torch.ones_like(tt[1:,:])))
Ubc1 = torch.zeros_like(tt[1:,:])

# pts internos
tin = tt[1:,:]
xin = xx[1:-1,:]
Sin = torch.empty((nt*(nx-1), 2))
Fin = torch.empty((nt*(nx-1), 1))
s = 0
for i,t in enumerate(tin):
    for j,x in enumerate(xin):
        Sin[s,0] = t
        Sin[s,1] = x
        Fin[s,0] = (pi**2 - 1.)*exp(-t)*sin(pi*x)
        s += 1
tin = torch.tensor(Sin[:,0:1], requires_grad=True)
xin = torch.tensor(Sin[:,1:2], requires_grad=True)
Sin = torch.hstack((tin,xin))

# training
nepochs = 50001
tol = 1e-4
nout = 100

for epoch in range(nepochs):

    # loss

    ## c.i.
    Uest = model(Sic)
    lic = torch.mean((Uest - Uic)**2)
    
    ## residual
    U = model(Sin)
    U_t = torch.autograd.grad(
        U, tin,
        grad_outputs=torch.ones_like(U),
        retain_graph=True,
        create_graph=True)[0]
    U_x = torch.autograd.grad(
        U, xin,
        grad_outputs=torch.ones_like(U),
        retain_graph=True,
        create_graph=True)[0]
    U_xx = torch.autograd.grad(
        U_x, xin,
        grad_outputs=torch.ones_like(U_x),
        retain_graph=True,
        create_graph=True)[0]
    res = U_t - U_xx - Fin
    lin = torch.mean(res**2)

    ## c.c. x = -1
    Uest = model(Sbc0)
    lbc0 = torch.mean(Uest**2)

    ## c.c. x = 1
    Uest = model(Sbc1)
    lbc1 = torch.mean(Uest**2)

    loss = lin + lic + lbc0 + lbc1

    lr = optim.param_groups[-1]['lr']
    print(f'{epoch}: loss = {loss.item():.4e}, lr = {lr:.4e}')

    # backward
    scheduler.step(loss)
    optim.zero_grad()
    loss.backward()
    optim.step()


    # output
    if ((epoch % nout == 0) or (loss.item() < tol)):
        plt.close()
        fig = plt.figure(dpi=300)
        nt = 10
        tt = torch.linspace(0., 1., nt+1)
        nx = 20
        xx = torch.linspace(-1., 1., nx+1)
        T,X = torch.meshgrid(tt, xx, indexing='ij')
        Uesp = torch.empty_like(T)
        M = torch.empty(((nt+1)*(nx+1),2))
        s = 0
        for i,t in enumerate(tt):
            for j,x in enumerate(xx):
                Uesp[i,j] = exp(-t)*sin(pi*x)
                M[s,0] = t
                M[s,1] = x
                s += 1
        Uest = model(M)
        Uest = Uest.detach().reshape(nt+1,nx+1)
        l2rel = torch.norm(Uest - Uesp)/torch.norm(Uesp)
        
        ax = fig.add_subplot()
        cb = ax.contourf(T, X, Uesp,
                         levels=10)
        fig.colorbar(cb)
        cl = ax.contour(T, X, Uest,
                        levels=10, colors='white')
        ax.clabel(cl, fmt='%.1f')
        ax.set_xlabel('$t$')
        ax.set_ylabel('$x$')
        plt.title(f'{epoch}: loss = {loss.item():.4e}, l2rel = {l2rel:.4e}')
        plt.savefig(f'./results/sol_{(epoch//nout):0>6}.png')

    if ((loss.item() < tol) or (lr < 1e-6)):
        break
    
