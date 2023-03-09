import torch

# modelo

# pesos e bias
model = {'weights': torch.zeros((2)),
         'bias': torch.zeros((1))}

# func. de ativação
def activation(z):
    return torch.sign(z)

# perceptron
def neuron(x, model=model):
    w = model['weights']
    b = model['bias']
    ns = x.size(0)
    y = torch.empty((ns))
    for s in range(ns):
        z = torch.dot(w, x[s,:]) + b
        y[s] = activation(z)
    return y

# algo treinamento
def train(X_train, y_train,
          model=model, nepochs=100):
    
    # núm. de amostras
    ns = X_train.size(0)
    
    w = model['weights']
    b = model['bias']

    y_est = torch.empty_like(y_train)
    
    # laço das épocas
    for epoch in range(nepochs):
        print(f"epoch = {epoch}\n\t{model}")
        not_updated = True
        # laço das amostras
        for s in range(ns):
            y_est[s] = neuron(X_train[s,:].reshape(1,-1),
                             model)
            if (y_train[s]*y_est[s] <= 0.):
                w += y_train[s]*X_train[s,:]
                b += y_train[s]
                not_updated = False
        # critério de parada
        if (not_updated):
            break
    
# dados de treinamento
X_train = torch.tensor([[1., 1.],
                        [1., -1.],
                        [-1., 1.],
                        [-1., -1.]])

y_train = torch.tensor([1., -1., -1., -1.])

# treinamento
print("\nTreinamento")
train(X_train, y_train)

# verificação
y_est = neuron(X_train)
print(f"\nVerificação\n{y_est}")
