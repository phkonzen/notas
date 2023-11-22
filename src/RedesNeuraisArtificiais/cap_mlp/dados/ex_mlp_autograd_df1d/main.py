import torch

# input
x = torch.linspace(-1., 1., steps=50).reshape(-1,1)
# requires grad
x.requires_grad = True

# output
y = torch.sin(torch.pi*x)

# compute gradients
y.backward(gradient=torch.ones_like(y))

# dy/dx
dydx = x.grad

# gráfico
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

fig = plt.figure(dpi=300)
ax = fig.add_subplot()

x = x.detach()
# fun
y = y.detach()
ax.plot(x, y, ls='--', label='$f$')
# dfun
df = torch.pi*torch.cos(torch.pi*x)
ax.plot(x, df, ls='-', label="$f'$")
# autograd
dydx = dydx.detach()
ax.plot(x, dydx, ls=':', label='autograd')

ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid()
plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')


