import torch
from torch import pi, pi, sin, cos
import matplotlib.pyplot as plt

# input
x = torch.linspace(-1., 1., steps=50)
x.requires_grad = True

# forward
y = sin(pi*x)

# backward
dydx = torch.autograd.grad(y, x,
                           retain_graph = True,
                           create_graph = True,
                           grad_outputs = torch.ones_like(x))[0]

# gráfico
x = x.detach()
y = y.detach()
dydx = dydx.detach()
plt.plot(x, y, ls='-', label='f')
plt.plot(x, pi*cos(pi*x), ls='-', label='df/dx')
plt.plot(x, dydx, ls='--', label='autograd')

plt.grid()
plt.legend()
plt.show()

