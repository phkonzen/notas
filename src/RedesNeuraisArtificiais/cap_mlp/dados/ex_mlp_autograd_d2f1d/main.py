import torch

# input
x = torch.linspace(-1., 1., steps=50).reshape(-1,1)
# requires grad
x.requires_grad = True

# output
y = torch.sin(torch.pi*x)

# compute gradients
dydx = torch.autograd.grad(
    y, x,
    grad_outputs=torch.ones_like(y),
    retain_graph=True,
    create_graph=True)[0]

d2ydx2 = torch.autograd.grad(
    dydx, x,
    grad_outputs=torch.ones_like(dydx))[0]

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
# autograd dydx
dydx = dydx.detach()
ax.plot(x, dydx, ls=':', label='dydx')
# d2fun
d2f = -torch.pi**2*torch.sin(torch.pi*x)
ax.plot(x, d2f, ls='-', label="$f''$")
# autograd d2ydx2
d2ydx2 = d2ydx2.detach()
ax.plot(x, d2ydx2, ls=':', label='d2ydx2')

ax.legend()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid()
plt.savefig('fig.png', bbox_inches='tight')
plt.savefig('fig.pdf', bbox_inches='tight')


