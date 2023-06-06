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

# dados de entrada
X = torch.tensor([[1., 1.],
                  [1., -1.],
                  [-1., 1.],
                  [-1., -1.]])

print(f"\nDados de entrada\n{X}")

# aplicação do modelo
y = neuron(X)
print(f"Valores estimados\n{y}")
