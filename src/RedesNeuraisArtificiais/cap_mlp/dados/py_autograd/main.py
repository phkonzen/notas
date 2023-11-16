import torch

x = torch.tensor([-0.5, 1., 0.5, 2.],
                 requires_grad=True).reshape(-1,1)
y = torch.tensor([1., 1.5, 2., 3.],
                 requires_grad=True).reshape(-1,1)
xy = torch.hstack((x,y))

u = xy[:,0:1]**2 + torch.log(xy[:,1:2])

# Du = 2*x + 1/y
Du0 = torch.autograd.grad(u.sum(), xy, create_graph=True)[0]

Du1 = torch.autograd.grad(u, xy,
                          grad_outputs=torch.ones_like(u), create_graph=True)[0]

# D2u = 2 - 1/y**2
D2u0 = torch.autograd.grad(Du0.sum(), xy)[0]

D2u1 = torch.autograd.grad(Du1, xy,
                           grad_outputs=torch.ones_like(Du1))[0]
