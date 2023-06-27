import torch

class IdentityFun:

    def __init__(self):
        self.val = torch.Tensor([])
        self.dfdz = torch.Tensor([])

    def value(self, z):
        # f(z)
        self.val = z
        # dfdz
        self.dfdz = torch.ones_like(z)
        return self.val

    def grad(self, s):
        return self.dfdz[s]

class Unit:

    def __init__(self, nin, fact):
        # num. de entradas
        self.nin = nin
        # fun. de ativivação
        self.fact = fact
        # pesos
        self.weights = torch.rand((nin,1))
        # bias
        self.bias = torch.rand((1))
        # pré-ativação
        self.z = None
        # saída
        self.y = None

    def forward(self, X):
        self.X = X
        ns = self.X.size(0)
        self.z = self.X @ self.weights + self.bias
        self.y = self.fact.value(self.z)
        return self.y

class Loss:

    def __init__(self):
        self.y_est = torch.Tensor([])
        self.y = torch.Tensor([])
        self.ns = 0

    def partial(self):
        return (self.y_est - self.y)**2

    def grad(self, s):
        return 2. * (self.y_est[s] - self.y[s])

    def value(self, y_est, y):
        self.y_est = y_est
        self.y = y
        self.ns = y.size(0)
        return 1./self.ns * torch.sum(self.partial())

class OptimGD:

    # inicialização
    def __init__(self, model, loss, lr = 1.e-2):        
        # taxa de aprendizagem
        self.lr = lr

        # modelo
        self.model = model
        self.weights = self.model.weights
        self.bias = self.model.bias

        # função erro
        self.loss = loss

        # dimensões
        self.nin = model.weights.size(0)

        # gradientes
        self.dedw = torch.empty((self.nin, 1))
        self.dedb = torch.empty((1))

    # zera os gradientes
    def zero_grad(self):
        self.dedw = torch.zeros_like(self.dedw)
        self.dedb = torch.zeros_like(self.dedb)

    # computa os gradientes
    def backward(self):
        for s in range(self.loss.ns):
            dedy = self.loss.grad(s)
            dydz = self.model.fact.grad(s)
            dzdw = self.model.X[s,:]

            self.dedw += dedy * dydz * dzdw
            self.dedb += dedy * dydz

        self.dedw /= self.loss.ns
        self.dedb /= self.loss.ns
        
    # atualização dos pesos
    def step(self):
        self.model.weights -= self.lr * self.dedw
        self.model.bias -= self.lr * self.dedb


# dados de treinamento
X_train = torch.Tensor([0.5,
                        1.0,
                        1.5,
                        2.0]).reshape(-1,1)
y_train = torch.Tensor([1.2,
                        2.1,
                        2.6,
                        3.6]).reshape(-1,1)

# modelo
model = Unit(1, IdentityFun())

# treinamento
nepochs = 5000

# função erro
loss_fun = Loss()

# otimizador
optim = OptimGD(model, loss_fun)

print(f"{0}: {model.weights}, {model.bias}")

for epoch in range(nepochs):
    # saída estimada
    y_est = model.forward(X_train)
    # erro estimado
    loss = loss_fun.value(y_est, y_train)
    # zera os gradientes
    optim.zero_grad()
    # computa os gradientes
    optim.backward()
    # atualiza os passos
    optim.step()

    if ((epoch+1)%100 == 0):
        print(f"{epoch+1}: weights = {model.weights}, bias = {model.bias}")
    
        

