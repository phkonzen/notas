import torch
from torch import nn
from torch import autograd

# modelo

model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(1,25))
model.add_module('fun_1', torch.nn.Tanh())
model.add_module('layer_2', torch.nn.Linear(25,25))
model.add_module('fun_2', torch.nn.Tanh())
model.add_module('layer_3', torch.nn.Linear(25,1))

# treinamento

## fun obj
fun = lambda x: torch.sin(torch.pi*x)
a = -1.
b = 1.

## optimizador
optim = torch.optim.SGD(model.parameters(),
                        lr=1e-1, momentum=0.9)

## num de amostras por época
ns = 100
## num max épocas
nepochs = 5000
## tolerância
tol = 1e-5

## amostras de validação
X_val = torch.linspace(a, b, steps=100).reshape(-1,1)
y_vest = fun(X_val)

for epoch in range(nepochs):

    # amostras
    X_train = (a - b) * torch.rand((ns,1)) + b
    y_train = fun(X_train)
    
    # forward
    y_est = model(X_train)

    # erro
    loss = torch.mean((y_est - y_train)**2)

    print(f'{epoch}: {loss.item():.4e}')

    # backward
    optim.zero_grad()
    loss.backward()
    optim.step()

    # validação
    y_val = model(X_val)
    loss_val = torch.mean((y_val - y_vest)**2)
    print(f"\tloss_val = {loss_val.item():.4e}")
    
    # critério de parada
    if (loss_val.item() < tol):
        break

# autograd MLP
X_val.requires_grad = True
# forward
y_val = model(X_val)
# gradient
dydx = autograd.grad(
    y_val, X_val,
    grad_outputs=torch.ones_like(y_val))[0]

# gráfico
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

fig = plt.figure()
ax = fig.add_subplot()

# dfun
x = X_val.detach()
df = torch.pi*torch.cos(torch.pi*x)
ax.plot(x, df, ls='-', label="$f'(x)$")

# model autograd
ax.plot(x, dydx.detach(), ls='--', label="$\\mathcal{N}'(x)$")

ax.legend()
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')
