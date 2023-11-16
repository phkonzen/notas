import torch
import matplotlib.pyplot as plt

# use LaTeX
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "savefig.bbox": 'tight'})
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


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


# verificação
fig = plt.figure(dpi=300)
ax = fig.add_subplot()

x = torch.linspace(a, b,
                   steps=100).reshape(-1,1)

y_esp = fun(x)
ax.plot(x, y_esp, label='fun')

y_est = model(x)
ax.plot(x, y_est.detach(), label='model')

ax.legend()
ax.grid()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')
