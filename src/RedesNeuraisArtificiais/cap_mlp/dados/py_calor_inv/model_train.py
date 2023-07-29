import torch
import numpy as np
import pickle
import matplotlib.pyplot as plt

# training data
X_train = torch.from_numpy(np.load('x_train.npy')).type(torch.float32)
Y_train = torch.from_numpy(np.load('y_train.npy')).type(torch.float32)

ns = X_train.size(0)
nin = X_train.size(1)
nout = Y_train.size(1)


# modelo
model = torch.nn.Sequential(
    torch.nn.Linear(nin,50),
    torch.nn.Tanh(),
    torch.nn.Linear(50,50),
    torch.nn.Tanh(),
    torch.nn.Linear(50,50),
    torch.nn.Tanh(),
    torch.nn.Linear(50,50),
    torch.nn.Tanh(),
    torch.nn.Linear(50,nout)
)

# otimizador
#optim = torch.optim.SGD(model.parameters(),
#                        lr = 1e-2, momentum=0.9)
optim = torch.optim.Adam(model.parameters(),
                        lr = 1e-3)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optim,
                                                      factor=0.3,
                                                       patience=250)


# treinamento
nepochs = 50000
tol = 1e-4

for epoch in range(nepochs):
    
    # forward
    Y_est = model(X_train)
    # loss
    loss = torch.mean((Y_est - Y_train)**2)
    lr = optim.param_groups[-1]['lr']
    print(f'{epoch}: loss = {loss.item()}, lr = {lr:.4e}')
    if (loss.item() < tol):
        break

    # backward
    # scheduler.step(loss)
    optim.zero_grad()
    loss.backward()
    optim.step()

# gráfico de calibração
plt.plot([0,1],[0,1],ls='--',color='gray')
plt.plot(Y_train[:,0], Y_est[:,0].detach(),
         ls='', marker='o', color='blue')
plt.plot(Y_train[:,1], Y_est[:,1].detach(),
         ls='', marker='o', color='red')
plt.grid()
plt.show()

# save for later
torch.save(model, 'model.pt')
