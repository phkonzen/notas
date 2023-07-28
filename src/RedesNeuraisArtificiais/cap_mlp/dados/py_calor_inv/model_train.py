import torch
import numpy as np
import pickle

# training data
X_train = torch.from_numpy(np.load('x_train.npy')).type(torch.float32)
Y_train = torch.from_numpy(np.load('y_train.npy')).type(torch.float32)

ns = X_train.size(0)
nin = X_train.size(1)
nout = Y_train.size(1)


# modelo
model = torch.nn.Sequential(
    torch.nn.Linear(nin,100),
    torch.nn.Tanh(),
    torch.nn.Linear(100,100),
    torch.nn.Tanh(),
    torch.nn.Linear(100,100),
    torch.nn.Tanh(),
    torch.nn.Linear(100,nout),
    torch.nn.Sigmoid()
)

# otimizador
optim = torch.optim.SGD(model.parameters(),
                        lr = 1e-2, momentum=0.9)

# treinamento
nepochs = 10000
tol = 1e-2

for epoch in range(nepochs):
    
    # forward
    Y_est = model(X_train)
    # loss
    loss = torch.mean((Y_est - Y_train)**2)
    print(f'{epoch}: loss = {loss.item()}')
    if (loss.item() < tol):
        break

    # backward
    optim.zero_grad()
    loss.backward()
    optim.step()

# save for later
torch.save(model, 'model.pt')
