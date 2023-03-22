import torch

# modelo

# pesos e bias
model = {'weights': torch.zeros((1)),
         'bias': torch.zeros((1))}

# func. de ativação
def activation(z):
    return z

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
def train(X_train, y_train, model=model):
    
    # núm. de amostras
    ns = X_train.size(0)

    # matriz
    M = torch.cat((X_train,
                   torch.ones((ns,1))),
                  dim=1)
    
    # sol. de Min. Quadrados
    c = torch.linalg.lstsq(M, y_train)[0]

    model['weights'] = c[0]
    model['bias'] = c[1]
    
    
# dados de treinamento
X_train = torch.tensor([0.5,
                        1.0,
                        1.5,
                        2.0]).reshape(-1,1)

y_train = torch.tensor([1.2,
                        2.1,
                        2.6,
                        3.6]).reshape(-1,1)

# treinamento
print("\nTreinamento")
train(X_train, y_train)

# verificação
print('Modelo após treinameto')
print(model)

y_est = neuron(X_train)
print(f"\nSaída\n{y_est}")
