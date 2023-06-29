import torch
import matplotlib.pyplot as plt

# modelo

model = torch.nn.Sequential(
    torch.nn.Linear(2,200),
    torch.nn.Tanh(),
    torch.nn.Linear(200,200),
    torch.nn.Tanh(),
    torch.nn.Linear(200,25),
    torch.nn.Tanh(),
    torch.nn.Linear(25,1)
    )

# treinamento

## fun obj
a = -1.
b = 1.
def exact(x):
    y = torch.sin(torch.pi*x[:,0])*torch.sin(torch.pi*x[:,1])
    return y.reshape(-1,1)

def rhs(x):
    y = 2*torch.pi**2*torch.sin(torch.pi*x[:,0])*torch.sin(torch.pi*x[:,1])
    return y.reshape(-1,1)

## optimizador
optim = torch.optim.SGD(model.parameters(),
                        lr=1e-3, momentum=0.9)            
## scheaduler
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optim,
                                                       factor = 0.6,
                                                       min_lr = 1e-6,)

## num de amostras pts internos
n_in = 100
## num de amostras pts fronteira
n_bound = 25
## num max épocas
nepochs = 5000
## tolerância
tol = 1e-5
## output freq
eout = 100

def loss_fun(X_in, X_bound, model=model):

    ## pontos internos
    n_in = X_in.size(0)
    l_in = 0.
    for s in range(n_in):
        x = X_in[s:s+1,:].detach()
        x.requires_grad = True
        u = model(x)
        grad_u = torch.autograd.grad(u, x,
                                     create_graph = True,
                                     retain_graph = True)[0]
        u_x = grad_u[0,0]
        u_y = grad_u[0,1]

        u_xx = torch.autograd.grad(u_x, x,
                                   create_graph = True,
                                   retain_graph = True)[0][0,0]
        u_yy = torch.autograd.grad(u_y, x,
                                   create_graph = True,
                                   retain_graph = True)[0][0,1]
        l_in = torch.add(l_in, (rhs(x) + u_xx + u_yy)**2)
    l_in /= n_in
            

    ## pontos de contorno
    n_bound = X_bound.size(0)
    l_bound = 0.
    for s in range(n_bound):
        x = X_bound[s:s+1,:]
        u = model(x)
        l_bound = torch.add(l_bound, u**2)
    l_bound /= n_bound

    return l_in + 10*l_bound


# pts de fronteira
X_bound = torch.empty((4*n_bound, 2))
# pts internos
X_in = torch.empty((n_in, 2))

# épocas
for epoch in range(nepochs):

    # amostras: pts internos
    for s in range(n_in):
        X_in[s,:] = (a-b)*torch.rand(2) + b
    # amostras: pst fronteira
    s = 0
    for i in range(n_bound):
        # a <= x0 <= b, x1 = 0
        X_bound[s,0] = (a-b)*torch.rand(1) + b
        X_bound[s,1] = a
        s += 1

        # x0 = b, a <= x1 <= b
        X_bound[s,0] = b
        X_bound[s,1] = (a-b)*torch.rand(1) + b
        s += 1

        # x0 = a, a <= x1 < b
        X_bound[s,0] = a
        X_bound[s,1] = (a-b)*torch.rand(1) + b
        s += 1

        # a <= x0 <= b, x1 = b
        X_bound[s,0] = (a-b)*torch.rand(1) + b
        X_bound[s,1] = b
        s += 1
            
    # erro
    loss = loss_fun(X_in, X_bound)

    print(f'{epoch}: loss = {loss.item():.4e}, lr = {optim.param_groups[0]["lr"]:.2e}')
    if ((epoch+1) % eout == 0):
        # verificação
        fig = plt.figure()
        ax = fig.add_subplot()

        ns = 50
        x0 = torch.linspace(a, b, steps=ns)
        x1 = torch.linspace(a, b, steps=ns)
        X0, X1 = torch.meshgrid(x0, x1)
        X = torch.cat((X0.reshape(-1,1),
                       X1.reshape(-1,1)),
                      dim=1)

        y_esp = exact(X)
        Y = y_esp.reshape((ns,ns))
        c = ax.contour(X0, X1, Y, levels=10, colors='white')
        ax.clabel(c)

        y_est = model(X)
        Y = y_est.reshape((ns,ns))
        cf = ax.contourf(X0, X1, Y.detach(), levels=10, cmap='coolwarm')
        plt.colorbar(cf)

        # amostras
        ax.plot(X_in[:,0].detach(), X_in[:,1].detach(), ls='', marker='*', color='white')
        ax.plot(X_bound[:,0].detach(), X_bound[:,1].detach(), ls='', marker='*', color='white')
        
        ax.grid()
        ax.set_xlabel('$x_1$')
        ax.set_ylabel('$x_2$')
        plt.show()
        

    # critério de parada
    if (loss.item() < tol):
        break

    # backward
    optim.zero_grad()
    loss.backward()
    optim.step()
    scheduler.step(loss)
