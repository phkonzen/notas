import torch

# modelo

# pesos
w = torch.tensor([1.,1.])
b = torch.tensor([-1])

# func. de ativação
def activation(z):
    return torch.sign(z)

# perceptron
def neuron(x, w=w, b=b):
    ns = x.size(0)
    y = torch.empty((ns))
    for s in range(ns):
        z = torch.dot(w, x[s,:]) + b
        y[s] = activation(z)
    return y

# (pré-)processamento
def pproc_transform(x):
    return torch.where(x == False, -1., 1.)

def pproc_inverse_transform(x):
    return torch.where(x == -1., False, True)

# dados de entrada
X = torch.tensor([[True, True],
                  [True, False],
                  [False, True],
                  [False, False]])

print(f"\nDados de entrada\n{X}")

# processamento dos dados de entrada
X_in = pproc_transform(X)
print(f"Pré-processamento\n{X_in}")

# aplicação do modelo
y_out = neuron(X_in)
print(f"Valores estimados\n{y_out}")

# processamento dos dados de saída
y = pproc_inverse_transform(y_out)
print(f"(Pré-)processamento\n{y}")
