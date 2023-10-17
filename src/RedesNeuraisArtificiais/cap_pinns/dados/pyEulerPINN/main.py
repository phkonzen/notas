import torch
from scipy.integrate import quad

# model
## num hidden layers
nh = 2
## num neurons per hidden layer
nn = 50
## activation fun in hidden layers
fh = torch.nn.Tanh()
## model architecture
model = torch.nn.Sequential()
model.add_module('layer_1', torch.nn.Linear(1,nn))
model.add_module('fun_1', fh)
for l in range(2, nh):
    model.add_module(f'layer_{l}', torch.nn.Linear(nn,nn))
    model.add_module(f'fun_{l}', fh)
model.add_module(f'layer_{nh}', torch.nn.Linear(nn,1))

# IVP params

## init time
t0 = 0.
## init condition
y0 = 0.5
## final time
tf = 1.

## num of time samples
ns = 10
## time step
ht = (tf - t0)/ns
## time samples
ts = torch.linspace(t0, tf, ns+1).reshape(-1,1)

## rhs
def g(t, y):
    return y + torch.sin(t)

# training
## num of epochs
nepochs = 10000
## output loss freq
eout = 100
## tolerance
tol = 1e-4
## early-stop
n_iter_no_change = 100

## optimizer
optim = torch.optim.Adam(model.parameters(), lr=1e-3)

# training loop
count_no_change = 0
best_loss = 1e38
for epoch in range(nepochs):

    # forward
    yy = model(ts)

    # loss
    ## t>0
    lup = torch.mean(((yy[1:] - yy[:-1])/ht \
                      - g(ts[:-1], yy[:-1]))**2)
    ## t = 0
    lic = (yy[0] - y0)**2

    loss_train = lup + lic        

    # backward
    optim.zero_grad()
    loss_train.backward()
    optim.step()

    # validation
    ys = model(ts).detach()
    yv = torch.empty_like(ys)
    yv[0] = y0
    for s in range(1,ns+1):
        yv[s] = yv[s-1] + quad(lambda t: g(torch.tensor([[t]]),
                                      model(torch.tensor([[t]])).detach()),
                               ts[s-1], ts[s])[0]
    loss_valid = torch.mean((ys - yv)**2)

    if (loss_valid < best_loss):
        torch.save(model, 'model.pt')
        best_loss = loss_valid
        count_no_change = 0
    else:
        count_no_change += 1

    if ((epoch % eout == 0) or (count_no_change == 0)):
        msg = f'{epoch}: train = {loss_train.item():.4e}, valid = {loss_valid.item():.4e}'
        if (count_no_change == 0):
            msg += ' (best)'
        print(msg)

    if ((best_loss < tol) or (count_no_change > n_iter_no_change)):
        break

    if (loss_train < tol):
        break
