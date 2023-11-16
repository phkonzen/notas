import torch
from torch import pi, sin, cos
import matplotlib.pyplot as plt

# input
x = torch.linspace(-1., 1., steps=50)
x.requires_grad = True

# forward
y = sin(pi*x)

# backward
# y.backward(torch.ones_like(x))
dydx = torch.autograd.grad(y, x,
                           retain_graph = True,
                           create_graph = True,
                           grad_outputs = torch.ones_like(x))[0]
d2ydx2 = torch.autograd.grad(dydx, x,
                           grad_outputs = torch.ones_like(dydx))[0]



# gráfico
plt.plot(x.detach(), torch.sin(pi*x.detach()), ls='-', label='f')
plt.plot(x.detach(), pi*torch.cos(pi*x.detach()), ls='-', label='df/dx')
plt.plot(x.detach(), dydx.detach(), ls='--', label='autograd d1')

plt.plot(x.detach(), -pi**2*torch.sin(pi*x.detach()), ls='-', label='d2f/dx2')
plt.plot(x.detach(), d2ydx2.detach(), ls='--', label='autograd d2')

plt.grid()
plt.legend()
plt.show()

