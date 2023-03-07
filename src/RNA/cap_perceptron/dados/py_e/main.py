import torch

# modelo

# func. de ativação
def activation(z):
    return z

# perceptron
def neuron(x, w, b):
    ns = x.size(0)
    y = torch.empty((ns))
    for s in range(ns):
        z = torch.dot(w, x[s,:]) + b
        y[s] = activation(z)
    return y

# (pré-)processamento
def preproc_in(x):
    return torch.where(x == False, -1., 1.)

def preproc_out(y):
    return torch.where(y < 0, False, True)

# pesos
w = torch.tensor([1.,1.])
b = torch.tensor([-1.5])

# dados de entrada
x_in = torch.tensor([[True, True],
                     [True, False],
                     [False, True],
                     [False, False]])
print("valores de entrada")
print(x_in)

# processamento dos dados de entrada
x = preproc_in(x_in)

# aplicação do modelo
y = neuron(x, w, b)

# processamento dos dados de saída
y_out = preproc_out(y)

# saída do modelo
print("valores de saída")
print(y_out)
