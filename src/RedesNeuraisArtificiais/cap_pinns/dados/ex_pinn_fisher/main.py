import torch

# modelo
nh = 4
nn = 50
fun = torch.nn.Tanh()
model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(2, nn))
model.add_module('fun_1', fun)
for l in range(2, nh+1):
    model.add_module(f'layer_{l}', torch.nn.Linear(nn, nn))
    model.add_module(f'fun_{l}', fun)
model.add_module(f'layer_{nh+1}', torch.nn.Linear(nn, 1))

# parâmetro
rgn = [5., 7]
model.lmbda = torch.nn.Parameter(
    data=(rgn[1]-rgn[0])*torch.rand(1)+rgn[0])

# otimizador
optim = torch.optim.Adam(model.parameters(), lr=0.001)

# parâmetros do problema
tf = 1.

# solução analítica
lmbda = torch.tensor([6.])
def ua(t,x, lmbda=lmbda):
    return 1./(1.+torch.exp(torch.sqrt(lmbda/6.)*x-5./6*lmbda*t))**2

# condição inicial
def u0(x, lmbda=lmbda):
    return 1./(1.+torch.exp(torch.sqrt(lmbda/6)*x))**2

# amostras
ts = torch.tensor([0.1, 0.2, 0.3])
xs = torch.tensor([0.25, 0.5, 0.75])
T, X = torch.meshgrid(ts, xs, indexing='ij')
Ss = torch.hstack((T.reshape(-1,1), X.reshape(-1,1)))
Us_exp = ua(T, X).reshape(-1,1)

# treinamento
nepochs = 50000
tol = 1e-5

eout = 100

sin = 50
penalty = 1e1

for epoch in range(nepochs):

    # forward

    ## pts internos
    tsin = tf*torch.rand(sin, 1)
    xsin = torch.rand(sin, 1)
    Sin = torch.hstack((tsin, xsin))
    Sin.requires_grad = True

    Uin = model(Sin)

    ## loss pts internos
    DUin = torch.autograd.grad(
        Uin, Sin, 
        torch.ones_like(Uin), 
        create_graph=True,
        retain_graph=True)[0]
    Uin_t = DUin[:,0:1]
    Uin_x = DUin[:,1:2]

    Uin_xx = torch.autograd.grad(
        Uin_x, Sin,
        torch.ones_like(Uin_x),
        create_graph=True,
        retain_graph=True)[0][:,1:2]
    
    
    lin = torch.mean((Uin_t - Uin_xx \
                      - model.lmbda*Uin*(1-Uin))**2)
    
    ## cond. inicial
    S0 = torch.hstack((torch.zeros_like(xsin), xsin))

    U0 = model(S0)

    ## loss cond. inicial
    l0 = torch.mean((U0 - u0(xsin))**2)

    ## cond. de contorno
    Sbc0 = torch.hstack((tsin, torch.zeros_like(xsin)))
    Sbc1 = torch.hstack((tsin, torch.ones_like(xsin)))
    Sbc = torch.vstack((Sbc0, Sbc1))

    Ubc_exp = ua(Sbc[:,0:1],Sbc[:,1:2])
    Ubc_est = model(Sbc)

    ## loss cond. de contorno    
    lbc = torch.mean((Ubc_est - Ubc_exp)**2)

    ## amostras
    Us_est = model(Ss)

    ## loss amostras
    ls = torch.mean((Us_est - Us_exp)**2)

    ## loss total
    loss = lin + l0 + lbc + penalty*ls 

    if ((epoch % eout == 0) or (loss.item() < tol)):
        print(f'epoch: {epoch}, '\
              + f'loss={loss.item():.4e}, '\
              + f'lmbda={model.lmbda.item():.3f}')
    
    if (loss.item() < tol):
        break
        
    optim.zero_grad()
    loss.backward()
    optim.step()

# verificação
t = torch.linspace(0., tf, 11)
x = torch.linspace(0., 1., 100)
T,X = torch.meshgrid(t,x, indexing='ij')
S = torch.hstack((T.reshape(-1,1), X.reshape(-1,1)))
U_exp = ua(T,X)
U_est = model(S).detach().reshape((t.size(0), x.size(0)))

import matplotlib.pyplot as plt
plt.rcParams.update({'text.usetex': True,
                     'font.family': 'Computer Modern Roman'})
fig = plt.figure(dpi=300)
ax = fig.add_subplot()
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$u(t,x)$')
ax.set_ylim(-0.1, 1)
ax.set_xticks([0., 0.25, 0.5, 0.75, 1.])

## t=0.
ax.text(0.3, 0.12, '$t=0.0$')
ax.plot(x, U_exp[0,:], ls='-', color=f'C{k}', label='Analítica')
ax.plot(x, U_est[0,:], ls='--', color=f'C{k}', label='PINN')

## t=0.1, 0.2, 0.3.
xs = xs.reshape(-1,1)
ax.text(0.3, 0.225, '$t=0.1$')
ax.plot(xs, ua(torch.full_like(xs, 0.1),xs), ls='', marker='o', color='red', label='Amostras')
ax.plot(xs, ua(torch.full_like(xs, 0.2),xs), ls='', marker='o', color='red')
ax.plot(xs, ua(torch.full_like(xs, 0.3),xs), ls='', marker='o', color='red')

for k,_ in enumerate(t[1:]):
    ax.plot(x, U_exp[k,:], ls='-', color=f'C{k+1}')
    ax.plot(x, U_est[k,:], ls='--', color=f'C{k+1}')

ax.legend(loc='lower left')
plt.savefig('fig.pdf', bbox_inches='tight')
plt.savefig('fig.png', bbox_inches='tight')
#plt.show()


