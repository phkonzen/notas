import torch

# modelo
## n camadas escondidas
nh = 2
## n neurônios por camada
nn = 50
## fun de ativação
fh = torch.nn.Tanh()
## arquitetura
model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(1,nn))
model.add_module('fun_1', fh)
for layer in range(2, nh+1):
    model.add_module(f'layer_{layer}', torch.nn.Linear(nn,nn))
    model.add_module(f'fun_{layer}', fh)
model.add_module(f'layer_{nh+1}', torch.nn.Linear(nn,1))

# otimizador
optim = torch.optim.Adam(model.parameters(),
                        lr = 1e-2)

# treinamento
ns = 100
nepochs = 10000
nout_loss = 100
tol = 1e-5

for epoch in range(nepochs):

  # samples
  X = 2.*torch.rand((ns,1)) - 1.

  f_exp = torch.cos(torch.pi*X)

  # forward
  X.requires_grad = True
  F = model(X)

  f_est = torch.autograd.grad(
    F, X,
    grad_outputs=torch.ones_like(F),
    retain_graph=True,
    create_graph=True)[0]

  # loss
  loss = torch.mean((f_exp - f_est)**2)

  if ((epoch % nout_loss) == 0):
    print(f'epoch {epoch}: loss = {loss.item():.4e}')

  if (loss.item() < tol):
    print('onvergiu')
    break

  optim.zero_grad()
  loss.backward()
  optim.step()  

import matplotlib.pyplot as plt

X = torch.linspace(-1, 1, 100).reshape(-1, 1)
F_est = model(X).detach().numpy()
F_exp = 1./torch.pi * torch.sin(torch.pi*X)

plt.plot(X, F_exp, label='exp')
plt.plot(X, F_est, label='est') 
plt.legend()
plt.grid()
plt.show()

