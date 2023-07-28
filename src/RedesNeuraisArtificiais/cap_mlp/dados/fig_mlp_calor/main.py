import torch
from torch import pi, sin, exp
import matplotlib.pyplot as plt

# modelo
model = torch.nn.Sequential(
    torch.nn.Linear(2,500),
    torch.nn.ELU(),
    torch.nn.Linear(500,500),
    torch.nn.ELU(),
    torch.nn.Linear(500,500),
    torch.nn.ELU(),
    torch.nn.Linear(500,1)
)

# otimizador
optim = torch.optim.SGD(model.parameters(),
                        lr = 1e-2, momentum = 0.9)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optim)

# amostras
nt = 10
ht = 1./nt
tt = torch.linspace(0., 1., nt+1)
nx = 20
hx = 2./nx
xx = torch.linspace(-1., 1., nx+1)
T, X = torch.meshgrid(tt, xx,
                      indexing='ij')
Uesp = torch.empty_like(T)
nsamples = (nt+1)*(nx+1)
M = torch.empty((nsamples, 2))
s = 0
for i,t in enumerate(tt):
    for j,x in enumerate(xx):
        Uesp[i,j] = exp(-t)*sin(pi*x)
        M[s,0] = t
        M[s,1] = x
        s += 1

# treinamento
nepochs = 10001
tol = 1e-5
nout = 100

for epoch in range(nepochs):

    # forward
    Uest = model(M)

    # loss
    ## c.i.
    lci = torch.tensor([0.])
    for j,x in enumerate(xx):
        s = j
        assert(M[s,1] == x)
        uesp = sin(pi*x)
        lci += (Uest[s] - uesp)**2
    ## pts internos
    lin = torch.tensor([0.])
    for i in range(1,nt+1):
        for j in range(1,nx):
            s = j + i*(nx+1)
            # u_t
            l = (Uest[s] - Uest[s-nx-1])/ht
            # u_xx
            l -= (Uest[s-1] - 2*Uest[s] + Uest[s+1])/hx**2
            # f
            l -= (pi**2 - 1.)*exp(-M[s,0])*sin(pi*M[s,1])
            lin += l**2
    ## c.c.
    lcc = torch.tensor([0.])
    for i,t in enumerate(tt[1:]):
        # x = 0
        s = i*(nx+1)
        lcc += Uest[s]**2
        # x = 1
        s = nx + i*(nx+1)
        lcc += Uest[s]**2

    loss = (lci + lin + lcc)/nsamples

    lr = optim.param_groups[-1]['lr']
    print(f'{epoch}: loss = {loss.item():.4e}, lr = {lr:.4e}')

    # output
    if ((epoch % nout == 0) or (loss.item() < tol)):
        plt.close()
        fig = plt.figure(dpi=300)
        ax = fig.add_subplot()
        cb = ax.contourf(T, X, Uesp,
                         levels=10)
        fig.colorbar(cb)
        cl = ax.contour(T, X, Uest.detach().reshape(nt+1,nx+1),
                        levels=10, colors='white')
        ax.clabel(cl, fmt='%.1f')
        ax.set_xlabel('$t$')
        ax.set_ylabel('$x$')
        plt.title(f'{epoch}: loss = {loss.item():.4e}, lr = {lr:.4e}')
        plt.savefig(f'fig.png')

    if (loss.item() < tol):
        break
    
    # backward
    scheduler.step(loss)
    optim.zero_grad()
    loss.backward()
    optim.step()
