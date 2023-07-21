import torch

# modelo
model = torch.nn.Linear(1,1)

# treinamento

## optimizador
optim = torch.optim.SGD(model.parameters(),
                        lr=1e-1)

## função erro
loss_fun = torch.nn.MSELoss()

## dados de treinamento
X_train = torch.tensor([[0.5],
                        [1.0],
                        [1.5],
                        [2.0]])
y_train = torch.tensor([[1.2],
                        [2.1],
                        [2.6],
                        [3.6]])

## num max épocas
nepochs = 5000
nstop = 10

cstop = 0
loss_min = torch.finfo().max
for epoch in range(nepochs):

    # forward
    y_est = model(X_train)

    # erro
    loss = loss_fun(y_est, y_train)

    # critério de parada
    if (loss.item() >= loss_min):
        cstop += 1
    else:
        loss_min = loss.item()
        cstop = 0

    print(f'{epoch}: {loss.item():.4e}, '\
          + f'cstop = {cstop}/{nstop}')

    if (cstop == nstop):
        break

    # backward
    optim.zero_grad()
    loss.backward()
    optim.step()


# verificação
print(f'w = {model.weight}')
print(f'b = {model.bias}')

# autograd dy/dx

## forward
x = torch.tensor([[1.]],
                 requires_grad=True)
y = model(x)

## backward
y.backward()
dydx = x.grad
print(f'dy/dx = {dydx}')
