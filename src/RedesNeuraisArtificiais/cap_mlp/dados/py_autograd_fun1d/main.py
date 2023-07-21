import torch
import matplotlib.pyplot as plt

# modelo

model = torch.nn.Sequential(
    torch.nn.Linear(1,50),
    torch.nn.Tanh(),
    torch.nn.Linear(50,25),
    torch.nn.Tanh(),
    torch.nn.Linear(25,1)
    )

# treinamento

## fun obj
fobj = lambda x: torch.sin(torch.pi*x)
a = -1.
b = 1.

## optimizador
optim = torch.optim.SGD(model.parameters(),
                        lr=1e-1, momentum=0.9)

## função erro
loss_fun = torch.nn.MSELoss()

## num de amostras por época
ns = 100
## num max épocas
nepochs = 10000
## tolerância
tol = 1e-5

for epoch in range(nepochs):

    # amostras
    X_train = (a - b) * torch.rand((ns,1)) + b
    y_train = fobj(X_train)
    
    # forward
    y_est = model(X_train)

    # erro
    loss = loss_fun(y_est, y_train)

    lr = optim.param_groups[-1]['lr']
    print(f'{epoch}: loss = {loss.item():.4e}, lr = {lr:.4e}')

    # critério de parada
    if ((loss.item() < tol) or (lr <= 1e-7)):
        break

    # backward
    optim.zero_grad()
    loss.backward()
    optim.step()


# verificação
fig = plt.figure()
ax = fig.add_subplot()

xx = torch.linspace(a, b,
                    steps=50).reshape(-1,1)
# y' = cos(x)
dy_esp = torch.pi*torch.cos(torch.pi*xx)
ax.plot(xx, dy_esp, label="$f'(x) = \\pi\cos(\\pi x)$")

# model autograd
dy_est = torch.empty_like(xx)
for i,x in enumerate(xx):
    x.requires_grad = True
    y = model(x)
    y.backward()
    dy_est[i] = x.grad
ax.plot(xx, dy_est, label='$d\\tilde{y}/dx$')

ax.legend()
ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
