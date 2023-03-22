import torch

model = torch.nn.Sequential(
    torch.nn.Linear(1,5),
    torch.nn.Sigmoid(),
    torch.nn.Linear(5,1),
    torch.nn.Sigmoid()
)

#x = torch.ones(1, requires_grad=True)
#y = torch.sigmoid(x)
#y.backward()

X = torch.Tensor([[1., 1.],
                  [1., -1.],
                  [-1., 1.],
                  [-1., -1.]], requires_grad())
y = torch.Tensor([1., -1., -1., -1.])

nepochs = 1
tol = 1e-3

ns = X.size(0)
for e in range(nepochs):
    # estimativa
    y_est = model(X)
    # erro
    loss = 1./ns * torch.sum((yest - y)**2)

    if (loss < tol):
        break
    else:
        for s in range(ns):
            
