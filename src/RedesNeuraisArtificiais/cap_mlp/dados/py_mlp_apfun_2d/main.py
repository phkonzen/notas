import torch

# modelo
nn = 50
model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(2,nn))
model.add_module('fun_1', torch.nn.Tanh())
model.add_module('layer_2', torch.nn.Linear(nn,nn))
model.add_module('fun_2', torch.nn.Tanh())
model.add_module('layer_3', torch.nn.Linear(nn,nn))
model.add_module('fun_3', torch.nn.Tanh())
model.add_module(f'layer_4', torch.nn.Linear(nn,1))

# treinamento

## fun obj
def fun(x1, x2):
    return torch.sin(torch.pi*x1) * \
           torch.sin(torch.pi*x2)

x1_a = -1.
x1_b = 1

x2_a = -1.
x2_b = 1.


## optimizador
optim = torch.optim.SGD(model.parameters(),
                        lr=1e-1, momentum=0.9)

## num de amostras por época
ns = 20
## num max épocas
nepochs = 50000
## tolerância
tol = 1e-4

## amostras de validação
n_val = 50
x1 = torch.linspace(x1_a, x1_b, steps=n_val)
x2 = torch.linspace(x2_a, x2_b, steps=n_val)
X1_val, X2_val = torch.meshgrid(x1, x2, indexing='ij')
X_val = torch.hstack((X1_val.reshape(n_val**2,1),
                      X2_val.reshape(n_val**2,1)))
Y_vest = fun(X1_val, X2_val).reshape(-1,1)

for epoch in range(nepochs):

    # amostras
    X1 = (x1_b - x1_a) * torch.rand(ns**2, 1) + x1_a
    X2 = (x2_b - x2_a) * torch.rand(ns**2, 1) + x2_a
    # X1, X2 = torch.meshgrid(x1, x2, indexing='ij')
    X_train = torch.hstack((X1, X2))
    Y_train = fun(X1, X2).reshape(-1,1)
    
    
    # forward
    Y_est = model(X_train)

    # erro
    loss = torch.mean((Y_est - Y_train)**2)

    if (epoch % 100 == 0):
        print(f'{epoch}: {loss.item():.4e}')

    # backward
    optim.zero_grad()
    loss.backward()
    optim.step()

    # validação
    if (epoch % 100 == 0):
        Y_val = model(X_val)
        loss_val = torch.mean((Y_val - Y_vest)**2)

        print(f"\tloss_val = {loss_val.item():.4e}")
    
        # critério de parada
        if (loss_val.item() < tol):
            break


# verificação

import matplotlib.pyplot as plt
plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'Computer Modern Serif',
    'font.size': 14
    })

fig = plt.figure()
ax = fig.add_subplot()

Y_vest = Y_vest.reshape((n_val, n_val))
Y_val = model(X_val)
Y_val = Y_val.detach().reshape((n_val, n_val))

levels = torch.linspace(-1., 1., steps=10)
ax.contour(X1_val, X2_val, Y_vest, 
           levels=levels, colors='white')
cb = ax.contourf(X1_val, X2_val, Y_val, 
                 levels=levels, extend='both')
ax.scatter(X1.reshape(-1), X2.reshape(-1), 
           s=5, marker='*', color='red')
plt.colorbar(cb)

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')