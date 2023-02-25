import torch

# modelo

# func. de ativação
def activation(p):
    return p

# perceptron
def neuron(x, w):
    p = x @ w[:2] + w[2]
    y = activation(p)
    return y

# (pré-)processamento
def preproc_in(x):
    return torch.where(x == False, -1., 1.)

def preproc_out(y):
    return torch.where(y < 0, False, True)

# pesos
w = torch.tensor([1.,
                  1.,
                  -1.5]).reshape(-1,1)

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
y = neuron(x, w)

# processamento dos dados de saída
y_out = preproc_out(y)

# saída do modelo
print("valores de saída")
print(y_out)
