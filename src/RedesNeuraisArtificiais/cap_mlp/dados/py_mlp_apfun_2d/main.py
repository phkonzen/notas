import torch
import matplotlib.pyplot as plt

# modelo
nh = 25
model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(2,nh))
model.add_module('fun_1', torch.nn.Tanh())
model.add_module('layer_2', torch.nn.Linear(nh,nh))
model.add_module('fun_2', torch.nn.Tanh())
model.add_module('layer_3', torch.nn.Linear(nh,nh))
model.add_module('fun_3', torch.nn.Tanh())
model.add_module(f'layer_4', torch.nn.Linear(nh,1))

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
                        lr=5e-2, momentum=0.9)

## num de amostras por época
ns = 10
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
    x1 = (x1_b - x1_a) * torch.rand(ns) + x1_a
    x2 = (x2_b - x2_a) * torch.rand(ns) + x2_a
    X1, X2 = torch.meshgrid(x1, x2, indexing='ij')
    X_train = torch.hstack((X1.reshape(-1,1),
                            X2.reshape(-1,1)))
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


# # verificação
fig = plt.figure()
ax = fig.add_subplot()

Y_vest = Y_vest.reshape((n_val, n_val))
Y_val = Y_val.detach().reshape((n_val, n_val))

levels=10
ax.contour(X1_val, X2_val, Y_vest, levels=levels, colors='white')
cb = ax.contourf(X1_val, X2_val, Y_val, levels=levels)
plt.colorbar(cb)

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
plt.show()
